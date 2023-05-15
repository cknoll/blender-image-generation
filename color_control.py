import bpy
import sys, os


# function to set the sky color
def set_sky_color(air_density):
    world = bpy.data.worlds["World"]
    nodes = world.node_tree.nodes

    # set air density
    nodes["Sky Texture"].air_density = air_density


# function to render an image with a given sky color
def render_with_sky_color(color):
    # set the sky color
    set_sky_color(color)

    # set up scene
    scene = bpy.context.scene
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = os.path.join(os.getcwd(), "img", f"./img/blender_sky_{color:.1f}.png")

    bpy.ops.render.render(write_still=True)


# main function
def main():
    # parse command line arguments
    args = sys.argv[sys.argv.index("--") + 1 :]  # Get all arguments after "--"

    # Parse color argument if provided
    if args and not args[0].startswith("-"):
        color = float(args[0])

    set_sky_color(color)

    # render the image with the specified sky color
    render_with_sky_color(color)


# run the main function
if __name__ == "__main__":
    main()
