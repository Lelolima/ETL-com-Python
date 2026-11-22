"""Application configuration settings"""
from datetime import timedelta

# API Settings
API_BASE_URL = "https://www.infomoney.com.br/wp-json/infomoney/v1"
API_TIMEOUT = 30  # seconds

# Dashboard Settings
UPDATE_INTERVAL = 60  # seconds
MAX_DATA_POINTS = 100  # Maximum number of points to show on graphs
CACHE_TIMEOUT = timedelta(minutes=5)

# Chart Colors
COLORS = {
    'positive': '#00ff00',
    'negative': '#ff0000',
    'neutral': '#808080',
    'background': '#ffffff',
    'text': '#000000'
}