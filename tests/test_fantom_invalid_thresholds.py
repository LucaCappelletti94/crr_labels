from crr_labels import fantom
import pytest


def test_fantom_invalid_enhancers_threshold():
    with pytest.raises(ValueError):
        fantom("unavailable_cell_line", 200, promoters_threshold=-1)
    with pytest.raises(ValueError):
        fantom("unavailable_cell_line", 200, enhancers_threshold=-1)