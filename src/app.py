from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos',methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text, 202

@app.route('/todos',methods=['POST'])
def add_new_todo():
    decoded = request.get_json()
    print("Petition", decoded)

    todos.append(decoded)
    print(todos)
    json_text = jsonify(todos)
    return json_text, 200

@app.route('/todos/<int:position>',methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete", position)

    longitud= len(todos) 
    print("longitud:", longitud)

    maxIndex= longitud-1

    if position> maxIndex:
        return jsonify({"message":"el numero es mayor de la cantidad de elementos"},400)
    elif longitud == 0:
        return jsonify({"message":"La lista esta vacia, y por eso maxIndex"},400)

    todos.pop(position)

    json_text = jsonify(todos)
    return json_text, 200

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)