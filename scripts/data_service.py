from sqlalchemy import create_engine, text
import json

# Setup engine
DATABASE_URL = "sqlite:///wellken.db"
engine = create_engine(DATABASE_URL)

def get_all_data(table_name):
    """Fetches all rows from a given table and returns them as a JSON string."""
    with engine.connect() as connection:
        query = text(f"SELECT * FROM {table_name}")
        result = connection.execute(query)
        # Convert rows to a list of dictionaries
        data = [dict(row._mapping) for row in result]
        return json.dumps(data, default=str)

# Example usage
if __name__ == "__main__":
    print(get_all_data("your_table_name_here"))
