"""Load bundled local datasets regardless of notebook working directory."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

_REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_OECD_OUTPUT_GAP_CSV = _REPO_ROOT / "Graficos" / "OECDevolucion.csv"


def load_oecd_output_gap(csv_path: str | Path | None = None) -> pd.DataFrame:
    """Return OECD output-gap series with a parsed annual ``Date`` column."""
    path = Path(csv_path) if csv_path is not None else DEFAULT_OECD_OUTPUT_GAP_CSV
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], format="%Y")
    return df.sort_values("Date")
