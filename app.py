from flask import Flask, render_template, request
from product_manager import create_product
from product_manager import fetch_products

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('products.html')

@app.route('/create_product', methods=['POST'])
def handle_product_creation():
    name = request.form['name']
    description = request.form['description']
    price = float(request.form['price'])
    stock_quantity = int(request.form['stock_quantity'])
    category_id = int(request.form['category_id'])  

    result = create_product(name, description, price, stock_quantity, category_id)
    if result:
        return 'Product created successfully!'
    else:
        return 'Error creating product.'
@app.route('/products')
def display_products():
    products = fetch_products()
    for product in products:
        if 'image_url' not in product:
            product['image_url'] = 'party-dog.png' 
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True) 
