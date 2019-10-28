from .utils import download, load_info
from typing import List, Dict
import pandas as pd


def filter_cell_lines(cell_lines: List[str], genome: str, info: Dict):
    download(info[genome]["cell_lines"], "fantom")
    df = pd.read_csv("fantom/{filename}".format(
        filename=info[genome]["cell_lines"].split("/")[-1]
    ), sep="\t", header=None)
    cell_lines_names = df[0].str.split("cell line:", expand=True)
    df = pd.concat([
        cell_lines_names[pd.notnull(cell_lines_names[1])],
        df[pd.notnull(cell_lines_names[1])][1],
    ], axis=1)
    df.columns = ["tissue", "cell_line", "code"]
    df.cell_line = df.cell_line.apply(lambda x: x.split("ENCODE")[0].strip())
    return df[df.cell_line.isin(cell_lines)]


def filter_promoters(cell_lines_names: pd.DataFrame, genome: str, info: Dict):
    download(info[genome]["promoters"], "fantom")
    df = pd.read_csv(
        "fantom/{filename}".format(
            filename=info[genome]["promoters"].split("/")[-1]
        ),
        compression="gzip",
        comment="#",
        sep="\t"
    )
    df.columns = [
        c.split(".")[2] if c.startswith("tpm") else c for c in df.columns
    ]

    df = df.drop(index=[0, 1])
    df = df[df.description.str.endswith("end")]
    annotations = df["00Annotation"].str.split(":", expand=True)
    regions = annotations[1].str.split(",", expand=True)
    annotations = pd.concat([
        annotations[0],
        regions[0].str.split(r"\.\.", expand=True),
        regions[1]
    ], axis=1)
    annotations.columns = ["chromosome", "start", "end", "strand"]
    df = pd.concat([
        annotations,
        df.drop(columns=[
            "00Annotation",
        ])
    ], axis=1)
    for cell_line, group in cell_lines_names.groupby("cell_line"):
        df[cell_line] = df[group.code].astype(float).mean(skipna=True, axis=1)
    df = df.drop(columns=df.columns[df.columns.str.startswith("CNhs")])
    return df


def filter_enhancers(cell_lines_names: pd.DataFrame, genome: str, info: Dict, window_size:int, center_enhancer:str):
    download(info[genome]["enhancers"], "fantom")
    download(info[genome]["enhancers_info"], "fantom")
    enhancers = pd.read_csv(
        "fantom/human_permissive_enhancers_phase_1_and_2_expression_tpm_matrix.txt.gz",
        compression="gzip",
        comment="#",
        sep="\t"
    ).drop(columns="Id")
    enhancers_info = pd.read_csv(
        "fantom/human_permissive_enhancers_phase_1_and_2.bed.gz",
        compression="gzip",
        comment="#",
        sep="\t",
        header=None
    )
    enhancers_info.columns = [
        "chromosome",
        "start",
        "end",
        "name",
        "score",
        "strand",
        "thickStart",
        "thickEnd",
        "itemRgb",
        "blockCount",
        "blockSizes",
        "blockStarts"
    ]
    enhancers["chromosome"] = enhancers_info.chromosome
    if center_enhancer=="peak":
        center = enhancers_info.thickStart
    elif center_enhancer=="center":
        center = (enhancers_info.start + (enhancers_info.end - enhancers_info.start)/2).astype(int)
    enhancers["start"] = (center - window_size/2).astype(int)
    enhancers["end"] = (center + window_size/2).astype(int)
    for cell_line, group in cell_lines_names.groupby("cell_line"):
        enhancers[cell_line] = enhancers[group.code].astype(
            float).mean(skipna=True, axis=1)
    enhancers = enhancers.drop(
        columns=enhancers.columns[enhancers.columns.str.startswith("CNhs")])
    return enhancers


def fantom(cell_lines: List[str], genome: str, window_size: int, center_enhancer: str):
    info = load_info("fantom")
    if genome not in info:
        raise ValueError("Given genome {genome} is not currently supported.".format(
            genome=genome
        ))

    cell_lines_names = filter_cell_lines(cell_lines, genome, info)
    #filter_promoters(cell_lines_names, genome, info).to_csv("promoters.csv.gz", compression="gzip", index=False)
    filter_enhancers(cell_lines_names, genome, info, window_size, center_enhancer).to_csv(
        "enhancers.csv.gz",
        compression="gzip",
        index=False
    )
