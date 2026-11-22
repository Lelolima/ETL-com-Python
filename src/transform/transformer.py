import pandas as pd

class DataTransformer:
    @staticmethod
    def transform_data(data):
        """
        Transform the raw data using pandas
        """
        try:
            # Convert to DataFrame
            df = pd.DataFrame(data)
            
            # Basic cleaning
            df = df.dropna()  # Remove null values
            
            # Add any specific transformations here
            
            return df
        except Exception as e:
            raise Exception(f"Error transforming data: {str(e)}")