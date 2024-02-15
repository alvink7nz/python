from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Constants
BLOCK_SIZE = 1

# Create an instance of the Ursina application
app = Ursina()
player = FirstPersonController()

# Create a 3D array to represent the world
world_width = 10
world_depth = 10
world_height = 0
world = [[[0] * world_depth for _ in range(world_width)] for _ in range(world_height)]

# Function to generate the world
def generate_world():
    for y in range(world_height):
        for z in range(world_depth):
            for x in range(world_width):
                # Place grass blocks on the top layer
                if y == world_height - 1:
                    world[y][z][x] = 1

# Generate the world
generate_world()

# Create blocks for rendering
blocks = []
for y in range(world_height):
    for z in range(world_depth):
        for x in range(world_width):
            if world[y][z][x] == 1:
                block = Entity(model='cube', texture='grass.png', position=(x * BLOCK_SIZE, y * BLOCK_SIZE, z * BLOCK_SIZE))
                blocks.append(block)
# Set the player's spawn point
player.position = (5 * BLOCK_SIZE, (world_height + 1) * BLOCK_SIZE, 5 * BLOCK_SIZE)

# Create a skybox
sky = Sky()

# Run the application
app.run()
