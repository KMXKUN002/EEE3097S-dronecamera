import picamera
import io
from threading import Condition


class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class DroneCamera(picamera.PiCamera):
    x_coordinate = 0
    y_coordinate = 0
    stream_output = StreamingOutput()

    def test_if_initialised(self):
        """
        Method for testing purposes. A printout confirms the API class has been initialised properly.
        """
        print("Has been initialised")
    
    def start(self):
        self.start_recording(self.stream_output, format='mjpeg')
    
    def stop(self):
        self.stop_recording()

    def set_zoom(self, zoom_param):
        self.zoom = (zoom_param, zoom_param, 1 - zoom_param, 1 - zoom_param)

    def get_zoom(self):
        return self.zoom

    def set_coordinates(self, x, y):
        x_coordinate = x
        y_coordinate = y

    def get_x_coordinate(self):
        return x_coordinate
    
    def get_y_coordinate(self):
        return y_coordinate

    