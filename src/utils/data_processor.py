"""Data processing utilities"""
import pandas as pd
from typing import Dict

def calculate_moving_average(data: pd.DataFrame, window: int = 5) -> pd.Series:
    """Calculate moving average of index values"""
    return data['index_value'].rolling(window=window).mean()

def calculate_statistics(data: pd.DataFrame) -> Dict[str, float]:
    """Calculate key statistics from the data"""
    if data.empty:
        return {
            'daily_change': 0,
            'avg_value': 0,
            'min_value': 0,
            'max_value': 0
        }
    
    return {
        'daily_change': data['variation'].iloc[-1],
        'avg_value': data['index_value'].mean(),
        'min_value': data['index_value'].min(),
        'max_value': data['index_value'].max()
    }