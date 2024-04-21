from flask import Flask, render_template, request, send_from_directory, abort
import os
from werkzeug.utils import secure_filename
import uuid
from product_manager import create_product, fetch_products, create_category,

app = Flask(__name__)
UPLOAD_FOLDER = './Images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('product_form.html')

@app.route('/create_product', methods=['POST'])
def handle_product_creation():
    name = request.form['name']
    description = request.form['description']
    price = float(request.form['price'])
    stock_quantity = int(request.form['stock_quantity'])
    category_id = int(request.form['category_id'])

    try:
        result = create_product(name, description, price, stock_quantity, category_id)
        return 'Product created successfully!'   
    except Exception as e:
        return f'Error creating product: {e}' 

@app.route('/create_category', methods=['POST'])
def handle_category_creation():
    name = request.form['name']
    try:
        result = create_category(name)
        return 'Category created successfully!'
    except Exception as e:
        return f'Error creating category: {e}'

@app.route('/products')
def display_products():
    products = fetch_products()
    for product in products:
        if 'image_url' not in product:
            product['image_url'] = 'default-image.png'  # Assign default image if not present
    return render_template('products.html', products=products)

from db_connect import connect_db
#working on image server
# @app.route('/upload', methods=['POST'])
# def upload_image():
#     file = request.files['image']
#     if file and allowed_file(file.filename):  # Make sure to check if the file is allowed
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         # Save file information to the database
#         conn = connect_db()
#         if conn:
#             cur = conn.cursor()
#             try:
#                 cur.execute(
#                     "INSERT INTO images (filename, filepath, product_id) VALUES (%s, %s, %s) RETURNING id",
#                     (filename, filepath, product_id)  # Assume product_id or similar is provided or determined
#                 )
#                 image_id = cur.fetchone()[0]
#                 conn.commit()
#                 return jsonify({"message": "Image uploaded successfully", "image_id": image_id}), 201
#             except Exception as e:
#                 conn.rollback()
#                 return jsonify({"error": str(e)}), 500
#             finally:
#                 cur.close()
#                 conn.close()
#         else:
#             return jsonify({"error": "Database connection failed"}), 500
#     else:
#         return "Invalid file or no file uploaded", 400

# @app.route('/images/<filename>')
# def get_image(filename):
#     filename = secure_filename(filename)  # Secure the filename to avoid directory traversal attacks
#     try:
#         return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
#     except FileNotFoundError:
#         abort(404)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5433)
