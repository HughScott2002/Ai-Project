import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

db_config = {
    "host": host,
    "user": user,
    "password": password,
    "database": database,
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("Cursor created successfully")
except Exception as e:
    print(f"Error creating cursor: {e}")
