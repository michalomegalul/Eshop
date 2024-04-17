from db_connect import connect_db

def create_product(name, description, price, stock_quantity, category_id):
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO products (name, description, price, stock_quantity, category_id)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
            """,
            (name, description, price, stock_quantity, category_id)
        )
        product_id = cur.fetchone()[0]  # Extract created ID
        conn.commit()
        cur.close()
        conn.close()
        return product_id
    else:
        return None
def fetch_products():
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE stock_quantity > 0")
        products = cur.fetchall()
        cur.close()
        conn.close()
        return products
    else:
        return None