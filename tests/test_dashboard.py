import importlib
from unittest.mock import patch

import pandas as pd


def test_main_importa_como_pacote():
    # Antes: ImportError (import relativo além do pacote) / ModuleNotFoundError
    mod = importlib.import_module("src.main")
    assert callable(mod.main)


def test_dashboard_monta_layout_e_metodo_run():
    from src.dashboard.ibovespa_dashboard import IbovespaDashboard

    dash_app = IbovespaDashboard()
    assert dash_app.app.layout is not None
    # Dash 3 removeu run_server; o método run precisa usar app.run
    with patch.object(dash_app.app, "run") as run:
        dash_app.run(debug=False)
        run.assert_called_once_with(debug=False)


def test_estatisticas_e_cache():
    from datetime import timedelta

    from src.utils.cache import Cache
    from src.utils.data_processor import calculate_statistics

    df = pd.DataFrame({"index_value": [100.0, 110.0], "variation": [0.5, -1.0], "volume": [1, 2]})
    stats = calculate_statistics(df)
    assert stats == {"daily_change": -1.0, "avg_value": 105.0, "min_value": 100.0, "max_value": 110.0}
    assert calculate_statistics(pd.DataFrame())["avg_value"] == 0
    c = Cache(timedelta(minutes=5))
    c.set("k", 1)
    assert c.get("k") == 1
    assert Cache(timedelta(seconds=0)).get("x") is None


def test_transformador_ibovespa():
    from src.transform.ibovespa_transformer import IbovespaTransformer

    df = IbovespaTransformer().transform_market_data({"value": 120000, "variation": 1.2, "volume": 10})
    assert df.loc[0, "index_value"] == 120000
