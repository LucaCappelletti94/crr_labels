from typing import List
import pandas as pd


def normalize_bed_file(cell_lines: List[str], bed_file: pd.DataFrame) -> pd.DataFrame:
    """Return normalized bed file.

    Parameters
    ---------------------------
    cell_lines:List[str],
        The cell lines to be maintained in the bed file.
    bed_file:pd.DataFrame,
        The bed file to normalized.

    Returns
    ----------------------------
    The normalized bed file.
    """
    if "strand" not in bed_file:
        bed_file["strand"] = "."
    return bed_file[["chromosome", "start", "end", "strand", *sorted(cell_lines)]]