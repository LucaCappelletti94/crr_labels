from crr_labels import crr_labels
import pytest

def test_crr_labels():
    with pytest.raises(ValueError):
        crr_labels(["HelaS3"], "hg19", 200, "unknown")
    with pytest.raises(ValueError):
        crr_labels(["HelaS3"], "hg19", 0, "unknown")
    crr_labels(["HelaS3"], "hg19", 200, "peak")
    crr_labels(["HelaS3"], "hg19", 200, "center")