import pandas as pd


def read_lcv_file(
    file: str,
    dodAttributes: bool = False,
) -> pd.DataFrame:
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
            "Watt-Hours",
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
            "Watt-Hours": float,
            "Mode": str,
            "Data Acquisition Flag": object,
        },
        engine="python",
    )

    # Identifying Attributes
    df.attrs["test"] = file.split("/")[-1].split(".")[0]
    df.attrs["battery"] = file.split("/")[-1].split("-")[2]
    df.attrs["stage"] = file.split("/")[-1].split(".")[0].split("-")[3]

    # Depth of Discharge Attributes
    if dodAttributes:
        calculate_dod_attributes(df)

    return df


def calculate_dod_attributes(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Calculate test attributes for the DataFrame.
    """
    df.attrs["dodAmpHours"] = -df["Amp-Hours"].min()
    df.attrs["dodWattHours"] = -df["Watt-Hours"].min()

    df.attrs["dorAmpHoursPre"] = df[df["Loop Counter #1"] == 1]["Amp-Hours"].max()
    df.attrs["dorAmpHoursPst"] = df[df["Loop Counter #1"] == 2]["Amp-Hours"].max()
    df.attrs["dorWattHoursPre"] = df[df["Loop Counter #1"] == 1]["Watt-Hours"].max()
    df.attrs["dorWattHoursPst"] = df[df["Loop Counter #1"] == 2]["Watt-Hours"].max()

    return df
