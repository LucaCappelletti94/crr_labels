from crr_labels import roadmap
import pytest


def test_roadmap_cell_lines():
    #with pytest.raises(ValueError):
    roadmap(["LOTR"], 200, states=15)