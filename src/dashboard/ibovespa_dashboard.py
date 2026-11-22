"""Main dashboard application"""
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from ..config.settings import UPDATE_INTERVAL, MAX_DATA_POINTS, CACHE_TIMEOUT
from ..extract.ibovespa_client import IbovespaClient
from ..transform.ibovespa_transformer import IbovespaTransformer
from ..utils.logger import get_logger
from ..utils.cache import Cache
from ..utils.data_processor import calculate_statistics
from .components.charts import create_main_chart, create_volume_chart
from .components.stats import create_stats_panel

logger = get_logger(__name__)

class IbovespaDashboard:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.client = IbovespaClient()
        self.transformer = IbovespaTransformer()
        self.cache = Cache(CACHE_TIMEOUT)
        self.data = pd.DataFrame()
        
        self.setup_layout()
        self.setup_callbacks()
    
    def setup_layout(self):
        """Setup dashboard layout"""
        self.app.layout = html.Div([
            html.Div([
                html.H1('Ibovespa Real-time Dashboard'),
                html.P(f'Auto-updates every {UPDATE_INTERVAL} seconds'),
            ], className='header'),
            
            html.Div(id='stats-container'),
            html.Div(id='main-chart-container'),
            html.Div(id='volume-chart-container'),
            
            dcc.Interval(
                id='interval-component',
                interval=UPDATE_INTERVAL * 1000,
                n_intervals=0
            )
        ])
    
    def setup_callbacks(self):
        """Setup dashboard callbacks"""
        @self.app.callback(
            [Output('stats-container', 'children'),
             Output('main-chart-container', 'children'),
             Output('volume-chart-container', 'children')],
            [Input('interval-component', 'n_intervals')]
        )
        def update_dashboard(n):
            try:
                # Try to get data from cache first
                data = self.cache.get('market_data')
                if data is None:
                    raw_data = self.client.fetch_ibovespa_data()
                    new_data = self.transformer.transform_market_data(raw_data)
                    
                    # Append to existing data and limit size
                    self.data = pd.concat([self.data, new_data]).tail(MAX_DATA_POINTS)
                    self.cache.set('market_data', self.data)
                else:
                    self.data = data
                
                # Calculate statistics
                stats = calculate_statistics(self.data)
                
                # Create components
                stats_panel = create_stats_panel(stats)
                main_chart = create_main_chart(self.data)
                volume_chart = create_volume_chart(self.data)
                
                return stats_panel, main_chart, volume_chart
                
            except Exception as e:
                logger.error(f"Failed to update dashboard: {str(e)}")
                return html.Div("Error loading data"), html.Div(), html.Div()
    
    def run(self, debug=False):
        """Run the dashboard server"""
        self.app.run(debug=debug)