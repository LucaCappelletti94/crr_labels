from typing import List
from .fantom import fantom


def crr_labels(cell_lines: List["str"], genome: str, window_size: int, center_enhancer: str = "peak"):
    """Renders cis-Regulatory regions datasets for each given cell line.
        cell_lines: List["str"], list of cell lines to extract.
        genome: str, genome to use for the datasets.
        window_size: int, window size to use for the various regions.
        center_enhancer: str, how to center the enhancer window, either around "peak" or the "center" of the region.
    """
    if window_size <= 0:
        raise ValueError("Window size must be a strictly positive integer.")
    if center_enhancer not in ["peak", "center"]:
        raise ValueError("The given center_enhancer option {center_enhancer} is not supported.".format(
            center_enhancer=center_enhancer
        ))
    fantom(cell_lines, genome, window_size, center_enhancer)
    #roadmap(cell_lines, only_primary_colture)
    #merge(cell_lines, only_primary_colture)
