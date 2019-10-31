from crr_labels import fantom, roadmap
import pytest


def test_invalid_window_size():
    with pytest.raises(ValueError):
        fantom(["HelaS3", "GM12878"], 0)
    with pytest.raises(ValueError):
        fantom(["HelaS3", "GM12878"], -1)
    with pytest.raises(ValueError):
        roadmap(["HelaS3", "GM12878"], 0)
    with pytest.raises(ValueError):
        roadmap(["HelaS3", "GM12878"], -1)