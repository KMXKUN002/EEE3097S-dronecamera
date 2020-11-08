The demonstrator uses Python Flask to make an interactive HTML page.

Features
--------

Methods:
    gen(DroneCamera camera) -- A generator function to continually return 
        the frame() buffer from the DroneCamera class.
    
    video_feed() -- Retrieves individual frames from the frame buffer.

    zoom() -- Either sets or gets the zoom level.

    capture() -- Redirects user to where they may download a snapshot.
        The name of the image is determined by the coordinates.

    capture_with_filename() -- Downloads snapshot image.