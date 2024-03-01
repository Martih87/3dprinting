from flask import Flask, render_template, Response, request, jsonify
import picamera
import io
import time

app = Flask(__name__)

camera = picamera.PiCamera()
camera.resolution = (640, 480)

def move_pan_tilt(direction, amount):
    print(f"Moving {direction} by {amount}")

@app.route('/control', methods=['POST'])
def control():
    action = request.form.get('action')
    if action == 'pan-left':
        move_pan_tilt('left', 10)
    elif action == 'pan-right':
        move_pan_tilt('right', 10)
    elif action == 'tilt-up':
        move_pan_tilt('up', 10)
    elif action == 'tilt-down':
        move_pan_tilt('down', 10)
    else:
        return jsonify({'error': 'Invalid action'}), 400
    return jsonify({'status': 'success'}), 200

def gen():
    stream = io.BytesIO()
    for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + stream.getvalue() + b'\r\n\r\n')
        stream.seek(0)
        stream.truncate()

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
