from crr_labels import roadmap, fantom
import pytest


def test_invalid_nros():
    with pytest.raises(ValueError):
        fantom(["HelaS3", "GM12878"], 200, nrows=-1)
    with pytest.raises(ValueError):
        roadmap(["HelaS3", "GM12878"], 200, nrows=0)