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
    download(info[genome]["promoters"], "fantom")
    promoters = pd.read_csv(
        "fantom/{filename}".format(
            filename=info[genome]["promoters"].split("/")[-1]
        ),
        compression="gzip",
        comment="#",
        sep="\t"
    ).drop(index=[0, 1])
    promoters.columns = [
        c.split(".")[2] if c.startswith("tpm") else c for c in promoters.columns
    ]
    promoters_info = pd.read_csv(
        "fantom/{filename}".format(
            filename=info[genome]["promoters_info"].split("/")[-1]
        ),
        compression="gzip",
        comment="#",
        sep="\t",
        header=None
    )
    promoters_info.columns = [
        "chromosome",
        "start",
        "end",
        "name",
        "score",
        "strand",
        "thickStart",
        "thickEnd",
        "itemRgb"
    ]
    mask = promoters.description.str.endswith("end")
    promoters = promoters[mask]
    promoters_info = promoters_info[mask]
    promoters["chromosome"] = promoters_info.chromosome
    promoters["start"] = promoters_info.start
    promoters["end"] = promoters_info.end
    for cell_line, group in cell_lines_names.groupby("cell_line"):
        promoters[cell_line] = promoters[group.code].astype(float).mean(skipna=True, axis=1)
    promoters = promoters.drop(columns=promoters.columns[promoters.columns.str.startswith("CNhs")])
    return promoters


def filter_enhancers(cell_lines_names: pd.DataFrame, genome: str, info: Dict, window_size:int, center_enhancer:str):
    download(info[genome]["enhancers"], "fantom")
    download(info[genome]["enhancers_info"], "fantom")
    enhancers = pd.read_csv(
        "fantom/{filename}".format(
            filename=info[genome]["enhancers"].split("/")[-1]
        ),
        compression="gzip",
        comment="#",
        sep="\t"
    ).drop(columns="Id")
    enhancers_info = pd.read_csv(
        "fantom/{filename}".format(
            filename=info[genome]["enhancers_info"].split("/")[-1]
        ),
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
