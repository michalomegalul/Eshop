import psycopg2

conn_params = {
    'host': '192.168.1.110',
    'port': '5432',
    'database': 'eshop_db',
    'user': 'admin',
    'password': 'admin'
}

def connect_db():
    try:
        conn = psycopg2.connect(**conn_params)
        return conn
    except (Exception, psycopg2.Error) as error:
        print(f"Error connecting to PostgreSQL: {error}")
        return None
