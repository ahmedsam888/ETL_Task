import psycopg2

# Database connection parameters
DB_HOST = 'ep-broad-tree-84296081-pooler.eu-central-1.postgres.vercel-storage.com'
DB_PORT = '5432'
DB_NAME = 'verceldb'
DB_USER = 'default'
DB_PASSWORD = 'yx4LeTgKdC7z'

def test_postgres_connection():
    try:
        conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        print("Connection to PostgreSQL database successful!")
        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
