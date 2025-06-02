import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter


time_formatter = FuncFormatter(
    lambda x, _: f"{int(x // 60**2):02d}:{int((x % 60**2) // 60):02d}"
)
volt_formatter = FuncFormatter(lambda x, _: f"{x:.2f} V")
amp_formatter = FuncFormatter(lambda x, _: f"{x:.2f} A")
amp_hour_formatter = FuncFormatter(lambda x, _: f"{x:.2f} Ah")


def plot_current_voltage(
    df: pd.DataFrame,
    **kwargs,
) -> Figure:
    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    ax.plot(df["Total Time"], df["Current"], label="Current", **kwargs)
    ax2.plot(df["Total Time"], df["Voltage"], color="r", label="Voltage", **kwargs)

    ax2.set_ylabel("Voltage")
    ax.set_ylabel("Current")
    ax.set_xlabel("Time (hh:mm)")

    ax.xaxis.set_major_formatter(time_formatter)
    ax.yaxis.set_major_formatter(amp_formatter)
    ax2.yaxis.set_major_formatter(volt_formatter)

    ax2_ymin, ax2_ymax = ax2.get_ylim()
    ax2.set_ylim(min(10.5, ax2_ymin), max(14.5, ax2_ymax))
    ax1_ymin, ax1_ymax = ax.get_ylim()
    ax.set_ylim(min(0, ax1_ymin), max(0, ax1_ymax))

    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2)

    return fig
