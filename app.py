from flask import Flask, jsonify, request
app = Flask(__name__)
store = {}
@app.route('/')
def root():
    #Root endpoint that provides an overview of the API features.
    description = "This is a simple key-value store API."
    features = [
        "GET /get/<key>: Retrieve the value associated with a given key.",
        "POST /set: Set a key-value pair.",
        "GET /search: Search for keys based on a prefix or suffix."
    ]
    return jsonify(description=description, features=features)


@app.route('/get/<key>', methods=['GET'])
def get_key(key):
    """
    Retrieve the value associated with a given key.
    """
    if key in store:
        return jsonify({key: store[key]}), 200
    else:
        return jsonify(error='Key not found'), 404


@app.route('/set', methods=['POST'])
def set_key():
    """
    Set a key-value pair.
    """
    data = request.get_json()
    if 'key' in data and 'value' in data:
        key = data['key']
        value = data['value']
        store[key] = value
        return jsonify(message='Key-value pair set successfully'), 200
    else:
        return jsonify(error='Invalid request data'), 400


@app.route('/search', methods=['GET'])
def search_keys():
    """
    Search for keys based on a prefix or suffix.
    """
    prefix = request.args.get('prefix')
    suffix = request.args.get('suffix')
    keys = []
    if prefix:
        keys = [key for key in store.keys() if key.startswith(prefix)]
    elif suffix:
        keys = [key for key in store.keys() if key.endswith(suffix)]
    return jsonify(keys=keys), 200


if __name__ == '__main__':
    app.run()
