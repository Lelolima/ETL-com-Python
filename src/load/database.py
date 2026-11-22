from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseLoader:
    def __init__(self):
        self.connection_string = os.getenv('DB_CONNECTION')
        if not self.connection_string:
            raise ValueError("DB_CONNECTION not found in environment variables")
        
        self.engine = create_engine(self.connection_string)

    def load_data(self, df, table_name):
        """
        Load DataFrame into database
        """
        try:
            df.to_sql(table_name, self.engine, if_exists='append', index=False)
        except Exception as e:
            raise Exception(f"Error loading data to database: {str(e)}")