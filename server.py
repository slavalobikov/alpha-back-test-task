from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app, support_credentials=True)



data = [
    {"id": 1, "name": "John Doe", "age": 24, "photo": "", "job_title": "", "bio": ""},
    {"id": 2, "name": "John Doe", "age": 32, "photo": "", "job_title": "", "bio": ""},
    {"id": 3, "name": "John Doe", "age": 44, "photo": "", "job_title": "", "bio": ""}
]


@app.route('/users', methods=['GET'])
def get_data():
    return jsonify(data)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_element(user_id):
    for item in data:
        if item['id'] == user_id:
            return jsonify(item)
    return jsonify({"message": "Item not found"})


@app.route('/users', methods=['POST'])
def create_element():
    new_element = {"id": len(data) + 1, "name": request.json['name'], "age": request.json['age'],
                   "photo": request.json['photo'], "job_title": request.json['job_title'], "bio": request.json['bio']}
    data.append(new_element)
    return jsonify(new_element)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_element(user_id):
    for item in data:
        if item['id'] == user_id:
            item['name'] = request.json['name']
            item['photo'] = request.json['photo']
            item['job_title'] = request.json['job_title']
            item['bio'] = request.json['bio']
            return jsonify(item)
    return jsonify({"message": "Item not found"})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_element(user_id):
    for item in data:
        if item['id'] == user_id:
            data.remove(item)
            return jsonify({"message": "Item deleted"})
    return jsonify({"message": "Item not found"})


if __name__ == '__main__':
    app.run()
