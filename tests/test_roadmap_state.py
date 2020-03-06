from crr_labels import roadmap
import pytest


def test_roadmap_state():
    with pytest.raises(ValueError):
        roadmap(["HelaS3", "GM12878"], 200, states=10)