from flask import Flask, render_template, Response
import dronecamera

app = Flask(__name__)
camera = dronecamera.DroneCamera(resolution='640x480', framerate=24)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        frame = camera.output.frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),\
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
