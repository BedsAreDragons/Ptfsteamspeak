from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('audio')
def handle_audio(data):
    # Broadcast the audio data to all other clients except the sender
    emit('audio', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)