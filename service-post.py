from flask import Flask, request, jsonify
import product_item as prod

app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    _user = prod.get_products()
    data = [x for x in _user if x["name"]==name]
    #Get Data
    if (data):
        return jsonify({'message': 'Cannot create item.'}), 401
    else:
        prod.add_product(name,category,price,instock)
        return jsonify({'message': 'Created successfully.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) 