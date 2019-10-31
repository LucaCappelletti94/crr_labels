from crr_labels import fantom, roadmap
import pytest

def test_fantom_unavailable_genome():
    with pytest.raises(ValueError):
        fantom(
            ["HelaS3", "GM12878"],
            window_size=200,
            genome="invalid_genome"
        )
    with pytest.raises(ValueError):
        roadmap(
            ["HelaS3", "GM12878"],
            window_size=200,
            genome="invalid_genome"
        )