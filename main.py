from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('audio_data')
def handle_audio_data(data):
    # Broadcast the audio data to all connected clients
    emit('play_audio', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")