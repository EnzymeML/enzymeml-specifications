"""
This file contains Pydantic XML model definitions for data validation.

Pydantic is a data validation library that uses Python type annotations.
It allows you to define data models with type hints that are validated
at runtime while providing static type checking.

Usage example:
```python
from my_model import MyModel

# Validates data at runtime
my_model = MyModel(name="John", age=30)

# Type-safe - my_model has correct type hints
print(my_model.name)

# Will raise error if validation fails
try:
    MyModel(name="", age=30)
except ValidationError as e:
    print(e)
```

For more information see:
https://pydantic-xml.readthedocs.io/en/latest/

WARNING: This is an auto-generated file.
Do not edit directly - any changes will be overwritten.
"""


## This is a generated file. Do not modify it manually!

from __future__ import annotations
from typing import Dict, List, Optional
from uuid import uuid4
from datetime import date, datetime
from xml.dom import minidom
from enum import Enum

from lxml.etree import _Element
from pydantic import PrivateAttr, model_validator
from pydantic_xml import attr, element, BaseXmlModel


class EnzymeMLDocument(
    BaseXmlModel,
    search_mode="unordered",
):
    name: str = element(
        tag="name",
        description="""Title of the EnzymeML Document.""",
        json_schema_extra=dict(
            term="schema:title",
        ),
    )

    references: list[str] = element(
        default_factory=list,
        tag="references",
        description="""Contains references to publications, databases, and arbitrary links to the web.""",
        json_schema_extra=dict(
            term="schema:citation",
        ),
    )

    created: Optional[str] = element(
        default=None,
        tag="created",
        description="""Date the EnzymeML document was created.""",
        json_schema_extra=dict(
            term="schema:dateCreated",
        ),
    )

    modified: Optional[str] = element(
        default=None,
        tag="modified",
        description="""Date the EnzymeML document was modified.""",
        json_schema_extra=dict(
            term="schema:dateModified",
        ),
    )

    creators: list[Creator] = element(
        default_factory=list,
        tag="creators",
        description="""Contains all authors that are part of the experiment.""",
        json_schema_extra=dict(
            term="schema:creator",
        ),
    )

    vessels: list[Vessel] = element(
        default_factory=list,
        tag="vessels",
        description="""Contains all vessels that are part of the experiment.""",
        json_schema_extra=dict(),
    )

    proteins: list[Protein] = element(
        default_factory=list,
        tag="proteins",
        description="""Contains all proteins that are part of the experiment.""",
        json_schema_extra=dict(),
    )

    complexes: list[Complex] = element(
        default_factory=list,
        tag="complexes",
        description="""Contains all complexes that are part of the experiment.""",
        json_schema_extra=dict(),
    )

    small_molecules: list[SmallMolecule] = element(
        default_factory=list,
        tag="small_molecules",
        description="""Contains all reactants that are part of the experiment.""",
        json_schema_extra=dict(),
    )

    reactions: list[Reaction] = element(
        default_factory=list,
        tag="reactions",
        description="""Dictionary mapping from reaction IDs to reaction-describing objects.""",
        json_schema_extra=dict(),
    )

    measurements: list[Measurement] = element(
        default_factory=list,
        tag="measurements",
        description="""Contains measurements that describe outcomes of an experiment.""",
        json_schema_extra=dict(),
    )

    equations: list[Equation] = element(
        default_factory=list,
        tag="equations",
        description="""Contains ordinary differential equations that describe the kinetic model.""",
        json_schema_extra=dict(),
    )

    parameters: list[Parameter] = element(
        default_factory=list,
        tag="parameters",
        description="""List of parameters that are part of the equation""",
        json_schema_extra=dict(),
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

        self.proteins.append(Protein(**params))

        return self.proteins[-1]

    def add_to_complexes(
        self,
        id: str,
        name: str,
        constant: bool = False,
        vessel_id: Optional[str] = None,
        participants: list[str] = [],
        **kwargs,
    ):
        params = {
            "id": id,
            "name": name,
            "constant": constant,
            "vessel_id": vessel_id,
            "participants": participants,
        }

        self.complexes.append(Complex(**params))

        return self.complexes[-1]

    def add_to_small_molecules(
        self,
        id: str,
        name: str,
        constant: bool = False,
        vessel_id: Optional[str] = None,
        canonical_smiles: Optional[str] = None,
        inchi: Optional[str] = None,
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
            "inchi": inchi,
            "inchikey": inchikey,
            "references": references,
        }

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

        self.reactions.append(Reaction(**params))

        return self.reactions[-1]

    def add_to_measurements(
        self,
        id: str,
        name: str,
        species_data: list[MeasurementData] = [],
        group_id: Optional[str] = None,
        ph: Optional[float] = None,
        temperature: Optional[float] = None,
        temperature_unit: Optional[UnitDefinition] = None,
        **kwargs,
    ):
        params = {
            "id": id,
            "name": name,
            "species_data": species_data,
            "group_id": group_id,
            "ph": ph,
            "temperature": temperature,
            "temperature_unit": temperature_unit,
        }

        self.measurements.append(Measurement(**params))

        return self.measurements[-1]

    def add_to_equations(
        self,
        equation: str,
        equation_type: EquationType,
        species_id: Optional[str] = None,
        variables: list[Variable] = [],
        **kwargs,
    ):
        params = {
            "equation": equation,
            "equation_type": equation_type,
            "species_id": species_id,
            "variables": variables,
        }

        self.equations.append(Equation(**params))

        return self.equations[-1]

    def add_to_parameters(
        self,
        id: str,
        name: str,
        symbol: str,
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
            "symbol": symbol,
            "value": value,
            "unit": unit,
            "initial_value": initial_value,
            "upper": upper,
            "lower": lower,
            "stderr": stderr,
            "constant": constant,
        }

        self.parameters.append(Parameter(**params))

        return self.parameters[-1]

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class Creator(
    BaseXmlModel,
    search_mode="unordered",
):
    given_name: str = element(
        tag="given_name",
        description="""Given name of the author or contributor.""",
        json_schema_extra=dict(
            term="schema:givenName",
        ),
    )

    family_name: str = element(
        tag="family_name",
        description="""Family name of the author or contributor.""",
        json_schema_extra=dict(
            term="schema:familyName",
        ),
    )

    mail: str = element(
        tag="mail",
        description="""Email address of the author or contributor.""",
        json_schema_extra=dict(
            term="schema:email",
        ),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class Vessel(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str = element(
        tag="id",
        description="""Unique identifier of the vessel.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    name: str = element(
        tag="name",
        description="""Name of the used vessel.""",
        json_schema_extra=dict(
            term="schema:name",
        ),
    )

    volume: float = element(
        tag="volume",
        description="""Volumetric value of the vessel.""",
        json_schema_extra=dict(
            term="OBO:OBI_0002139",
        ),
    )

    unit: UnitDefinition = element(
        tag="unit",
        description="""Volumetric unit of the vessel.""",
        json_schema_extra=dict(),
    )

    constant: bool = element(
        tag="constant",
        description="""Whether the volume of the vessel is constant or not.""",
        json_schema_extra=dict(),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class Protein(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str = element(
        tag="id",
        description="""Unique internal identifier of the protein.""",
        json_schema_extra=dict(
            schema="identifier",
        ),
    )

    name: str = element(
        tag="name",
        json_schema_extra=dict(
            term="schema:name",
        ),
    )

    constant: bool = element(tag="constant", json_schema_extra=dict())

    sequence: Optional[str] = element(
        default=None,
        tag="sequence",
        description="""Amino acid sequence of the protein""",
        json_schema_extra=dict(
            term="OBO:GSSO_007262",
        ),
    )

    vessel_id: Optional[str] = element(
        default=None,
        tag="vessel_id",
        description="""Unique identifier of the vessel this protein has been used in.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    ecnumber: Optional[str] = element(
        default=None,
        tag="ecnumber",
        description="""EC number of the protein.""",
        json_schema_extra=dict(),
    )

    organism: Optional[str] = element(
        default=None,
        tag="organism",
        description="""Organism the protein was expressed in.""",
        json_schema_extra=dict(
            term="OBO:OBI_0100026",
        ),
    )

    organism_tax_id: Optional[str] = element(
        default=None,
        tag="organism_tax_id",
        description="""Taxonomy identifier of the expression host.""",
        json_schema_extra=dict(),
    )

    references: list[str] = element(
        default_factory=list,
        tag="references",
        description="""Array of references to publications, database entries, etc. that describe the
            protein.""",
        json_schema_extra=dict(
            term="schema:citation",
        ),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class Complex(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str = element(
        tag="id",
        description="""Unique identifier of the complex.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    name: str = element(
        tag="name",
        json_schema_extra=dict(
            term="schema:name",
        ),
    )

    constant: bool = element(tag="constant", json_schema_extra=dict())

    vessel_id: Optional[str] = element(
        default=None,
        tag="vessel_id",
        description="""Unique identifier of the vessel this complex has been used in.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    participants: list[str] = element(
        default_factory=list,
        tag="participants",
        description="""Array of IDs the complex contains""",
        json_schema_extra=dict(),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class SmallMolecule(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str = element(
        tag="id",
        description="""Unique identifier of the small molecule.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    name: str = element(
        tag="name",
        json_schema_extra=dict(
            term="schema:name",
        ),
    )

    constant: bool = element(tag="constant", json_schema_extra=dict())

    vessel_id: Optional[str] = element(
        default=None,
        tag="vessel_id",
        description="""Unique identifier of the vessel this small molecule has been used in.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    canonical_smiles: Optional[str] = element(
        default=None,
        tag="canonical_smiles",
        description="""Canonical Simplified Molecular-Input Line-Entry System (SMILES) encoding of
            the reactant.""",
        json_schema_extra=dict(),
    )

    inchi: Optional[str] = element(
        default=None,
        tag="inchi",
        description="""International Chemical Identifier (InChI) encoding of the reactant.""",
        json_schema_extra=dict(),
    )

    inchikey: Optional[str] = element(
        default=None,
        tag="inchikey",
        description="""Hashed International Chemical Identifier (InChIKey) encoding of the reactant.""",
        json_schema_extra=dict(),
    )

    references: list[str] = element(
        default_factory=list,
        tag="references",
        description="""Array of references to publications, database entries, etc. that describe the
            reactant.""",
        json_schema_extra=dict(
            term="schema:citation",
        ),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class Reaction(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str = element(
        tag="id",
        description="""Unique identifier of the reaction.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    name: str = element(
        tag="name", description="""Name of the reaction.""", json_schema_extra=dict()
    )

    reversible: bool = element(
        tag="reversible",
        description="""Whether the reaction is reversible or irreversible""",
        json_schema_extra=dict(),
    )

    kinetic_law: Optional[Equation] = element(
        default=None,
        tag="kinetic_law",
        description="""Mathematical expression of the reaction.""",
        json_schema_extra=dict(),
    )

    species: list[ReactionElement] = element(
        default_factory=list,
        tag="species",
        description="""List of reaction elements that are part of the reaction.""",
        json_schema_extra=dict(),
    )

    modifiers: list[str] = element(
        default_factory=list,
        tag="modifiers",
        description="""List of reaction elements that are not part of the reaction but influence it.""",
        json_schema_extra=dict(),
    )

    def add_to_species(
        self,
        species_id: str,
        stoichiometry: float,
        **kwargs,
    ):
        params = {"species_id": species_id, "stoichiometry": stoichiometry}

        self.species.append(ReactionElement(**params))

        return self.species[-1]

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class ReactionElement(
    BaseXmlModel,
    search_mode="unordered",
):
    species_id: str = element(
        tag="species_id",
        description="""Internal identifier to either a protein or reactant defined in the
            EnzymeMLDocument.""",
        json_schema_extra=dict(
            schema="identifier",
        ),
    )

    stoichiometry: float = element(
        tag="stoichiometry",
        description="""Float number representing the associated stoichiometry.""",
        json_schema_extra=dict(),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class Equation(
    BaseXmlModel,
    search_mode="unordered",
):
    equation: str = element(
        tag="equation",
        description="""Mathematical expression of the equation.""",
        json_schema_extra=dict(),
    )

    equation_type: EquationType = element(
        tag="equation_type",
        description="""Type of the equation.""",
        json_schema_extra=dict(),
    )

    species_id: Optional[str] = element(
        default=None,
        tag="species_id",
        description="""Internal identifier to a species defined in the EnzymeMLDocument, given it is a
            rate equation.""",
        json_schema_extra=dict(),
    )

    variables: list[Variable] = element(
        default_factory=list,
        tag="variables",
        description="""List of variables that are part of the equation""",
        json_schema_extra=dict(),
    )

    def add_to_variables(
        self,
        id: str,
        name: str,
        symbol: str,
        **kwargs,
    ):
        params = {"id": id, "name": name, "symbol": symbol}

        self.variables.append(Variable(**params))

        return self.variables[-1]

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class Variable(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str = element(
        tag="id",
        description="""Unique identifier of the variable.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    name: str = element(
        tag="name", description="""Name of the variable.""", json_schema_extra=dict()
    )

    symbol: str = element(
        tag="symbol",
        description="""Symbol of the variable.""",
        json_schema_extra=dict(),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class Parameter(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str = element(
        tag="id",
        description="""Unique identifier of the parameter.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    name: str = element(
        tag="name", description="""Name of the parameter.""", json_schema_extra=dict()
    )

    symbol: str = element(
        tag="symbol",
        description="""Symbol of the parameter.""",
        json_schema_extra=dict(),
    )

    value: Optional[float] = element(
        default=None,
        tag="value",
        description="""Numerical value of the estimated parameter.""",
        json_schema_extra=dict(),
    )

    unit: Optional[UnitDefinition] = element(
        default=None,
        tag="unit",
        description="""Unit of the estimated parameter.""",
        json_schema_extra=dict(),
    )

    initial_value: Optional[float] = element(
        default=None,
        tag="initial_value",
        description="""Initial value that was used for the parameter estimation.""",
        json_schema_extra=dict(),
    )

    upper: Optional[float] = element(
        default=None,
        tag="upper",
        description="""Upper bound of the estimated parameter.""",
        json_schema_extra=dict(),
    )

    lower: Optional[float] = element(
        default=None,
        tag="lower",
        description="""Lower bound of the estimated parameter.""",
        json_schema_extra=dict(),
    )

    stderr: Optional[float] = element(
        default=None,
        tag="stderr",
        description="""Standard error of the estimated parameter.""",
        json_schema_extra=dict(),
    )

    constant: Optional[bool] = element(
        default=true,
        tag="constant",
        description="""Specifies if this parameter is constant""",
        json_schema_extra=dict(),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class Measurement(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str = element(
        tag="id",
        description="""Unique identifier of the measurement.""",
        json_schema_extra=dict(
            term="schema:identifier",
        ),
    )

    name: str = element(
        tag="name", description="""Name of the measurement""", json_schema_extra=dict()
    )

    species_data: list[MeasurementData] = element(
        default_factory=list,
        tag="species_data",
        description="""Measurement data of all species that were part of the measurement. A species can
            refer to a protein, complex, or small molecule.""",
        json_schema_extra=dict(),
    )

    group_id: Optional[str] = element(
        default=None,
        tag="group_id",
        description="""User-defined group ID to signal relationships between measurements.""",
        json_schema_extra=dict(),
    )

    ph: Optional[float] = element(
        default=None,
        tag="ph",
        description="""PH value of the measurement.""",
        json_schema_extra=dict(
            minimum="0",
            maximum="14",
        ),
    )

    temperature: Optional[float] = element(
        default=None,
        tag="temperature",
        description="""Temperature of the measurement.""",
        json_schema_extra=dict(),
    )

    temperature_unit: Optional[UnitDefinition] = element(
        default=None,
        tag="temperature_unit",
        description="""Unit of the temperature of the measurement.""",
        json_schema_extra=dict(),
    )

    def add_to_species_data(
        self,
        species_id: str,
        initial: float,
        data_unit: UnitDefinition,
        data_type: DataTypes,
        prepared: Optional[float] = None,
        data: list[float] = [],
        time: list[float] = [],
        time_unit: Optional[UnitDefinition] = None,
        is_simulated: bool = False,
        **kwargs,
    ):
        params = {
            "species_id": species_id,
            "initial": initial,
            "data_unit": data_unit,
            "data_type": data_type,
            "prepared": prepared,
            "data": data,
            "time": time,
            "time_unit": time_unit,
            "is_simulated": is_simulated,
        }

        self.species_data.append(MeasurementData(**params))

        return self.species_data[-1]

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class MeasurementData(
    BaseXmlModel,
    search_mode="unordered",
):
    species_id: str = element(
        tag="species_id",
        description="""The identifier for the described reactant.""",
        json_schema_extra=dict(),
    )

    initial: float = element(
        tag="initial",
        description="""Initial amount of the measurement data. This must be the same as the first data
            point in the array.""",
        json_schema_extra=dict(),
    )

    data_unit: UnitDefinition = element(
        tag="data_unit",
        description="""SI unit of the data that was measured.""",
        json_schema_extra=dict(),
    )

    data_type: DataTypes = element(
        tag="data_type",
        description="""Type of data that was measured (e.g. concentration)""",
        json_schema_extra=dict(),
    )

    prepared: Optional[float] = element(
        default=None,
        tag="prepared",
        description="""Amount of the reactant before the measurement. This field should be used for
            specifying the prepared amount of a species in the reaction mix. Not
            to be confused with , specifying the concentration at the first data
            point from the array.""",
        json_schema_extra=dict(),
    )

    data: list[float] = element(
        default_factory=list,
        tag="data",
        description="""Data that was measured.""",
        json_schema_extra=dict(),
    )

    time: list[float] = element(
        default_factory=list,
        tag="time",
        description="""Time steps of the replicate.""",
        json_schema_extra=dict(),
    )

    time_unit: Optional[UnitDefinition] = element(
        default=None,
        tag="time_unit",
        description="""Time unit of the replicate.""",
        json_schema_extra=dict(),
    )

    is_simulated: bool = element(
        tag="is_simulated",
        description="""Whether or not the data has been generated by simulation.""",
        json_schema_extra=dict(),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class UnitDefinition(
    BaseXmlModel,
    search_mode="unordered",
):
    id: Optional[str] = attr(
        default=None,
        tag="id",
        description="""Unique identifier of the unit definition.""",
        json_schema_extra=dict(),
    )

    name: Optional[str] = attr(
        default=None,
        tag="name",
        description="""Common name of the unit definition.""",
        json_schema_extra=dict(),
    )

    base_units: list[BaseUnit] = element(
        default_factory=list,
        tag="base_units",
        description="""Base units that define the unit.""",
        json_schema_extra=dict(),
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

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class BaseUnit(
    BaseXmlModel,
    search_mode="unordered",
):
    kind: UnitType = attr(
        tag="kind",
        description="""Kind of the base unit (e.g., meter, kilogram, second).""",
        json_schema_extra=dict(),
    )

    exponent: int = attr(
        tag="exponent",
        description="""Exponent of the base unit in the unit definition.""",
        json_schema_extra=dict(),
    )

    multiplier: Optional[float] = attr(
        default=None,
        tag="multiplier",
        description="""Multiplier of the base unit in the unit definition.""",
        json_schema_extra=dict(),
    )

    scale: Optional[float] = attr(
        default=None,
        tag="scale",
        description="""Scale of the base unit in the unit definition.""",
        json_schema_extra=dict(),
    )

    def xml(self, encoding: str = "unicode") -> str | bytes:
        """Converts the object to an XML string

        Args:
            encoding (str, optional): The encoding to use. If set to "bytes", will return a bytes string.
                                      Defaults to "unicode".
        """

        if encoding == "bytes":
            return self.to_xml()

        raw_xml = self.to_xml(encoding=None)
        parsed_xml = minidom.parseString(raw_xml)
        return parsed_xml.toprettyxml(indent="  ")


class EquationType(Enum):
    ASSIGNMENT = "assignment"
    INITIAL_ASSIGNMENT = "initialAssignment"
    ODE = "ode"
    RATE_LAW = "rateLaw"


class DataTypes(Enum):
    ABSORBANCE = "http://purl.allotrope.org/ontologies/quality#AFQ_0000061"
    CONCENTRATION = "http://purl.obolibrary.org/obo/PATO_0000033"
    CONVERSION = "http://purl.allotrope.org/ontologies/quality#AFQ_0000226"
    FLUORESCENCE = "http://purl.obolibrary.org/obo/PATO_0000018"
    PEAK_AREA = "http://purl.allotrope.org/ontologies/result#AFR_0001073"
    TRANSMITTANCE = "http://purl.allotrope.org/ontologies/result#AFR_0002261"


class UnitType(Enum):
    AMPERE = "ampere"
    AVOGADRO = "avogadro"
    BECQUEREL = "becquerel"
    CANDELA = "candela"
    CELSIUS = "celsius"
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
