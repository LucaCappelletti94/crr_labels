from crr_labels import fantom
import pandas as pd
from dict_hash import sha256
from pandas.testing import assert_frame_equal
import os
from tqdm.auto import tqdm


def test_fantom():
    for window_size in tqdm((5, 200, 1000), desc="Window sizes", leave=False):
        for cell_lines in tqdm(("HelaS3", ["HelaS3", "GM12878"]), leave=False, desc="Cell lines"):
            for center_enhancers in tqdm(("peak", "center"), leave=False, desc="Enhancer centering"):
                for drop_always_inactive_rows in tqdm((True, False), leave=False, desc="Dropping inactive"):
                    for binarize in tqdm((True, False), leave=False, desc="Binarization option"):
                        enhancers, promoters = fantom(
                            cell_lines,
                            window_size,
                            center_enhancers=center_enhancers,
                            drop_always_inactive_rows=drop_always_inactive_rows,
                            binarize=binarize,
                            nrows=300
                        )
                        path = "tests/test_data/fantom/{key}".format(
                            key=sha256({
                                "cell_lines": cell_lines,
                                "window_size": window_size,
                                "center_enhancers": center_enhancers,
                                "drop_always_inactive_rows": drop_always_inactive_rows,
                                "binarize": binarize
                            })
                        )
                        if not os.path.exists(path):
                            os.makedirs(path)
                            enhancers.to_csv(
                                "{path}/enhancers.csv.gz".format(path=path), index=False, sep="\t")
                            promoters.to_csv(
                                "{path}/promoters.csv.gz".format(path=path), index=False, sep="\t")
                        assert (enhancers.chromEnd - enhancers.chromStart == window_size).all()
                        assert_frame_equal(
                            enhancers,
                            pd.read_csv(
                                "{path}/enhancers.csv.gz".format(path=path), sep="\t"),
                            check_dtype=False
                        )
                        assert (promoters.chromEnd - promoters.chromStart == window_size).all()
                        assert_frame_equal(
                            promoters,
                            pd.read_csv(
                                "{path}/promoters.csv.gz".format(path=path), sep="\t"),
                            check_dtype=False
                        )
