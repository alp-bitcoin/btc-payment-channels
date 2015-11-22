from payment_channels import app

from flask import jsonify, abort

@app.route('/api/v1/connections')
def get_connections():
    from connections import connections
    return jsonify({'connections': list(map(lambda x: x.serialize(), connections))})
    
    
@app.route('/api/v1/connections/<int:id>', methods=['GET'])
def get_connection(id):
    connection = find_connection(id)
    return jsonify({'connection': connection.serialize()})

@app.route('/api/v1/connections/<int:id>/fund/<int:amount>', methods=['POST'])
def fund_connection(id, amount):
    connection = find_connection(id)
    try:
        connection.fund(amount)
    except RuntimeError as ex:
        abort(400)
    return jsonify({'connection': connection.serialize()})

@app.route('/api/v1/connections/<int:id>/funded', methods=['POST'])
def funded_connection(id):
    connection = find_connection(id)
    try:
        connection.funded()
    except RuntimeError as ex:
        abort(400)
    return jsonify({'connection': connection.serialize()})
    
@app.route('/api/v1/connections/<int:id>/close', methods=['POST'])
def close(id):
    connection = find_connection(id)
    try:
        connection.close()
    except RuntimeError as ex:
        abort(400)
    return jsonify({'connection': connection.serialize()})

def find_connection(id):
    from connections import connections
    connection = [connection for connection in connections if connection.id == id]
    if len(connection) == 0:
        abort(404)
    return connection[0]
    
