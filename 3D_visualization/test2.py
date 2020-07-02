import pyglet
from pyglet.window import key
import ratcave as rc

# Create Window and Add Keyboard State Handler to it's Event Loop
window = pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# Create Mesh
cube = obj_reader.get_mesh("Cube", position=(0, 0, -1.5), scale=.3)

# Create Scene
scene = rc.Scene(meshes=[cube])
scene.bgColor = 1, 0, 0

# Functions to Run in Event Loop
def rotate_meshes(dt):
    cube.rotation.y += 15 * dt  # dt is the time between frames

pyglet.clock.schedule(rotate_meshes)


def move_camera(dt):
    camera_speed = 3
    if keys[key.LEFT]:
        scene.camera.position.x += camera_speed * dt
    if keys[key.RIGHT]:
        scene.camera.position.x -= camera_speed * dt
    if keys[key.UP]:
        scene.camera.position.y -= camera_speed * dt
    if keys[key.DOWN]:
        scene.camera.position.y += camera_speed * dt

pyglet.clock.schedule(move_camera)


@window.event
def on_draw():
    with rc.default_shader:
        scene.draw()


pyglet.app.run()