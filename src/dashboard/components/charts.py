"""Dashboard chart components"""
import plotly.graph_objs as go
from dash import dcc
import pandas as pd
from ...config.settings import COLORS

def create_main_chart(data: pd.DataFrame) -> dcc.Graph:
    """Create the main Ibovespa chart"""
    return dcc.Graph(
        id='main-chart',
        figure={
            'data': [
                go.Scatter(
                    x=data['timestamp'],
                    y=data['index_value'],
                    name='Ibovespa',
                    mode='lines+markers',
                    line={'color': COLORS['neutral']}
                )
            ],
            'layout': go.Layout(
                title='Ibovespa Index Value',
                template='plotly_white',
                height=600,
                xaxis={'title': 'Time'},
                yaxis={'title': 'Index Value'}
            )
        }
    )

def create_volume_chart(data: pd.DataFrame) -> dcc.Graph:
    """Create volume analysis chart"""
    return dcc.Graph(
        id='volume-chart',
        figure={
            'data': [
                go.Bar(
                    x=data['timestamp'],
                    y=data['volume'],
                    name='Volume'
                )
            ],
            'layout': go.Layout(
                title='Trading Volume',
                height=300,
                xaxis={'title': 'Time'},
                yaxis={'title': 'Volume'}
            )
        }
    )