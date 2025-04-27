from flask import Flask, render_template
import subprocess

app = Flask(__name__)

# Global variable to keep track of the webcam capture status
capture_active = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-capture')
def start_capture():
    # Code to start the webcam capture
    # ...
    try:
        global capture_active
        capture_active = True

        subprocess.run(['python', 'canvas.py'], check=True)

        # Reset the capture status when board.py finishes
        capture_active = False

        return {'status': 'success', 'message': 'canvas.py executed'}
    except subprocess.CalledProcessError:
        capture_active = False
        return {'status': 'error', 'message': 'Failed to run Air Canvas'}

@app.route('/run-board')
def run_board():
    try:
        global capture_active
        capture_active = True

        subprocess.run(['python', 'board.py'], check=True)

        # Reset the capture status when board.py finishes
        capture_active = False

        return {'status': 'success', 'message': 'board.py executed'}
    except subprocess.CalledProcessError:
        capture_active = False
        return {'status': 'error', 'message': 'Failed to run White Board'}

@app.route('/stop-capture')
def stop_capture():
    global capture_active
    capture_active = False
    return {'status': 'success', 'message': 'Capture stopped'}

if __name__ == '__main__':
    app.run(debug=True)
