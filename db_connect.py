import psycopg2
import logging

conn_params = {
    'host': 'postgres',  # Service name in docker-compose.yml
    'port': '5432',
    'database': 'eshop_db',
    'user': 'eshop_user',
    'password': 'admin'
}


def connect_db():
    try:
        conn = psycopg2.connect(**conn_params)
        logging.info("Database connection successful") 
        return conn
    except (Exception, psycopg2.Error) as error:
        logging.error(f"Error connecting to PostgreSQL: {error}")
        return None
