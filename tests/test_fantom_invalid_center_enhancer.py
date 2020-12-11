from crr_labels import fantom
import pytest


def test_fantom_invalid_center_enhancer():
    with pytest.raises(ValueError):
        next(fantom("HelaS3", 200, center_enhancers="invalid_mode"))