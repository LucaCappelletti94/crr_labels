from crr_labels import roadmap
import pandas as pd
from dict_hash import sha256
from pandas.testing import assert_frame_equal
import os
from tqdm.auto import tqdm


def test_roadmap():
    for window_size in tqdm((5, 200, 1000)):
        for states in tqdm((15, 18)):
            enhancers, promoters = roadmap(
                ["HelaS3", "GM12878"],
                window_size,
                states=states
            )
            path = "tests/test_data/roadmap/{key}".format(
                key=sha256({
                    "window_size": window_size,
                    "states": states
                })
            )
            if not os.path.exists(path):
                os.makedirs(path)
                enhancers.to_csv("{path}/enhancers.csv".format(path=path), index=False)
                promoters.to_csv("{path}/promoters.csv".format(path=path), index=False)
            assert_frame_equal(
                enhancers,
                pd.read_csv("{path}/enhancers.csv".format(path=path)),
                check_dtype=False
            )
            assert_frame_equal(
                promoters,
                pd.read_csv("{path}/promoters.csv".format(path=path)),
                check_dtype=False
            )