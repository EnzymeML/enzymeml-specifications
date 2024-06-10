## This is a generated file. Do not modify it manually!

from __future__ import annotations
from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from typing import List, Optional
from enum import Enum
from uuid import uuid4
from datetime import date, datetime


@dataclass_json
@dataclass
class EnzymeMLDocument:
    name: str
    references: List[str] = field(default_factory=list)
    created: Optional[str] = None
    modified: Optional[str] = None
    creators: List[Creator] = field(default_factory=list)
    vessels: List[Vessel] = field(default_factory=list)
    proteins: List[Protein] = field(default_factory=list)
    complexes: List[Complex] = field(default_factory=list)
    reactants: List[Reactant] = field(default_factory=list)
    reactions: List[Reaction] = field(default_factory=list)
    conditions: Optional[ReactionConditions] = None
    measurements: List[Measurement] = field(default_factory=list)
    kinetic_model: Optional[KineticModel] = None

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:EnzymeMLDocument/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:EnzymeMLDocument",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "name": "schema:name",
            "references": {
                "@type": "@id",
            },
        },
    )

    def add_to_creators(
        self,
        given_name: str,
        family_name: str,
        mail: str,
        **kwargs,
    ):
        params = {"given_name": given_name, "family_name": family_name, "mail": mail}

        self.creators.append(Creator(**params))

        return self.creators[-1]

    def add_to_vessels(
        self,
        name: str,
        volume: float,
        unit: UnitDefinition,
        constant: bool,
        creator_id: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "name": name,
            "volume": volume,
            "unit": unit,
            "constant": constant,
            "creator_id": creator_id,
        }

        self.vessels.append(Vessel(**params))

        return self.vessels[-1]

    def add_to_proteins(
        self,
        name: str,
        sequence: str,
        constant: bool = False,
        vessel_id: Optional[str] = None,
        ecnumber: Optional[str] = None,
        organism: Optional[str] = None,
        organism_tax_id: Optional[str] = None,
        references: List[str] = [],
        **kwargs,
    ):
        params = {
            "name": name,
            "sequence": sequence,
            "constant": constant,
            "vessel_id": vessel_id,
            "ecnumber": ecnumber,
            "organism": organism,
            "organism_tax_id": organism_tax_id,
            "references": references,
        }

        self.proteins.append(Protein(**params))

        return self.proteins[-1]

    def add_to_complexes(
        self,
        participants: List[str] = [],
        **kwargs,
    ):
        params = {"participants": participants}

        self.complexes.append(Complex(**params))

        return self.complexes[-1]

    def add_to_reactants(
        self,
        name: str,
        constant: bool = False,
        vessel_id: Optional[str] = None,
        canonical_smiles: Optional[str] = None,
        inchikey: Optional[str] = None,
        references: List[str] = [],
        **kwargs,
    ):
        params = {
            "name": name,
            "constant": constant,
            "vessel_id": vessel_id,
            "canonical_smiles": canonical_smiles,
            "inchikey": inchikey,
            "references": references,
        }

        self.reactants.append(Reactant(**params))

        return self.reactants[-1]

    def add_to_reactions(
        self,
        name: str,
        reversible: bool = False,
        species: List[ReactionSpecies] = [],
        modifiers: List[str] = [],
        **kwargs,
    ):
        params = {
            "name": name,
            "reversible": reversible,
            "species": species,
            "modifiers": modifiers,
        }

        self.reactions.append(Reaction(**params))

        return self.reactions[-1]

    def add_to_measurements(
        self,
        name: str,
        species: List[MeasurementData] = [],
        group_id: Optional[str] = None,
        **kwargs,
    ):
        params = {"name": name, "species": species, "group_id": group_id}

        self.measurements.append(Measurement(**params))

        return self.measurements[-1]


@dataclass_json
@dataclass
class Creator:
    given_name: str
    family_name: str
    mail: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:Creator/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: ["md:Creator", "schema:creator"],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "given_name": "schema:givenName",
            "family_name": "schema:familyName",
            "mail": "schema:email",
        },
    )


