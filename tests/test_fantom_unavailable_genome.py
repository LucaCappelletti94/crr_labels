from crr_labels import fantom
import pytest

def test_fantom_unavailable_genome():
    with pytest.raises(ValueError):
        fantom(
            "HelaS3",
            window_size=200,
            genome="invalid_genome"
        )