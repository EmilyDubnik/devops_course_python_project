from flask import Flask
from flask import jsonify
from flask import request
import db_connector
import os
import signal


HOSTNAME: str = '127.0.0.1'
PORT: int = 5000

app = Flask(__name__)

# Add a new row to the users table
@app.route("/users/<user_id>", methods = ['POST'])
def create_user(user_id):
    data = request.get_json()
    user_name = data['user_name']
    res = db_connector.add_user(user_id,user_name)
    if res == "Row Added Successfully":
        return jsonify(
            status = "ok",
            user_added=user_name
        ), 200
    else:
        return jsonify(
            status = "error",
            reason = f'user_id {user_id} already exists'
        ), 500

#Get a user by ID
@app.route("/users/<user_id>", methods = ['GET'])
def get_user(user_id):
    res = db_connector.get_user_name_by_user_id(user_id)
    if res != "user_id doesn't exist":
        return jsonify(
            status = "ok",
            user_name=res
        ), 200
    else:
        return jsonify(
            status = "error",
            reason = "no such id"
        ), 500

#Set a new username to a specific ID
@app.route("/users/<user_id>", methods = ['PUT'])
def set_user(user_id):
    data = request.get_json()
    new_user_name = data['user_name']
    res = db_connector.update_username(user_id,new_user_name)
    if res == "user_name updated successfully":
        return jsonify(
            status = "ok",
            user_updated=res
        ), 200
    else:
        return jsonify(
            status = "error",
            reason = "no such id"
        ), 500

#Delete an existing user
@app.route("/users/<user_id>", methods = ['DELETE'])
def delete_user(user_id):
    res = db_connector.delete_user(user_id)
    if res == "User deleted successfully":
        return jsonify(
            status = "ok",
            user_deleted=res
        ), 200
    else:
        return jsonify(
            status = "error",
            reason = "no such id"
        ), 500

#Automatic termination
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


if __name__ == '__main__':
    app.run(host=HOSTNAME, debug=True, port=PORT)