@dataclass_json
@dataclass
class Vessel:
    name: str
    volume: float
    unit: UnitDefinition
    constant: bool
    creator_id: Optional[str] = None

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:Vessel/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: ["md:Vessel", "OBO:OBI_0400081"],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "name": "schema:name",
            "volume": "OBO:OBI_0002139",
            "creator_id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class Protein:
    name: str
    sequence: str
    constant: bool = false
    vessel_id: Optional[str] = None
    ecnumber: Optional[str] = None
    organism: Optional[str] = None
    organism_tax_id: Optional[str] = None
    references: List[str] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:Protein/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: ["md:Protein", "schema:Protein"],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "name": "schema:name",
            "sequence": "OBO:GSSO_007262",
            "vessel_id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
            "organism": "OBO:OBI_0100026",
            "organism_tax_id": {
                "@type": "@id",
            },
            "references": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class Complex:
    participants: List[str] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:Complex/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:Complex",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "participants": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class Reactant:
    name: str
    constant: bool = false
    vessel_id: Optional[str] = None
    canonical_smiles: Optional[str] = None
    inchikey: Optional[str] = None
    references: List[str] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:Reactant/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:Reactant",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "name": "schema:name",
            "vessel_id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
            "references": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class Reaction:
    name: str
    reversible: bool = false
    species: List[ReactionSpecies] = field(default_factory=list)
    modifiers: List[str] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:Reaction/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:Reaction",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "modifiers": {
                "@type": "@id",
            },
        },
    )

    def add_to_species(
        self,
        species_id: str,
        stoichiometry: Optional[float] = None,
        **kwargs,
    ):
        params = {"species_id": species_id, "stoichiometry": stoichiometry}

        self.species.append(ReactionSpecies(**params))

        return self.species[-1]


@dataclass_json
@dataclass
class ReactionSpecies:
    species_id: str
    stoichiometry: Optional[float] = None

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:ReactionSpecies/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:ReactionSpecies",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "species_id": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class ReactionConditions:
    temperature: Optional[float] = None
    temperature_unit: Optional[UnitDefinition] = None
    ph: Optional[float] = None

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:ReactionConditions/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:ReactionConditions",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
        },
    )


@dataclass_json
@dataclass
class KineticModel:
    name: str
    equations: List[RateLaw] = field(default_factory=list)
    parameters: List[KineticParameter] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:KineticModel/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:KineticModel",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
        },
    )

    def add_to_equations(
        self,
        species_id: str,
        equation: Equation,
        **kwargs,
    ):
        params = {"species_id": species_id, "equation": equation}

        self.equations.append(RateLaw(**params))

        return self.equations[-1]

    def add_to_parameters(
        self,
        name: str,
        value: float,
        unit: UnitDefinition,
        constant: bool,
        initial_value: Optional[float] = None,
        upper: Optional[float] = None,
        lower: Optional[float] = None,
        stderr: Optional[float] = None,
        **kwargs,
    ):
        params = {
            "name": name,
            "value": value,
            "unit": unit,
            "constant": constant,
            "initial_value": initial_value,
            "upper": upper,
            "lower": lower,
            "stderr": stderr,
        }

        self.parameters.append(KineticParameter(**params))

        return self.parameters[-1]


@dataclass_json
@dataclass
class RateLaw:
    species_id: str
    equation: Equation

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:RateLaw/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:RateLaw",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "species_id": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class KineticParameter:
    name: str
    value: float
    unit: UnitDefinition
    constant: bool
    initial_value: Optional[float] = None
    upper: Optional[float] = None
    lower: Optional[float] = None
    stderr: Optional[float] = None

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:KineticParameter/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:KineticParameter",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
        },
    )


@dataclass_json
@dataclass
class Measurement:
    name: str
    species: List[MeasurementData] = field(default_factory=list)
    group_id: Optional[str] = None

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:Measurement/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:Measurement",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "group_id": {
                "@type": "@id",
            },
        },
    )

    def add_to_species(
        self,
        species_id: str,
        init_conc: float,
        data_type: DataTypes,
        data_unit: UnitDefinition,
        time_unit: UnitDefinition,
        time: List[float] = [],
        data: List[float] = [],
        is_calculated: bool = False,
        **kwargs,
    ):
        params = {
            "species_id": species_id,
            "init_conc": init_conc,
            "data_type": data_type,
            "data_unit": data_unit,
            "time_unit": time_unit,
            "time": time,
            "data": data,
            "is_calculated": is_calculated,
        }

        self.species.append(MeasurementData(**params))

        return self.species[-1]


