import pathlib

from honeybee_ies.writer import model_to_ies as hb_model_to_ies
from dragonfly.model import Model


def model_to_ies(
        model: Model, folder: str = '.', name: str = None) -> pathlib.Path:
    """Export a dragonfly model to an IES GEM file.

    Args:
        model: A dragonfly model.
        folder: Path to target folder to export the file. Default is current folder.
        name: An optional name for exported file. By default the name of the model will
            be used.

    Returns:
        Path to exported GEM file.
    """
    hb_models = model.to_honeybee(
        object_per_model='District', use_multiplier=False,
        solve_ceiling_adjacencies=False
    )
    return hb_model_to_ies(hb_models[0], folder, name)
