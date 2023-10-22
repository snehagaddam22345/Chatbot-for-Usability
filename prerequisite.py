import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'chatbot_sql',
    'user': 'chatbot_sql_user',
    'password': 'l2yVHSjU8VNKYh1V16FoqXnBqHDAEudY',
    'host': 'dpg-ckq9ol9rfc9c73fl76ag-a',
    'port': 5432  # The default PostgreSQL port
}

# SQL file containing your queries
sql_file = 'schema.sql'

try:
    # Connect to the database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Read and execute the SQL file
    with open(sql_file, 'r') as sql_file:
        cursor.execute(sql_file.read())

    # Commit the changes
    conn.commit()

    print("Schema SQL file executed successfully.")

except psycopg2.Error as e:
    print(f"Error: {e}")
    conn.rollback()

finally:
    if conn:
        conn.close()
