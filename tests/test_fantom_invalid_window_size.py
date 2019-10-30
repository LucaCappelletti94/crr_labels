from crr_labels import fantom
import pytest


def test_fantom_invalid_window_size():
    with pytest.raises(ValueError):
        fantom("unavailable_cell_line", 0)
    with pytest.raises(ValueError):
        fantom("unavailable_cell_line", -1)