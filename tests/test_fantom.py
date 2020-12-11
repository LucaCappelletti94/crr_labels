from crr_labels import fantom
import pandas as pd
from dict_hash import sha256
from pandas.testing import assert_frame_equal
import os
from tqdm.auto import tqdm


def test_fantom():
    """Test execution of pipeline for FANTOM5."""
    for genome in tqdm(("hg19", "hg38"), desc="Genomes", leave=False):
        for center_enhancers in tqdm(("peak", "center"), leave=False, desc="Enhancer centering"):
            for binarize in tqdm((True, False), leave=False, desc="Binarization option"):
                window_size = 10
                for _ in fantom(
                    "HelaS3",
                    window_size,
                    root="fantom_test",
                    genome=genome,
                    center_enhancers=center_enhancers,
                    binarize=binarize,
                    nrows=100
                ):
                    pass
