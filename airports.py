# airports.py

import mysql.connector

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tiger',
    'database': 'airline',
    'port': 3306
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def fetch_airports():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT airport_name FROM airports ORDER BY airport_id")
        airports = cursor.fetchall()
        cursor.close()
        connection.close()
        return airports
    except Exception as e:
        print(f"Error fetching airports: {e}")
        return None
