from crr_labels import fantom
import pandas as pd
from pandas.testing import assert_frame_equal
import os
import pytest


def test_fantom_keep_inactives():
    enhancers, promoters = fantom("HelaS3", 200, drop_always_inactive_rows=False)
    os.makedirs("tests/test_fantom_keep_inactives", exist_ok=True)
    #enhancers.to_csv("tests/test_fantom_keep_inactives/enhancers.csv", index=False)
    #promoters.to_csv("tests/test_fantom_keep_inactives/promoters.csv", index=False)
    assert_frame_equal(enhancers, pd.read_csv("tests/test_fantom_keep_inactives/enhancers.csv"), check_dtype=False)
    assert_frame_equal(promoters, pd.read_csv("tests/test_fantom_keep_inactives/promoters.csv"), check_dtype=False)