=========
KMXKUN002-EEE3097S-dronecamera
=========


.. image:: https://img.shields.io/pypi/v/mypackage.svg
        :target: https://pypi.python.org/pypi/mypackage

.. image:: https://img.shields.io/travis/KMXKUN002/mypackage.svg
        :target: https://travis-ci.com/KMXKUN002/mypackage

.. image:: https://readthedocs.org/projects/mypackage/badge/?version=latest
        :target: https://mypackage.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




KMXKUN002-EEE3097S-dronecamera


* Free software: MIT license
* Documentation: https://KMXKUN002-EEE3097S-dronecamera.readthedocs.io.

Install
--------
In terminal, run
	pip install KMXKUN002-3097S-dronecamera

Instantiate with,
	camera = DroneCamera.__enter__()

Features
--------

This API uses the class DroneCamera from dronecamera.py.

Methods:
        __enter__() -- Initialises a 640x480 video stream. Resolution may be 
                modified in code.

        __exit__() -- Cleanly exits the program, ending the connection to the 
                camera.

        frames() -- Creates a buffer into which the camera constantly feeds 
                its frames.

        frame() -- Retrieves the first frame in the buffer.

        set_zoom(int zoom) -- Set a zoom level. This zoom value may range 
                from 0 to 100.

        get_zoom() -- Get zoom level that ranges from 0 to 100.

        set_coordinates(x, y) -- Sets the x- and y-coordinates of the drone.

        get_x_coordinate() -- Returns the x-coordinate.

        get_y_coordinate() -- Returns the y-coordinate.

        get_coordinates() -- Returns both x- and y-coordinates in an array.

When the program ends, the connection to the camera will automatically end as 
well. 

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

The API is an extension of the PiCamera package, which is a copyright of Dave Jones.
