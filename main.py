""" 
Authors: Omar Mohammed, Nabeel Ahmad
Creation date: 11/07/23
Last modified: 11/07/23
"""

from flask import Flask 
from flask_socketio import SocketIO
import config 


app = Flask(__name__)
app.config['SECRET_KEY'] = config.flask_auth_key 
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app,debug=True)

