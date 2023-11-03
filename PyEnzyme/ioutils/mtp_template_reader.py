import numpy as np
import pandas as pd
import re

from typing import Any, Dict, List, OrderedDict, Tuple
from math import isnan

from PyEnzyme.core.creator import Creator
from PyEnzyme.core.vessel import Vessel
from PyEnzyme.core.protein import Protein
from PyEnzyme.core.reactant import Reactant
from PyEnzyme.core.measurement import Measurement
from PyEnzyme.core.replicate import Replicate
from PyEnzyme.core.datatypes import DataTypes
from PyEnzyme.core.reaction import Reaction
from PyEnzyme.core.datatypes import DataTypes


def read_96well_template(cls, path: str):
    """Parser for 96 well plate template. Creates an EnzymeML document"""

    general_info = pd.read_excel(path, sheet_name="General Information", skiprows=1)

    params = dict(
        name=general_info.iloc[0, 1],
        created=str(general_info.iloc[1, 1]),
        doi=None,
        pubmedid=general_info.iloc[3, 1],
        url=general_info.iloc[4, 1],
    )

    enzmldoc = cls(**params)

    # User information
    user_infos = pd.read_excel(
        path, sheet_name="General Information", skiprows=9, nrows=8
    ).dropna()

    for record in user_infos.to_dict(orient="records"):
        enzmldoc.add_to_creators(
            family_name=record["Family Name"],
            given_name=record["Given Name"],
            mail=record["Mail"],
        )

    # Vessel (96 well plate)
    vessel_info = pd.read_excel(
        path, sheet_name="General Information", skiprows=18, nrows=2
    ).dropna()

    vessel_info = vessel_info.to_dict(orient="records")[0]
    vessel = Vessel(
        id=vessel_info["ID"],
        name=vessel_info["Name"],
        volume=vessel_info["Volume value"],
        unit=vessel_info["Volume unit"],
    )
    enzmldoc.vessels.append(vessel)

    # Proteins
    proteins = pd.read_excel(path, sheet_name="Proteins", skiprows=2)
    instances = get_instances(proteins, Protein, enzmldoc)
    for instance in instances:
        protein = Protein(**instance | {"vessel_id": vessel.id})
        enzmldoc.proteins.append(protein)

    # Reactants
    reactants = pd.read_excel(path, sheet_name="Chemicals", skiprows=2, usecols="A:E")
    instances = get_instances(reactants, Reactant, enzmldoc)

    for instance in instances:
        reactant = Reactant(**instance | {"vessel_id": vessel.id})
        enzmldoc.reactants.append(reactant)

    # Reactions
    reactions = pd.read_excel(path, sheet_name="Reactions", skiprows=2, usecols="A:J")

    # Merge proteins and modifiers
    nu_mods = [
        merge_protein_modifier(protein, modifier)
        for modifier, protein in zip(
            reactions.Modifiers.values.tolist(), reactions.Proteins.values.tolist()
        )
    ]

    # Replace merged modifiers with modifier tag
    reactions.Modifiers = nu_mods

    instances = get_instances(reactions, Reaction, enzmldoc)

    for instance in instances:
        # Get Educts, Products and Modifiers to add to the reaction
        educts = parse_reaction_element(instance.get("educts"))
        products = parse_reaction_element(instance.get("products"))
        modifiers = parse_reaction_element(instance.get("modifiers"))

        instance.pop("educts")
        instance.pop("products")
        instance.pop("modifiers")

        # Instantiate Reaction
        print(educts)
        reaction = Reaction(**instance)

        add_instances(reaction.addModifier, modifiers, enzmldoc)
        add_instances(reaction.addEduct, educts, enzmldoc)
        add_instances(reaction.addProduct, products, enzmldoc)

        enzmldoc.addReaction(reaction)

    # Set initial conditions of measurements
    measurement_conditions = get_measurement_conditions(path)

    enzmldoc = generate_measurements(
        path=path,
        enzmldoc=enzmldoc,
        temperature=measurement_conditions["Temperature"],
        temperature_unit=measurement_conditions["Temperature unit"],
    )

    ph_dict = extract_initial_conditions(path, "pH")

    for measurement in enzmldoc.measurements:
        # Add pH
        measurement.ph = ph_dict[measurement.name]

        # get initial concentrations of reactants
        for reactant_id in enzmldoc.reactant_dict:
            reactant_name = enzmldoc.getReactant(reactant_id).name
            unit = get_species_unit(path, reactant_name)
            init_concs = extract_initial_conditions(path, reactant_name)

            measurement.addData(
                init_conc=init_concs[measurement.name],
                unit=unit,
                reactant_id=reactant_id,
            )

        # get initial concentrations of proteins
        for protein_id in enzmldoc.protein_dict:
            protein_name = enzmldoc.getProtein(protein_id).name
            unit = get_species_unit(path, protein_name)
            init_concs = extract_initial_conditions(path, protein_name)

            measurement.addData(
                init_conc=init_concs[measurement.name], unit=unit, protein_id=protein_id
            )

    # Add measurement data
    type_mapping = {
        "Concentration": DataTypes.CONCENTRATION,
        "Absorption": DataTypes.ABSORPTION,
        "Fluorescence": DataTypes.FLUORESCENCE,
        "Luminescence": DataTypes.LUMINESCENCE,
        "Conversion [%]": DataTypes.CONVERSION,
        "Peak Area": DataTypes.PEAK_AREA,
        "Total concentration after addition": DataTypes.CONCENTRATION,
    }

    # Ensure that reactant is specified in the 'Chemicals' sheet
    try:
        measured_reactant_id = [
            reactant.id
            for reactant in enzmldoc.reactants
            if reactant.name == measurement_conditions["Reactant"]
        ][0]
    except IndexError:
        raise ValueError(
            f"Reactant {measurement_conditions['Reactant']} not found in excel template sheet 'Chemicals'."
        )

    time, data_dict = get_timecourse_data(path)

    for measurement in enzmldoc.measurement_dict.values():
        measurement.addReplicates(
            Replicate(
                id=measurement.name,
                species_id=measured_reactant_id,
                time_unit=measurement_conditions["Time unit"],
                time=time,
                data=data_dict[measurement.name],
                is_calculated=False,
                data_type=type_mapping[measurement_conditions["Data type"]],
                data_unit="dimensionless",
            ),
            enzmldoc,
        )
    return enzmldoc


