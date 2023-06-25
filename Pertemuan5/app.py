from flask import Flask, request, jsonify
import json

app = Flask(__name__)

DATA_FILE = 'data.json'

def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    return "API Ready"

@app.route('/stores', methods=['GET'])
def get_stores():
    stores = load_data()

    return jsonify(stores)

@app.route('/stores/<int:store_id>', methods=['GET'])
def get_store(store_id):
    stores = load_data()

    for store in stores:
        if store['id'] == store_id:
            return jsonify(store)

    return jsonify({'error': 'Store not found'}), 404

@app.route('/stores', methods=['POST'])
def add_store():
    stores = load_data()
    data = request.get_json()

    required_keys = {'name', 'address', 'phone'}

    if not required_keys.issubset(data.keys()):
        missing_keys = required_keys - data.keys()
        return jsonify({'error': f'Missing required keys: {", ".join(missing_keys)}'}), 400

    new_store = {
        'id': max(store['id'] for store in stores) + 1,
        'name': data['name'],
        'address': data['address'],
        'phone': data['phone'],
    }

    stores.append(new_store)
    save_data(stores)

    return jsonify(new_store), 201

if __name__ == '__main__':
    app.run(debug = True)
