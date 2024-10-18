
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO, emit
import os, threading, logging
from scripts.multi_device_camera import start_camera
from scripts.voice_analysis import analyze_voice
from scripts.body_language import analyze_body_language
from scripts.responsible_ai import check_fairness

app = Flask(__name__)
app.secret_key = 'supersecretkey'
socketio = SocketIO(app)

# User Authentication
users = {"admin": "password"}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['user'] = username
            return redirect(url_for('home'))
        return "Invalid credentials, try again!"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/camera', methods=['GET'])
def camera():
    threading.Thread(target=start_camera).start()
    return jsonify({'status': 'Camera started'})

@app.route('/voice_analysis', methods=['POST'])
def voice_analysis():
    audio_file = request.files['audio']
    audio_path = os.path.join('uploads', audio_file.filename)
    audio_file.save(audio_path)
    result = analyze_voice(audio_path)
    return jsonify(result)

@app.route('/body_language', methods=['POST'])
def body_language():
    video_file = request.files['video']
    video_path = os.path.join('uploads', video_file.filename)
    video_file.save(video_path)
    threading.Thread(target=analyze_body_language, args=(video_path,)).start()
    return jsonify({'status': 'Body language analysis started'})

@app.route('/fairness_check', methods=['POST'])
def fairness_check():
    context = request.json.get('context', '')
    check_fairness({}, context)
    return jsonify({'status': f'Fairness check completed for context: {context}'})

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
