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
    created: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    modified: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    creators: List[Creator] = field(default_factory=list)
    vessels: List[Vessel] = field(default_factory=list)
    proteins: List[Protein] = field(default_factory=list)
    complexes: List[Complex] = field(default_factory=list)
    small_molecules: List[SmallMolecule] = field(default_factory=list)
    reactions: List[Reaction] = field(default_factory=list)
    measurements: List[Measurement] = field(default_factory=list)
    equations: List[Equation] = field(default_factory=list)
    parameters: List[Parameter] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:EnzymeMLDocument/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:EnzymeMLDocument",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "name": "schema:title",
            "references": {
                "@id": "schema:citation",
                "@type": "@id",
            },
            "created": "schema:dateCreated",
            "modified": "schema:dateModified",
            "creators": "schema:creator",
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

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.creators.append(Creator(**params))

        return self.creators[-1]

    def add_to_vessels(
        self,
        id: str,
        name: str,
        volume: float,
        unit: UnitDefinition,
        constant: bool = True,
        **kwargs,
    ):
        params = {
            "id": id,
            "name": name,
            "volume": volume,
            "unit": unit,
            "constant": constant,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.vessels.append(Vessel(**params))

        return self.vessels[-1]

    def add_to_proteins(
        self,
        id: str,
        name: str,
        constant: bool = False,
        sequence: Optional[str] = None,
        vessel_id: Optional[str] = None,
        ecnumber: Optional[str] = None,
        organism: Optional[str] = None,
        organism_tax_id: Optional[str] = None,
        references: list[str] = [],
        **kwargs,
    ):
        params = {
            "id": id,
            "name": name,
            "constant": constant,
            "sequence": sequence,
            "vessel_id": vessel_id,
            "ecnumber": ecnumber,
            "organism": organism,
            "organism_tax_id": organism_tax_id,
            "references": references,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.proteins.append(Protein(**params))

        return self.proteins[-1]

    def add_to_complexes(
        self,
        id: str,
        participants: list[str] = [],
        **kwargs,
    ):
        params = {"id": id, "participants": participants}

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.complexes.append(Complex(**params))

        return self.complexes[-1]

    def add_to_small_molecules(
        self,
        id: str,
        name: str,
        constant: bool = False,
        vessel_id: Optional[str] = None,
        canonical_smiles: Optional[str] = None,
        inchikey: Optional[str] = None,
        references: list[str] = [],
        **kwargs,
    ):
        params = {
            "id": id,
            "name": name,
            "constant": constant,
            "vessel_id": vessel_id,
            "canonical_smiles": canonical_smiles,
            "inchikey": inchikey,
            "references": references,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.small_molecules.append(SmallMolecule(**params))

        return self.small_molecules[-1]

    def add_to_reactions(
        self,
        id: str,
        name: str,
        reversible: bool = False,
        kinetic_law: Optional[Equation] = None,
        species: list[ReactionElement] = [],
        modifiers: list[str] = [],
        **kwargs,
    ):
        params = {
            "id": id,
            "name": name,
            "reversible": reversible,
            "kinetic_law": kinetic_law,
            "species": species,
            "modifiers": modifiers,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.reactions.append(Reaction(**params))

        return self.reactions[-1]

    def add_to_measurements(
        self,
        id: str,
        name: str,
        species: list[MeasurementData] = [],
        group_id: Optional[str] = None,
        ph: Optional[float] = None,
        temperature: Optional[float] = None,
        temperature_unit: Optional[UnitDefinition] = None,
        **kwargs,
    ):
        params = {
            "id": id,
            "name": name,
            "species": species,
            "group_id": group_id,
            "ph": ph,
            "temperature": temperature,
            "temperature_unit": temperature_unit,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.measurements.append(Measurement(**params))

        return self.measurements[-1]

    def add_to_equations(
        self,
        unit: UnitDefinition,
        equation_type: EquationType,
        equation: str,
        species_id: Optional[str] = None,
        variables: list[EqVariable] = [],
        parameters: list[EqParameter] = [],
        **kwargs,
    ):
        params = {
            "unit": unit,
            "equation_type": equation_type,
            "equation": equation,
            "species_id": species_id,
            "variables": variables,
            "parameters": parameters,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.equations.append(Equation(**params))

        return self.equations[-1]

    def add_to_parameters(
        self,
        id: str,
        name: str,
        value: Optional[float] = None,
        unit: Optional[UnitDefinition] = None,
        initial_value: Optional[float] = None,
        upper: Optional[float] = None,
        lower: Optional[float] = None,
        stderr: Optional[float] = None,
        constant: Optional[bool] = True,
        **kwargs,
    ):
        params = {
            "id": id,
            "name": name,
            "value": value,
            "unit": unit,
            "initial_value": initial_value,
            "upper": upper,
            "lower": lower,
            "stderr": stderr,
            "constant": constant,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.parameters.append(Parameter(**params))

        return self.parameters[-1]


@dataclass_json
@dataclass
class Creator:
    given_name: str
    family_name: str
    mail: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:Creator/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: ["enzml:Creator", "schema:person"],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
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
    constant: bool = True

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:Vessel/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: ["enzml:Vessel", "OBO:OBI_0400081"],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
            "name": "schema:name",
            "volume": "OBO:OBI_0002139",
        },
    )


@dataclass_json
@dataclass
class Protein:
    name: str
    constant: bool = False
    sequence: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    vessel_id: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    ecnumber: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    organism: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    organism_tax_id: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    references: List[str] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:Protein/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: ["enzml:Protein", "schema:Protein"],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "id": {
                "@type": "@id",
            },
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
                "@id": "schema:citation",
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
        default_factory=lambda: "enzml:Complex/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:Complex",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
            "participants": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class SmallMolecule:
    name: str
    constant: bool = False
    vessel_id: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    canonical_smiles: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    inchikey: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    references: List[str] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:SmallMolecule/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:SmallMolecule",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
            "name": "schema:name",
            "vessel_id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
            "references": {
                "@id": "schema:citation",
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class Reaction:
    name: str
    reversible: bool = False
    kinetic_law: Optional[Equation] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    species: List[ReactionElement] = field(default_factory=list)
    modifiers: List[str] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:Reaction/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:Reaction",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
            "modifiers": {
                "@type": "@id",
            },
        },
    )

    def add_to_species(
        self,
        species_id: str,
        stoichiometry: float,
        **kwargs,
    ):
        params = {"species_id": species_id, "stoichiometry": stoichiometry}

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.species.append(ReactionElement(**params))

        return self.species[-1]


@dataclass_json
@dataclass
class ReactionElement:
    species_id: str
    stoichiometry: float

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:ReactionElement/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:ReactionElement",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "species_id": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class Equation:
    unit: UnitDefinition
    equation_type: EquationType
    equation: str
    species_id: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    variables: List[EqVariable] = field(default_factory=list)
    parameters: List[EqParameter] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:Equation/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:Equation",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "species_id": {
                "@type": "@id",
            },
        },
    )

    def add_to_variables(
        self,
        id: str,
        name: str,
        symbol: Optional[str] = None,
        **kwargs,
    ):
        params = {"id": id, "name": name, "symbol": symbol}

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.variables.append(EqVariable(**params))

        return self.variables[-1]

    def add_to_parameters(
        self,
        id: str,
        name: str,
        symbol: Optional[str] = None,
        value: Optional[float] = None,
        **kwargs,
    ):
        params = {"id": id, "name": name, "symbol": symbol, "value": value}

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.parameters.append(EqParameter(**params))

        return self.parameters[-1]


@dataclass_json
@dataclass
class Parameter:
    name: str
    value: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    unit: Optional[UnitDefinition] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    initial_value: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    upper: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    lower: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    stderr: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    constant: bool = True

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:Parameter/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:Parameter",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class Measurement:
    name: str
    species: List[MeasurementData] = field(default_factory=list)
    group_id: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    ph: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    temperature: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    temperature_unit: Optional[UnitDefinition] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:Measurement/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:Measurement",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "id": {
                "@id": "schema:identifier",
                "@type": "@id",
            },
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
        time: list[float] = [],
        data: list[float] = [],
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

        if "id" in kwargs:
            params["id"] = kwargs["id"]

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
    is_calculated: bool = False

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:MeasurementData/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:MeasurementData",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "species_id": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class UnitDefinition:
    name: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    base_units: List[BaseUnit] = field(default_factory=list)

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:UnitDefinition/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:UnitDefinition",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
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

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.base_units.append(BaseUnit(**params))

        return self.base_units[-1]


@dataclass_json
@dataclass
class BaseUnit:
    kind: UnitType
    exponent: int
    multiplier: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    scale: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:BaseUnit/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:BaseUnit",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
        },
    )


@dataclass_json
@dataclass
class EqVariable:
    name: str
    symbol: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:EqVariable/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:EqVariable",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "id": {
                "@type": "@id",
            },
        },
    )


@dataclass_json
@dataclass
class EqParameter:
    name: str
    symbol: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    value: Optional[float] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "enzml:EqParameter/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "enzml:EqParameter",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "enzml": "http://www.enzymeml.org/v2/",
            "schema": "https://schema.org/",
            "OBO": "http://purl.obolibrary.org/obo/",
            "id": {
                "@type": "@id",
            },
        },
    )


class DataTypes(Enum):
    ABSORPTION = "abs"
    BIOMASS = "biomass"
    CONCENTRATION = "conc"
    CONVERSION = "conversion"
    FEED = "feed"
    PEAK_AREA = "peak-area"


class EquationType(Enum):
    ASSIGNMENT = "assignment"
    INITIAL_ASSIGNMENT = "initialAssignment"
    ODE = "ode"
    RATE_LAW = "rateLaw"


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
