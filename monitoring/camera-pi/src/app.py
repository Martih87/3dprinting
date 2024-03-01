from flask import Flask, render_template, Response, request, jsonify
from camera import Camera  # Assuming you have a Camera class that handles the video streaming

app = Flask(__name__)

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

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
