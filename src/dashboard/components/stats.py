"""Dashboard statistics components"""
from dash import html
from typing import Dict

def create_stats_panel(stats: Dict[str, float]) -> html.Div:
    """Create statistics panel"""
    return html.Div([
        html.Div([
            html.H3('Daily Statistics'),
            html.Div([
                create_stat_card('Daily Change', f"{stats['daily_change']:.2f}%"),
                create_stat_card('Average', f"{stats['avg_value']:.2f}"),
                create_stat_card('Min', f"{stats['min_value']:.2f}"),
                create_stat_card('Max', f"{stats['max_value']:.2f}")
            ], style={'display': 'flex', 'justifyContent': 'space-between'})
        ])
    ], className='stats-panel')

def create_stat_card(label: str, value: str) -> html.Div:
    """Create individual stat card"""
    return html.Div([
        html.P(label, className='stat-label'),
        html.H4(value, className='stat-value')
    ], className='stat-card')