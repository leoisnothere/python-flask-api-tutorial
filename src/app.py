from flask import Flask, jsonify, request
todos = [ { "label": "Prueba1", "done": False },{ "label": "Prueba2", "done": True }]
app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    # Puedes convertir esa variable en una cadena json de la siguiente manera
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request.get_json(force=True))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos), 201


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)