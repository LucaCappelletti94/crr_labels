from crr_labels import fantom
import pandas as pd
import os
import pytest


def test_fantom_peak():
    enhancers, promoters = fantom(["HelaS3", "GM12878"], 200, center_enhancers="peak")
    # os.makedirs("tests/test_fantom_peak", exist_ok=True)
    # enhancers.to_csv("tests/test_fantom_peak/enhancers.csv", index=False)
    # promoters.to_csv("tests/test_fantom_peak/promoters.csv", index=False)
    assert enhancers.equals(pd.read_csv("tests/test_fantom_peak/enhancers.csv"))
    assert promoters.equals(pd.read_csv("tests/test_fantom_peak/promoters.csv"))