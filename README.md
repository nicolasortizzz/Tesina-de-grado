# Tesina de grado — Investment analysis notebooks

*Repositorio de código y notebooks para evaluar en la práctica los marcos analíticos desarrollados en el trabajo de grado.*

This repository accompanies an undergraduate thesis on practical equity and macro analysis. It contains Jupyter notebooks that pull market data, build comparison tables, optimize portfolios with Markowitz-style Monte Carlo simulation, and visualize business-cycle (RCBC) indicators and sector-rotation frameworks.

## Purpose

The project connects three lines of work:

1. **Fundamental screening** — Compare many S&P 500–related tickers on valuation, profitability, capital cost, dividends, and correlation with the index.
2. **Portfolio optimization** — Estimate efficient combinations of selected stocks from historical returns using random long-only weights and the Sharpe ratio.
3. **Business cycle (RCBC)** — Relate inflation and growth proxies (U.S. CPI from BLS, OECD output gap) to a four-phase cycle framework and sector rotation charts used in the thesis.

## Repository structure

| Path | Description |
|------|-------------|
| `AnalisisFundamental.ipynb` | Yahoo Finance helpers, WACC/ROIC, dividend and S&P 500 correlation metrics, comparison table, optional `ipywidgets` dashboard |
| `MarkowitzPortafolio.ipynb` | Historical prices via `yfinance`, daily returns, 100,000-weight Monte Carlo simulation, efficient-frontier scatter plot |
| `RCBC.ipynb` | Notes and charts for cycle indicators; plots OECD output gap from local CSV |
| `Graficos/graficos.ipynb` | Thesis figures: RCBC quadrant map, Markowitz risk–return sketch, sector-pair tables by phase |
| `Graficos/OECDevolucion.csv` | Annual OECD output-gap series (column `Value`, years in `Date`) |
| `portfolio_data.py` | Shared `obtener_precios_activos()` helper used by `MarkowitzPortafolio.ipynb` |
| `tesina_data.py` | `load_oecd_output_gap()` loader (repo-relative path to `Graficos/OECDevolucion.csv`) |
| `scripts/validate_notebooks.py` | JSON + `nbformat` validation for all notebooks |

Static image `Graficos/MarkImage.png` is referenced in `MarkowitzPortafolio.ipynb` but is not included in this repository; the notebook still contains an executed efficient-frontier plot in its outputs.

## Data sources

