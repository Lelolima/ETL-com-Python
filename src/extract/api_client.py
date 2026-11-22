import requests
import os
from dotenv import load_dotenv

from ..config.settings import API_TIMEOUT

load_dotenv()

class APIClient:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        if not self.api_key:
            raise ValueError("API_KEY not found in environment variables")

    def fetch_data(self, endpoint):
        """
        Fetch data from the specified API endpoint
        """
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.get(endpoint, headers=headers, timeout=API_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data: {str(e)}")