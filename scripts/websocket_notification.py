
from flask_socketio import SocketIO, emit

socketio = SocketIO()

@socketio.on('message')
def handle_message(data):
    print(f'Received message: {data}')
    emit('response', {'status': 'Success', 'message': 'Notification received'})
