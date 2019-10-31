from crr_labels import fantom, roadmap
import pytest


def test_fantom_unavailable_cell_line():
    with pytest.raises(ValueError):
        fantom("unavailable_cell_line", 200)
    with pytest.raises(ValueError):
        roadmap("unavailable_cell_line", 200)
