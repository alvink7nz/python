from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Create a player entity
player = FirstPersonController()

# Create a grid of cubes
for z in range(20):
    for x in range(20):
        cube = Entity(model='cube', color=color.green, position=(x, -3, z), texture='white_cube')

# Run the Ursina application
app.run()
