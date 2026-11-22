import unittest
from src.extract.api_client import APIClient
from src.transform.transformer import DataTransformer
from src.load.database import DatabaseLoader

class TestETL(unittest.TestCase):
    def test_api_client_initialization(self):
        with self.assertRaises(ValueError):
            APIClient()  # Should raise error if API_KEY not in env

    def test_transformer_with_valid_data(self):
        test_data = [{'id': 1, 'value': 'test'}]
        transformer = DataTransformer()
        result = transformer.transform_data(test_data)
        self.assertFalse(result.empty)
        self.assertEqual(len(result), 1)

    def test_database_loader_initialization(self):
        with self.assertRaises(ValueError):
            DatabaseLoader()  # Should raise error if DB_CONNECTION not in env

if __name__ == '__main__':
    unittest.main()