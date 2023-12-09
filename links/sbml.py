from typing import Dict
from sdRDM import Linker


def link(
    dataset: "DataModel",  # type: ignore
    template: Dict,
):
    """
    Links the dataset to an SBML document based on the provided mapping template.

    Args:
        dataset: The dataset to be linked.
        template: The mapping template specifying the link between the dataset and SBML.

    Raises:
        AssertionError: If the mapping template does not specify a 'SBML' source.

    Returns:
        None
    """

    linker = Linker(template)

    assert (
        "SBML" in linker.__sources__
    ), "Not able to link to SBML. Please specify a 'SBML' source in the mapping template."

    sbmldoc = linker.__sources__["SBML"]()
    linker(dataset, sbmldoc)

    for vessel in dataset.vessels:
        linker(vessel, sbmldoc.model)

    for protein in dataset.proteins:
        linker(protein, sbmldoc.model)

    for reactant in dataset.reactants:
        linker(reactant, sbmldoc.model)

    for reaction in dataset.reactions:
        mapped = linker(reaction, sbmldoc.model)

        for educt in reaction.educts:
            linker(educt, mapped.reactions)

        for product in reaction.products:
            linker(product, mapped.reactions)

        for modifier in reaction.modifiers:
            linker(modifier, mapped.reactions)

    return sbmldoc
