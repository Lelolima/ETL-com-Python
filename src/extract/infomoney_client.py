import requests
from ..config.settings import API_TIMEOUT
from ..utils.logger import get_logger

logger = get_logger(__name__)

class InfoMoneyClient:
    BASE_URL = "https://www.infomoney.com.br/wp-json/infomoney/v1/cotacoes/bitcoin"

    def fetch_bitcoin_price(self):
        """Fetch current Bitcoin price from InfoMoney"""
        try:
            logger.info("Fetching Bitcoin price from InfoMoney")
            response = requests.get(self.BASE_URL, timeout=API_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch Bitcoin price: {str(e)}")
            raise