import pandas as pd
from datetime import datetime
from ..utils.logger import get_logger

logger = get_logger(__name__)

class IbovespaTransformer:
    def transform_market_data(self, raw_data):
        """Transform raw Ibovespa data into structured format"""
        try:
            logger.info("Transforming Ibovespa data")
            df = pd.DataFrame([{
                'index_value': raw_data.get('value', 0),
                'variation': raw_data.get('variation', 0),
                'volume': raw_data.get('volume', 0),
                'timestamp': datetime.now().isoformat()
            }])
            return df
        except Exception as e:
            logger.error(f"Failed to transform Ibovespa data: {str(e)}")
            raise