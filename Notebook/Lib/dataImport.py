import pandas as pd


def read_lcv_file(file: str) -> pd.DataFrame:
    """
    Read a single LCV file and return the DataFrame.
    """

    with open(file, "r") as f:
        lines = f.readlines()
        header_row = next(i for i, line in enumerate(lines) if line.strip() == "") + 1

    df = pd.read_csv(
        file,
        skiprows=header_row - 1,
        skipfooter=1,
        usecols=[
            "Total Time",
            "Cycle",
            "Loop Counter #1",
            "Loop Counter #2",
            "Loop Counter #3",
            "Step",
            "Step time",
            "Current",
            "Voltage",
            "Power",
            "Amp-Hours",
            "Mode",
            "Data Acquisition Flag",
        ],
        dtype={
            "Total Time": float,
            "Cycle": int,
            "Loop Counter #1": int,
            "Loop Counter #2": int,
            "Loop Counter #3": int,
            "Step": int,
            "Step time": float,
            "Current": float,
            "Voltage": float,
            "Power": float,
            "Amp-Hours": float,
            "Mode": str,
            "Data Acquisition Flag": object,
        },
        engine="python",
    )

    df.attrs["test"] = file.split("/")[-1].split(".")[0]
    df.attrs["battery"] = file.split("/")[-1].split("-")[2]
    df.attrs["stage"] = file.split("/")[-1].split(".")[0].split("-")[3]

    return df
