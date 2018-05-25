from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

products = {
    42: {'id': 42, 'name': 'Phone', 'price': 121},
    43: {'id': 43, 'name': 'phoNE', 'price': 118},
}

@app.route("/products")
def _products():
    return render_template('products.html', products=products.values())
#     return '</br>'.join(['<span>{}</span>: <b>{}</b>'.format(v['name'], v['price']) for v in fixture])

@app.route('/products/<int:product_id>')
def _product(product_id):
    print('ID', product_id)
    product = products.get(product_id, {})
    # product = {}
    # for k, v in products:
    #     if v['id'] == product_id:
    #         product = v
    #         print('PRODUCT', v)
    return render_template('product.html', **product)
