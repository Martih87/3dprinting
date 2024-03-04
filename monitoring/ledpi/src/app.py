from flask import Flask, request, render_template, jsonify
import rpi_ws281x

app = Flask(__name__)

# Create a strip with the parameters appropriate for your LED strip
strip = rpi_ws281x.PixelStrip(46, 18, 800000, 5, False, 255)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_color', methods=['POST'])
def set_color():
    color = request.form.get('color')
    if color:
        color = color.lstrip('#')
        color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, rpi_ws281x.Color(*color))
        strip.show()
    return 'OK'


@app.route('/clear')
def clear():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, rpi_ws281x.Color(0, 0, 0))
    strip.show()
    return 'OK'

@app.route('/rainbow')
def rainbow():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, rpi_ws281x.Color(0, 0, 0))
    strip.show()
    theaterChaseRainbow(strip)
    return 'OK'

@app.route('/theater_chase')
def theater_chase():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, rpi_ws281x.Color(0, 0, 0))
    strip.show()
    theaterChase(strip, rpi_ws281x.Color(127, 127, 127))
    return 'OK'


@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    strip.begin()
    app.run(host='0.0.0.0', port=5000, debug=False)
