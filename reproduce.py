"""Reproduce the paper figures, disclosure scores, and Partial-weight sensitivity."""

from pathlib import Path
import json
import os
import runpy

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent
FIELDS = [
    "DC-only MWh",
    "Spatially attributable electricity",
    "Hourly CFE",
    "Boundary",
    "Renewable accounting transparency",
]


def main():
    os.chdir(ROOT)
    output = ROOT / "plots"
    output.mkdir(exist_ok=True)
    data = pd.read_csv(ROOT / "data" / "disclosure_coding.csv")
    coding = data.set_index("Company")[FIELDS]
    if coding.isna().any().any():
        raise ValueError("Missing index classifications in the input table")
    unknown = set(coding.to_numpy().ravel()) - {"Yes", "Partial", "No"}
    if unknown:
        raise ValueError(f"Unrecognized classifications: {unknown}")

    scores = coding.map({"Yes": 1, "Partial": 0.5, "No": 0}.get).sum(axis=1)
    scores.rename("Score_out_of_5").to_csv(output / "transparency_scores.csv")
    sensitivity = pd.DataFrame({
        weight: coding.map({"Yes": 1, "Partial": weight, "No": 0}.get).sum(axis=1)
        for weight in [0, 0.25, 0.5, 0.75, 1]
    }).T
    sensitivity.index.name = "Partial_weight"
    sensitivity.to_csv(output / "partial_weight_sensitivity.csv")
    print(scores.to_string())

    runpy.run_path(str(ROOT / "code" / "build_pipeline_diagram.py"), run_name="__main__")
    plt.close("all")
    for name in [
        "disclosure_matrix_nature_style.ipynb",
        "disclosure_gap_matrix.ipynb",
        "granularity_plot.ipynb",
    ]:
        notebook = json.loads((ROOT / "code" / name).read_text(encoding="utf-8"))
        namespace = {"__name__": "__main__"}
        for index, cell in enumerate(notebook["cells"]):
            if cell["cell_type"] == "code":
                exec(compile("".join(cell["source"]), f"{name}:cell{index}", "exec"), namespace)
        plt.close("all")
    print(f"Outputs saved to {output}")


if __name__ == "__main__":
    main()
