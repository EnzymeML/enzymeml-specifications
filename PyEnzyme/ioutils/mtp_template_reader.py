import numpy as np
import pandas as pd
import warnings

from typing import Any, Dict, List, OrderedDict, Tuple
from math import e, isnan
from PyEnzyme.core.abstractspecies import AbstractSpecies
from PyEnzyme.core.sboterm import SBOTerm

from PyEnzyme.core.vessel import Vessel
from PyEnzyme.core.protein import Protein
from PyEnzyme.core.reactant import Reactant
from PyEnzyme.core.measurement import Measurement
from PyEnzyme.core.replicate import Replicate
from PyEnzyme.core.datatypes import DataTypes
from PyEnzyme.core.reaction import Reaction
from PyEnzyme.core.datatypes import DataTypes
from PyEnzyme.core.reaction import Reaction


warnings.simplefilter(action="ignore", category=UserWarning)


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
    vessel = enzmldoc.add_to_vessels(
        id=vessel_info["ID"],
        name=vessel_info["Name"],
        volume=vessel_info["Volume value"],
        unit=vessel_info["Volume unit"],
    )

    # Proteins
    proteins = pd.read_excel(path, sheet_name="Proteins", skiprows=2)
    instances = get_instances(proteins, Protein, enzmldoc)
    for instance in instances:
        protein = enzmldoc.add_to_proteins(**instance | {"vessel_id": vessel.id})

    # Reactants
    reactants = pd.read_excel(path, sheet_name="Chemicals", skiprows=2, usecols="A:E")
    instances = get_instances(reactants, Reactant, enzmldoc)

    for instance in instances:
        reactant = enzmldoc.add_to_reactants(**instance | {"vessel_id": vessel.id})

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
    # Replace merged modifiers with modifier tag

    instances = get_instances(reactions, Reaction, enzmldoc)

    for i, instance in enumerate(instances):
        # Get Educts, Products and Modifiers to add to the reaction
        educts = parse_reaction_element_ids(instance, "educts", enzmldoc.reactants)
        products = parse_reaction_element_ids(instance, "products", enzmldoc.reactants)
        protein_modifiers = parse_reaction_element_ids(
            instance, "modifiers", enzmldoc.proteins
        )
        modifiers = parse_reaction_element_ids(
            instance, "modifiers", enzmldoc.reactants
        )

        instance.pop("educts")
        instance.pop("products")
        instance.pop("modifiers")

        reaction = enzmldoc.add_to_reactions(**instance)
        for educt in educts:
            reaction.add_to_educts(educt, ontology=SBOTerm.SUBSTRATE)
        for product in products:
            reaction.add_to_products(product, ontology=SBOTerm.PRODUCT)
        for modifier in modifiers:
            reaction.add_to_modifiers(modifier)
        for protein_modifier in protein_modifiers:
            reaction.add_to_modifiers(protein_modifier, ontology=SBOTerm.CATALYST)

        enzmldoc.reactions.append(reaction)

    # Set initial conditions of measurements
    measurement_conditions = get_measurement_conditions(path)
    ph_dict = extract_initial_conditions(path, "pH")

    enzmldoc = generate_measurements(
        path=path,
        enzmldoc=enzmldoc,
        ph_dict=ph_dict,
        measurement_conditions=measurement_conditions,
    )

    for measurement in enzmldoc.measurements:
        # Add pH
        # measurement.ph = ph_dict[measurement.name]

        # get initial concentrations of reactants
        for reactant in enzmldoc.reactants:
            unit = get_species_unit(path, reactant.name)
            init_concs = extract_initial_conditions(path, reactant.name)

            measurement.add_to_species(
                init_conc=init_concs[measurement.name],
                unit=unit,
                species_id=reactant.id,
                measurement_id=measurement.id,
            )

        # get initial concentrations of proteins
        for protein in enzmldoc.proteins:
            unit = get_species_unit(path, protein.name)
            init_concs = extract_initial_conditions(path, protein.name)

            measurement.add_to_species(
                init_conc=init_concs[measurement.name],
                unit=unit,
                species_id=protein.id,
                measurement_id=measurement.id,
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

    for meas_id, measurement in enumerate(enzmldoc.measurements):
        for spec_id, species in enumerate(measurement.species):
            if species.species_id == measured_reactant_id:
                species.add_to_replicates(
                    id=measurement.name,
                    species_id=species.species_id,
                    time_unit=measurement_conditions["Time unit"],
                    time=time,
                    data=data_dict[measurement.name],
                    is_calculated=False,
                    data_type=type_mapping[measurement_conditions["Data type"]],
                    data_unit="dimensionless",
                    measurement_id=measurement.id,
                )

    return enzmldoc


def parse_reaction_element_ids(
    instance: Reaction,
    target: str,
    species_list: List[AbstractSpecies],
):
    # Parse element names
    if "|" in instance[target]:
        elements = instance[target].split("|")
    else:
        elements = [instance[target]]

    # Get species ids or each name
    species_ids = []
    for element in elements:
        for species in species_list:
            if element.strip() == species.name:
                species_ids.append(species.id)

    return species_ids


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

    return "|".join(
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
    path: str,
    enzmldoc,
    ph_dict: dict,
    measurement_conditions: dict,
):
    """Generates a measurement for each well position in the template."""

    validate_plate_layout_homogeneity(path, enzmldoc)

    reactant_name = next(iter(enzmldoc.reactants)).name

    well_positions = extract_initial_conditions(path, reactant_name).keys()
    for well in well_positions:
        enzmldoc.add_to_measurements(
            name=well,
            temperature=enzmldoc.reactions[0].temperature,
            temperature_unit=enzmldoc.reactions[0].temperature_unit,
            ph=ph_dict[well],
            global_time_unit=measurement_conditions["Time unit"],
        )

    return enzmldoc


def get_measurement_conditions(path: str) -> Dict[str, Any]:
    return pd.read_excel(
        path, skiprows=2, sheet_name="Data", nrows=1, usecols="A:C"
    ).to_dict(orient="records")[0]