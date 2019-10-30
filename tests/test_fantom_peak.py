from crr_labels import fantom
import pandas as pd
from pandas.testing import assert_frame_equal
import os


def test_fantom_peak():
    enhancers, promoters = fantom(["HelaS3", "GM12878"], 200, center_enhancers="peak", nrows=500)
    os.makedirs("tests/test_fantom_peak", exist_ok=True)
    #enhancers.to_csv("tests/test_fantom_peak/enhancers.csv", index=False)
    #promoters.to_csv("tests/test_fantom_peak/promoters.csv", index=False)
    assert_frame_equal(enhancers, pd.read_csv("tests/test_fantom_peak/enhancers.csv"), check_dtype=False)
    assert_frame_equal(promoters, pd.read_csv("tests/test_fantom_peak/promoters.csv"), check_dtype=False)