def parse_reaction_element(elements):
    if repr(elements) == "nan":
        return []

    return elements


def validate_plate_layout_homogeneity(path: str, enzmldoc):
    """Validates that for all species the initial concentration is set
    for all well positions."""

    proteins = [protein.name for protein in enzmldoc.proteins]
    reactants = [reactant.name for reactant in enzmldoc.reactants]

    species = proteins + reactants

    well_ids = []
    species_well_ids = []
    for spec in species:
        spec_well_ids = extract_initial_conditions(path, spec).keys()
        species_well_ids.append(spec_well_ids)
        well_ids = well_ids + list(spec_well_ids)

    unique_well_ids = set(well_ids)

    for spec, spec_well_ids in zip(species, species_well_ids):
        if set(spec_well_ids) != unique_well_ids:
            raise ValueError(
                f"Initial concentration for plate postion(s)"
                f"{list(set(spec_well_ids) ^ set(unique_well_ids))} of {spec} not specified."
            )


def merge_protein_modifier(protein, modifier):
    proteins = repr(protein).split(",")
    modifier = repr(modifier).split(",")
    entities = proteins + modifier

    return ",".join(
        [entity.replace("'", "").strip() for entity in entities if entity != "nan"]
    )


def extract_initial_conditions(path: str, sheet_name: str) -> OrderedDict[str, float]:
    """Extracts initial concentration values for each cell, representing a
    position on a 96 well plate."""

    plate = pd.read_excel(
        path,
        sheet_name=sheet_name,
        skiprows=3,
        nrows=8,
        usecols="A:M",
        header=0,
        index_col=0,
    )

    plate_dict = plate.T.to_dict(orient="dict")

    # flatten nested dict
    flat_plate_dict = flatten_dict(plate_dict)

    # remove nan values
    clean_dict = OrderedDict(
        {
            key: value
            for key, value in flat_plate_dict.items()
            if not isnan(flat_plate_dict[key])
        }
    )

    return clean_dict


