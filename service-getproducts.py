from flask import Flask, request, jsonify
import product_item as prod

app = Flask(__name__)


@app.route('/products', methods=['GET'])
def products():
    _products = prod.get_products()
    return jsonify(_products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
