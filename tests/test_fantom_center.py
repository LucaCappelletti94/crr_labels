from crr_labels import fantom
import pandas as pd
import numpy as np
import os
from pandas.testing import assert_frame_equal



def test_fantom_center():
    enhancers, promoters = fantom(["HelaS3", "GM12878"], 200, center_enhancers="center", nrows=500)
    os.makedirs("tests/test_fantom_center", exist_ok=True)
    #enhancers.to_csv("tests/test_fantom_center/enhancers.csv", index=False)
    #promoters.to_csv("tests/test_fantom_center/promoters.csv", index=False)
    assert_frame_equal(enhancers, pd.read_csv("tests/test_fantom_center/enhancers.csv"), check_dtype=False)
    assert_frame_equal(promoters, pd.read_csv("tests/test_fantom_center/promoters.csv"), check_dtype=False)