import picamera
import io
from threading import Condition

class DroneCamera():

    def __init__(self):
        """Initialises with the attributes:
        
        x_coordinate -- The x-coordinate of the drone
        y_coordinate -- The y-coordinate of the drone
        camera -- PiCamera object
        zoom -- The zoom level of the camera
        """
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.camera = None
        self.zoom = 0
    
    def __enter__(self):
        """Initialises with __enter__ so that __exit__ can be used to cleanly 
        end the interface with camera.
        """
        self.camera = picamera.PiCamera(resolution='640x480', framerate=24)\
            .__enter__()
        return self
    
    def __exit__(self, *args):
        """Cleanly ends interaction with camera."""
        self.camera.__exit__(*args)

    def frames(self):
        """Pushes frames from the camera into a buffer."""
        buffer = io.BytesIO()
        for _ in self.camera.capture_continuous(buffer, 'jpeg', \
            use_video_port=True):
            buffer.seek(0)
            yield buffer.read()

            buffer.seek(0)
            buffer.truncate()

    def frame(self):
        """Outputs the first-place frame in the buffer that contains camera
        frames.
        """
        buffer = io.BytesIO()
        self.camera.capture(buffer, 'jpeg')
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def camera_zoom(zoom):
        """In-class method to calculate decimal zoom values (0 - 1) from an 
        integer value (0 - 100).

        :type zoom: int
        :param zoom: The zoom level of the camera ranging from 0 - 100
        """
        z = zoom / 200
        return (z, z, 1 - z * 2, 1 - z * 2)

    def set_zoom(self, zoom):
        """Sets the zoom level of the camera. This is a crop function that 
        uses the zoom() function of the picamera method.

        :type zoom: int
        :param zoom: The zoom level of the camera ranging from 0 - 100
        """
        self.zoom = zoom
        self.camera.zoom = self.camera_zoom(zoom)

    def get_zoom(self):
        """Returns the zoom level in integer value (0 - 100)."""
        return self.zoom

    def set_coordinates(self, x, y):
        """Sets the coordinate values.
        
        :type x: float
        :param x: The x-coordinate

        :type y: float
        :param y: The y-coordinate
        """
        self.x_coordinate = x
        self.y_coordinate = y

    def get_x_coordinate(self):
        """Returns x-coordinate value."""
        return self.x_coordinate
    
    def get_y_coordinate(self):
        """Returns y-coordinate value."""
        return self.y_coordinate

    def get_coordinates(self):
        """Returns x- and y-coordinate values."""
        return (self.x_coordinate, self.y_coordinate)

    