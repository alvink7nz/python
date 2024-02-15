from ursina import *
from perlin_noise import PerlinNoise
from ursina.prefabs.first_person_controller import FirstPersonController

# Create an instance of the Ursina application
app = Ursina()

# Function to generate terrain using Perlin noise
def generate_terrain(width, depth, height_scale, frequency):
    terrain = Entity(model=Mesh(), texture='grass')

    verts = []
    tris = []

    # Create Perlin noise object
    noise_generator = PerlinNoise(octaves=6, seed=2022)

    for z in range(depth):
        for x in range(width):
            # Generate terrain height using Perlin noise
            y = noise_generator([x / frequency, z / frequency]) * height_scale
            verts.append((x, y, z))

    for z in range(depth - 1):
        for x in range(width - 1):
            i = z * width + x
            tris += [i, i + 1, i + width]
            tris += [i + 1, i + width + 1, i + width]

    terrain.model.vertices = verts
    terrain.model.triangles = tris

    # Adjust the terrain's position so it's above the controller's initial position
    terrain.y = -height_scale / 2

    return terrain

# Generate terrain using Perlin noise
terrain = generate_terrain(width=50, depth=50, height_scale=10, frequency=20)

# Create a skybox
sky = Sky()

# Create a FirstPersonController
player = FirstPersonController()

# Set up camera position and rotation to look at the terrain
camera.position = (25, 20, -25)
camera.rotation_x = 45

# Run the application
app.run()
