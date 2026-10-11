"""Market data helpers shared by thesis notebooks."""

from __future__ import annotations

import pandas as pd
import yfinance as yf


def obtener_precios_activos(activos, inicio_periodo, fin_periodo) -> pd.DataFrame:
    """Download adjusted (or close) daily prices for each ticker in ``activos``."""
    marco_precios = pd.DataFrame()
    for activo in activos:
        datos_crudos = yf.download(
            activo, start=inicio_periodo, end=fin_periodo, auto_adjust=False
        )
        if isinstance(datos_crudos, pd.Series):
            serie_precios = datos_crudos
        elif "Adj Close" in datos_crudos.columns:
            serie_precios = datos_crudos["Adj Close"]
        elif "Close" in datos_crudos.columns:
            serie_precios = datos_crudos["Close"]
        else:
            serie_precios = datos_crudos.iloc[:, 0]
        marco_precios[activo] = serie_precios
    return marco_precios
