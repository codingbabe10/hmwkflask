@app.route('/user', methods=['GET'])
def user():
    return{'users': list(users.values())}, 200

@app.route('/user', methods=["POST"])
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return {'message' : f'{json_body["username"]} created'}, 201

@app.put('/user')
def update_user():
    return

@app.delete('/user')
def delete_user():
    pass