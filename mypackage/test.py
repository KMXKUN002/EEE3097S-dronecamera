import time
import picamera

with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    camera.start_preview()
    camera.start_recording('my_video.h264')
    time.sleep(0.5)
    for x in range(25,100):
        zoom_param = (100-x)/200.
        camera.zoom = (zoom_param, zoom_param, 1 - zoom_param, 1 - zoom_param)
        time.sleep(0.1)
    camera.stop_recording()
