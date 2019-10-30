from crr_labels import fantom
import pandas as pd
import os
import pytest


def test_fantom_center():
    enhancers, promoters = fantom(["HelaS3", "GM12878"], 200, center_enhancers="center")
    os.makedirs("tests/test_fantom_center", exist_ok=True)
    enhancers.to_csv("tests/test_fantom_center/enhancers.csv", index=False)
    promoters.to_csv("tests/test_fantom_center/promoters.csv", index=False)
    assert enhancers.equals(pd.read_csv("tests/test_fantom_center/enhancers.csv"))
    assert promoters.equals(pd.read_csv("tests/test_fantom_center/promoters.csv"))