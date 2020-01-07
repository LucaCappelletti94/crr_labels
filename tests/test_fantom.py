from crr_labels import fantom
import pandas as pd
from dict_hash import sha256
from pandas.testing import assert_frame_equal
import os
from tqdm.auto import tqdm


def test_fantom():
    for window_size in tqdm((5, 200, 1000)):
        for cell_lines in tqdm(("HelaS3", ["HelaS3", "GM12878"])):
            for center_enhancers in tqdm(("peak", "center")):
                for drop_always_inactive_rows in tqdm((True, False)):
                    for binarize in tqdm((True, False)):
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
                                "{path}/enhancers.csv".format(path=path), index=False, sep="\t")
                            promoters.to_csv(
                                "{path}/promoters.csv".format(path=path), index=False, sep="\t")
                        assert_frame_equal(
                            enhancers,
                            pd.read_csv(
                                "{path}/enhancers.csv".format(path=path), sep="\t"),
                            check_dtype=False
                        )
                        assert_frame_equal(
                            promoters,
                            pd.read_csv(
                                "{path}/promoters.csv".format(path=path), sep="\t"),
                            check_dtype=False
                        )