| Source | Used in | Notes |
|--------|---------|--------|
| [Yahoo Finance](https://finance.yahoo.com/) (`yfinance`) | `AnalisisFundamental.ipynb`, `MarkowitzPortafolio.ipynb` | Prices, `info`, financials, dividends; risk-free proxy `^TNX` for WACC |
| S&P 500 (`^GSPC`) | `AnalisisFundamental.ipynb` | Daily returns from 2010 for correlation with each ticker |
| [U.S. BLS CPI charts](https://www.bls.gov/charts/consumer-price-index/consumer-price-index-by-category-line-chart.htm) | `RCBC.ipynb` | Linked for year-on-year U.S. inflation context (figure in notebook markdown/output) |
| OECD output gap | `RCBC.ipynb`, `Graficos/OECDevolucion.csv` | Exported series plotted as “Evolución del Output Gap OECD” |
| Hard-coded sector tables | `Graficos/graficos.ipynb` | Pairwise percentages (e.g. 99.8% oil & gas vs. discretionary in stagflation) transcribed from thesis figures |

Re-running notebooks refreshes Yahoo data; saved outputs reflect the environment where the notebooks were last executed.

## Methodology (by notebook)

### Fundamental analysis (`AnalisisFundamental.ipynb`)

- Normalizes numeric fields and computes **WACC** (CAPM cost of equity with market risk premium 5.5%, cost of debt and tax rate from statements, fallbacks when data is missing) and **ROIC** from Yahoo financials.
- Builds a panel per ticker: market cap, P/E, EPS growth, leverage, ROE, dividend yield, book value, P/B, dividend rate/shield/5y growth, **correlation with S&P 500** since 2010, internal WACC/ROIC, and **Roic/WACC** (winsorized and median-imputed).
- Default run uses a configurable list of tickers (e.g. large caps and selected names across sectors); results can be sorted and filtered in an interactive widget table when run locally with Jupyter/VS Code.

### Markowitz + Monte Carlo (`MarkowitzPortafolio.ipynb`)

- Assets (example run): `GOOGL`, `ASML`, `MOH`, `ORLA`, `NVDA`, `META`, `PG`, `PDD`.
- Window: **2019-01-01** to **2025-01-01**; **adjusted close** prices; **daily** simple returns.
- **100,000** random long-only weight vectors (normalized to sum to 1); annualized mean return and volatility (×252); Sharpe with **risk-free rate 4%**.
- Selects the portfolio with maximum Sharpe and plots all draws colored by Sharpe (efficient frontier cloud).

### RCBC (`RCBC.ipynb`)

- Documents use of U.S. inflation (BLS) and OECD **output gap** for growth.
- Code loads `Graficos/OECDevolucion.csv` and plots the gap over time (1985–2026 in the bundled file).

### Figures (`Graficos/graficos.ipynb`)

- Four-quadrant **estanflación / recalentamiento / reflación / recuperación** diagram with clockwise cycle arrows and sector lists per phase.
- Stylized **σ_P vs μ_P** points for portfolio theory exposition.
- Matplotlib tables of high co-movement sector pairs within each phase (values stored as strings in code, e.g. “99.8%”).

## Key results shown in saved notebook outputs

Values below come from **executed cells** in the committed notebooks (historical sample and dates as coded). They will change if you re-run with newer data or parameters.

### Maximum-Sharpe portfolio (`MarkowitzPortafolio.ipynb`)

For the eight-ticker universe and 2019–2025 window, the stored simulation reports:

| Metric | Value |
|--------|------:|
| Expected return (annualized) | 53.23% |
| Volatility (annualized) | 32.67% |
| Sharpe ratio | 1.51 |

**Optimal weights (long-only):** NVDA 43.54%, ORLA 22.05%, PG 15.06%, PDD 9.07%, MOH 5.00%, META 3.17%, GOOGL 1.87%, ASML 0.24%.

The notebook includes a risk–return scatter of all simulated portfolios with Sharpe on the color scale.

### OECD output gap (`RCBC.ipynb` + `OECDevolucion.csv`)

The bundled series includes pronounced negative gaps in **2009** (≈ −4.02) and **2020** (≈ −4.13). Recent annual values in the CSV include **2024** ≈ 0.12, **2025** ≈ −0.44, **2026** ≈ −0.83 (units as provided in the OECD extract).

### Fundamental panel (`AnalisisFundamental.ipynb`)

The saved static table shows **50 rows** (tickers such as UNH, MSFT, NVDA, AMZN, etc.) with Yahoo-derived fields and computed WACC, ROIC, and Roic/WACC. Example stored figures: NVDA trailing P/E ≈ 43.3 and market cap ≈ 4.26×10¹² USD; MSFT market cap ≈ 3.56×10¹² USD; many rows include dividend and correlation columns as defined in the notebook.

### Sector rotation tables (`Graficos/graficos.ipynb`)

Figures list sector pairs with high stated co-movement within each RCBC phase—for example, under **estanflación**, oil & gas vs. consumer discretionary at **99.8%** in the embedded table data (see notebook cells for full matrices).

## Requirements

- Python **3.10+** recommended  
- Jupyter Lab or Notebook, or VS Code with Jupyter support (recommended for the fundamental **dashboard** in `AnalisisFundamental.ipynb`)

Install dependencies:

```bash
pip install -r requirements.txt
```

Validate notebook files (without re-executing):

```bash
python scripts/validate_notebooks.py
```

## How to run

From the repository root:

```bash
jupyter lab
# or
jupyter notebook
```

Open notebooks in this order if you are exploring the thesis flow:

1. `Graficos/graficos.ipynb` — static/thesis figures (no network required except optional font lookup).
2. `RCBC.ipynb` — requires `Graficos/OECDevolucion.csv` on the relative path used in the notebook.
3. `MarkowitzPortafolio.ipynb` — needs internet for `yfinance` downloads; Monte Carlo with 100k iterations may take a minute.
4. `AnalisisFundamental.ipynb` — needs internet; run all cells before the dashboard cell; use a local Jupyter kernel for `ipywidgets`.

**Paths:** `RCBC.ipynb` and `tesina_data.load_oecd_output_gap()` resolve `Graficos/OECDevolucion.csv` from the repository root via `tesina_data.py`. Run `MarkowitzPortafolio.ipynb` from the repo root so `from portfolio_data import …` works. Each notebook includes markdown sections (intro, data, methodology, analysis, conclusions) for easier navigation on GitHub.

## Limitations

- Models use **historical** returns and statements; results are illustrative, not investment advice.
- WACC/ROIC depend on Yahoo data quality and stated fallbacks (e.g. default risk-free rate 4% if `^TNX` fails).
- Markowitz simulation uses **long-only** weights and past covariance; no transaction costs or constraints beyond normalization.
- RCBC notebook does not auto-classify the current cycle—it provides indicators and visuals for interpretation.

## License

No license file is included; treat as academic project code unless otherwise specified by the author.
