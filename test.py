# test.py
import os
from sqlalchemy import create_engine, text

# Load environment variables (set in your docker-compose file)
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "testdb")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_HOST = "localhost"  # Docker exposes on localhost

# Create SQLAlchemy engine
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            print("✅ Connected to Postgres!")
            for row in result:
                print("Postgres version:", row[0])
    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    test_connection()
