import requests
from ..config.settings import API_TIMEOUT
from ..utils.logger import get_logger

logger = get_logger(__name__)

class IbovespaClient:
    BASE_URL = "https://www.infomoney.com.br/wp-json/infomoney/v1/cotacoes/ibovespa"

    def fetch_ibovespa_data(self):
        """Fetch current Ibovespa data from InfoMoney"""
        try:
            logger.info("Fetching Ibovespa data")
            response = requests.get(self.BASE_URL, timeout=API_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch Ibovespa data: {str(e)}")
            raise