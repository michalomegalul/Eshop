from flask import Flask, render_template, request
from product_manager import create_product
from product_manager import fetch_products
from product_manager import create_category

app = Flask(__name__)

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
            product['image_url'] = 'party-dog.png'  # Assign default image if not present
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5433) 
