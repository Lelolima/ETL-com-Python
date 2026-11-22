import pandas as pd
from datetime import datetime
from ..utils.logger import get_logger

logger = get_logger(__name__)

class BitcoinTransformer:
    def transform_price_data(self, raw_data):
        """Transform raw Bitcoin price data into structured format"""
        try:
            logger.info("Transforming Bitcoin price data")
            df = pd.DataFrame([{
                'price_usd': raw_data.get('price', 0),
                'timestamp': datetime.now().isoformat(),
                'source': 'infomoney'
            }])
            return df
        except Exception as e:
            logger.error(f"Failed to transform Bitcoin data: {str(e)}")
            raise