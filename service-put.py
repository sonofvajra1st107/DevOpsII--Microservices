from flask import Flask, request, jsonify
import product_item as prod

app = Flask(__name__)

@app.route('/update', methods=['PUT'])
def update():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    _user = prod.get_products()
    data = [x for x in _user if x["name"]==name]
    #Get Data
    if data:
        prod.update_product(name,category,price,instock)
        return jsonify({'message': 'Update successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot update item.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) 