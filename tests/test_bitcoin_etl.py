import unittest
from unittest.mock import patch
from src.extract.infomoney_client import InfoMoneyClient
from src.transform.bitcoin_transformer import BitcoinTransformer

class TestBitcoinETL(unittest.TestCase):
    def test_infomoney_client(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {'price': 50000}
            client = InfoMoneyClient()
            data = client.fetch_bitcoin_price()
            self.assertEqual(data['price'], 50000)

    def test_bitcoin_transformer(self):
        raw_data = {'price': 50000}
        transformer = BitcoinTransformer()
        df = transformer.transform_price_data(raw_data)
        self.assertEqual(df['price_usd'].iloc[0], 50000)
        self.assertEqual(df['source'].iloc[0], 'infomoney')

if __name__ == '__main__':
    unittest.main()