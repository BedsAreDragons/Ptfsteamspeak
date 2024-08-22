from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('audio')
def handle_audio(data):
    # Broadcast the audio data to all other clients
    emit('audio', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")