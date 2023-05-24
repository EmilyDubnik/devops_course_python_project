from flask import Flask
import db_connector
import os
import signal


HOSTNAME: str = '127.0.0.1'
PORT: int = 5001

app = Flask(__name__)
#Get user_name by user_id from DB and return result in HTML format
@app.route("/users/get_user_data/<user_id>", methods = ['GET'])
def get_user_name(user_id):
    user_name = db_connector.get_user_name_by_user_id(user_id)
    if user_name != "user_id doesn't exist":
        return "<H1 id='user'>" + user_name + "</H1>"
    else:
        return "<H1 id='error'>" + "no such user: " + user_id + "</H1>"

#Automatic termination
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

if __name__ == '__main__':
    app.run(host=HOSTNAME, debug=True, port=PORT)