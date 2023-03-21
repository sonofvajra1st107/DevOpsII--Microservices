from flask import Flask, request, jsonify
import product_item as prod

app = Flask(__name__)

@app.route('/delete/<name>', methods=['DELETE'])
def delete(name):
    # Get the product information from the request
    # _user = prod.find_product(name)
    _user = prod.get_products()
    data = [x for x in _user if x["name"] == name]
    if data:
        prod.delete_product(name)   
        return jsonify({'message': 'Item deleted successfully.'}), 200
    else:
        return jsonify({'message': 'Item not found.'}), 404   

    
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
