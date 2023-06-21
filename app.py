from flask import Flask, jsonify, request

app = Flask(__name__)
store = {}


@app.route('/get/<key>', methods=['GET'])
def get_key(key):
    if key in store:
        return jsonify({key: store[key]})
    else:
        return jsonify(error='Key not found'), 404


@app.route('/set', methods=['POST'])
def set_key():
    data = request.get_json()
    if 'key' in data and 'value' in data:
        key = data['key']
        value = data['value']
        store[key] = value
        return jsonify(message='Key-value pair set successfully')
    else:
        return jsonify(error='Invalid request data'), 400


@app.route('/search', methods=['GET'])
def search_keys():
    prefix = request.args.get('prefix')
    suffix = request.args.get('suffix')
    keys = []
    if prefix:
        keys = [key for key in store.keys() if key.startswith(prefix)]
    elif suffix:
        keys = [key for key in store.keys() if key.endswith(suffix)]
    return jsonify(keys=keys)


if __name__ == '__main__':
    app.run()
