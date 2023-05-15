import bpy
import os

import math
import numpy as np

def rotate(point, angle_degrees, axis=(0,1,0)):
    theta_degrees = angle_degrees
    theta_radians = math.radians(theta_degrees)

    rotated_point =  np.dot(rotation_matrix(axis, theta_radians), point)
    
    return rotated_point


def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


# create img folder if it doesn't exist
if not os.path.exists('img'):
    os.makedirs('img')

# get camera and lighthouse collection
cam = bpy.data.objects.get("Camera")
lighthouse_col = bpy.data.collections.get("Lighthouse")
lighthouse_obj = None

# if lighthouse collection exists, track it, else track any object in the scene
if lighthouse_col:
    lighthouse_obj = lighthouse_col.objects[0]
else:
    lighthouse_obj = bpy.context.scene.objects[0]

# set up track constraint
track_constraint = cam.constraints.get("Track To")
if not track_constraint:
    track_constraint = cam.constraints.new(type='TRACK_TO')
track_constraint.target = lighthouse_obj
track_constraint.track_axis = 'TRACK_NEGATIVE_Z'
track_constraint.up_axis = 'UP_Y'



# set up scene
scene = bpy.context.scene
scene.render.image_settings.file_format = 'PNG'

# set initial camera location and rotation
cam_location = cam.location
cam_rotation = cam.rotation_euler


for angle in range(0, 360, 10):
    # update camera location and rotation
    cam.location = rotate(cam_location, 10, axis=(0,0,1))
    cam.rotation_euler = rotate(cam_rotation, 10, axis=(0,0,1))

    # render image
    scene.render.filepath = os.path.join(os.getcwd(), 'img',  f'./img/blender_{angle:03d}.png')
    bpy.ops.render.render(write_still=True)



