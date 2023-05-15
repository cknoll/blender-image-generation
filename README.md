[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Usage

The lighthouse_scene.blend file and the render.py must be placed in the same folder. From the folder run headless blender to execute script:

`blender -b lighthouse_scene.blend -P render.py`


With the color_control.py file is possible to set the air density from command line to change the color of the the sky. The air density is a value in the range (0, 10) with the default value set close to 0. To change it to 5 run the following command:

`blender -b lighthouse_scene.blend -P color_control.py -- 5.0`

This will change the color from blue to orange and it will render a single image with the result.