@dataclass_json
@dataclass
class MeasurementData:
    species_id: str
    init_conc: float
    data_type: DataTypes
    data_unit: UnitDefinition
    time_unit: UnitDefinition
    time: List[float] = field(default_factory=list)
    data: List[float] = field(default_factory=list)
    is_calculated: bool = false

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:MeasurementData/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:MeasurementData",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "species_id": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class Equation:
    equation: Optional[str] = None
    variables: List[EqVariable] = field(default_factory=list)
    parameters: List[EqParameter] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:Equation/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:Equation",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "id": {
                "@type": "@id",
            },
        },
    )

    def add_to_variables(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        symbol: Optional[str] = None,
        **kwargs,
    ):
        params = {"id": id, "name": name, "symbol": symbol}

        self.variables.append(EqVariable(**params))

        return self.variables[-1]

    def add_to_parameters(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        symbol: Optional[str] = None,
        value: Optional[float] = None,
        **kwargs,
    ):
        params = {"id": id, "name": name, "symbol": symbol, "value": value}

        self.parameters.append(EqParameter(**params))

        return self.parameters[-1]


@dataclass_json
@dataclass
class EqVariable:
    name: Optional[str] = None
    symbol: Optional[str] = None

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:EqVariable/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:EqVariable",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "id": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class EqParameter:
    name: Optional[str] = None
    symbol: Optional[str] = None
    value: Optional[float] = None

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:EqParameter/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:EqParameter",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "id": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class UnitDefinition:
    base_units: List[BaseUnit] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:UnitDefinition/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:UnitDefinition",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
            "id": {
                "@type": "@id",
            },
        },
    )

    def add_to_base_units(
        self,
        kind: UnitType,
        exponent: int,
        multiplier: Optional[float] = None,
        scale: Optional[float] = None,
        **kwargs,
    ):
        params = {
            "kind": kind,
            "exponent": exponent,
            "multiplier": multiplier,
            "scale": scale,
        }

        self.base_units.append(BaseUnit(**params))

        return self.base_units[-1]


@dataclass_json
@dataclass
class BaseUnit:
    kind: UnitType
    exponent: int
    multiplier: Optional[float] = None
    scale: Optional[float] = None

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "md:BaseUnit/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "md:BaseUnit",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "md": "http://mdmodel.net/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "schema": "https://schema.org/",
        },
    )


class DataTypes(Enum):
    ABSORPTION = "abs"
    BIOMASS = "biomass"
    CONCENTRATION = "conc"
    CONVERSION = "conversion"
    FEED = "feed"
    PEAK_AREA = "peak-area"


class UnitType(Enum):
    AMPERE = "ampere"
    AVOGADRO = "avogadro"
    BECQUEREL = "becquerel"
    CANDELA = "candela"
    COULOMB = "coulomb"
    DIMENSIONLESS = "dimensionless"
    FARAD = "farad"
    GRAM = "gram"
    GRAY = "gray"
    HENRY = "henry"
    HERTZ = "hertz"
    ITEM = "item"
    JOULE = "joule"
    KATAL = "katal"
    KELVIN = "kelvin"
    KILOGRAM = "kilogram"
    LITRE = "litre"
    LUMEN = "lumen"
    LUX = "lux"
    METRE = "metre"
    MOLE = "mole"
    NEWTON = "newton"
    OHM = "ohm"
    PASCAL = "pascal"
    RADIAN = "radian"
    SECOND = "second"
    SIEMENS = "siemens"
    SIEVERT = "sievert"
    STERADIAN = "steradian"
    TESLA = "tesla"
    VOLT = "volt"
    WATT = "watt"
    WEBER = "weber"
