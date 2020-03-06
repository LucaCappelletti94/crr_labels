from crr_labels import roadmap
import pytest


def test_roadmap_state():
    with pytest.raises(ValueError):
        roadmap(["HelaS3", "GM12878"], 200, states=10)
        
def test_roadmap_cell_lines():
    with pytest.raises(ValueError):
        roadmap(["LOTR"], 200, states=15)