from crr_labels import fantom
import pandas as pd
import os
import pytest


def test_fantom_keep_inactives():
    enhancers, promoters = fantom("HelaS3", 200, drop_always_inactive_rows=False)
    os.makedirs("tests/test_fantom_keep_inactives", exist_ok=True)
    enhancers.to_csv("tests/test_fantom_keep_inactives/enhancers.csv", index=False)
    promoters.to_csv("tests/test_fantom_keep_inactives/promoters.csv", index=False)
    assert enhancers.equals(pd.read_csv("tests/test_fantom_keep_inactives/enhancers.csv"))
    assert promoters.equals(pd.read_csv("tests/test_fantom_keep_inactives/promoters.csv"))