def get_instances(sheet: pd.DataFrame, obj, enzmldoc) -> list:
    mapping = get_template_map(obj)
    instances = extract_values(sheet, mapping)

    return [clean_instance(instance, enzmldoc) for instance in instances]


def get_template_map(obj) -> dict:
    """Extracts the template mappings"""

    return {
        field.field_info.extra.get("template_alias"): name
        for name, field in obj.__fields__.items()
        if field.field_info.extra.get("template_alias")
    }


def extract_values(sheet: pd.DataFrame, mapping: Dict[str, str]) -> list:
    # Get all valid columns
    cols = [col for col in sheet.columns if "Unnamed" not in col]
    sheet = sheet[cols]
    sheet = sheet.replace(r"^\s*$", np.nan, regex=True)
    sheet = sheet.dropna(thresh=len(mapping) - 2)
    records = sheet.to_dict(orient="records")

    return [
        {
            mapping.get(key): item
            for key, item in record.items()
            if item and mapping.get(key) and "nan" != repr(item)
        }
        for record in records
    ]


def clean_instance(instance: dict, enzmldoc) -> dict:
    def get_vessel_name(name: str, enzmldoc):
        return enzmldoc.getVessel(name).id

    def get_constant(constant: str, enzmldoc):
        if constant == "Constant":
            return True
        elif constant == "Not constant":
            return False

    def get_reversible(reversible: str, enzmldoc):
        if reversible == "reversible":
            return True
        elif reversible == "irreversible":
            return False

    def clean_temp_unit(temp_unit: str, enzmldoc):
        return temp_unit.replace("°", "")

    def clean_uniprotid(uniprotid: str, enzmldoc):
        if repr(uniprotid) == "nan":
            return None
        else:
            return uniprotid

    mapping = {
        "vessel_id": get_vessel_name,
        "constant": get_constant,
        "temperature_unit": clean_temp_unit,
        "reversible": get_reversible,
        "uniprotid": clean_uniprotid,
    }

    for key, item in instance.items():
        if key in mapping:
            instance[key] = mapping[key](item, enzmldoc)
    return instance


def flatten_dict(nested_dict: Dict[str, Dict]) -> dict:
    """Flattens nested dict. Concatenates inner and outer keys."""

    flat_dict = OrderedDict()
    for outer_k, outer_v in nested_dict.items():
        for inner_k, inner_v in outer_v.items():
            flat_dict.update({outer_k.strip() + str(inner_k): inner_v})

    return flat_dict


def get_timecourse_data(path: str) -> Tuple[List[float], Dict[str, List[float]]]:
    df = pd.read_excel(path, skiprows=4, sheet_name="Data")
    time = df.pop("Time").values.tolist()
    data_dict = df.to_dict(orient="list")

    return time, data_dict


def get_species_unit(path: str, sheet_name: str) -> str:
    """Extracts the unit of the reactant / protein from the template."""

    unit = pd.read_excel(path, sheet_name=sheet_name, skiprows=2, nrows=0, usecols="D")
    return unit.columns[0]


def generate_measurements(
    path: str, enzmldoc, temperature: float, temperature_unit: str
):
    """Generates a measurement for each well position in the template."""

    validate_plate_layout_homogeneity(path, enzmldoc)

    reactant_name = next(iter(enzmldoc.reactants)).name

    well_positions = extract_initial_conditions(path, reactant_name).keys()
    for well in well_positions:
        enzmldoc.addMeasurement(
            Measurement(
                name=well,
                temperature=temperature,
                temperature_unit=temperature_unit,
            )
        )

    return enzmldoc


def get_measurement_conditions(path: str) -> Dict[str, Any]:
    return pd.read_excel(
        path, skiprows=2, sheet_name="Data", nrows=1, usecols="A:E"
    ).to_dict(orient="records")[0]


def add_instances(fun, elements, enzmldoc) -> None:
    all_species = {**enzmldoc.protein_dict, **enzmldoc.reactant_dict}
    for id, species in all_species.items():
        if species.name in elements:
            fun(
                species_id=id,
                stoichiometry=1.0,
                constant=False,
                enzmldoc=enzmldoc,
            )
