from crr_labels import roadmap
import pandas as pd
from dict_hash import sha256
from pandas.testing import assert_frame_equal
import os
from tqdm.auto import tqdm


def test_roadmap():
    window_size = 10
    for genome in ("hg19", "hg38"):
        for states in tqdm((15, 18), leave=False, desc="States"):
            _ = roadmap(
                ["HelaS3", "GM12878"],
                window_size,
                genome=genome,
                states=states,
                nrows=100
            )