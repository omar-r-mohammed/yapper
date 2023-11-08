""" 
Authors: Omar Mohammed, Nabeel Ahmad
Creation date: 11/07/23
Last modified: 11/07/23
"""

from flask import Flask, render_template
from flask_socketio import SocketIO
import config 


app = Flask(__name__)
app.config['SECRET_KEY'] = config.flask_auth_key 
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message received!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app,debug=True)

