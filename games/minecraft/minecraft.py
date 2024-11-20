from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise

# Initialize Ursina app
app = Ursina()

seed = random.randint(-10000, 10000)

noise = PerlinNoise(octaves=3, seed=seed)

player = FirstPersonController()
player.cursor.texture = "cursor.png"

day_color = color.rgb(135, 206, 235)  # Daytime sky color
sunset_color = color.rgb(255, 94, 0)  # Sunset sky color
night_color = color.rgb(0, 0, 50)  # Night sky color

# Create a custom cursor
custom_cursor = Entity(
    parent=camera.ui,
    model='quad',
    texture='cursor.png',  # Initial cursor texture
    scale=0.03
)


blocks = [
    "grass.png",
    "dirt.jpg",
    "stone.jpg",
    "bedrock.png",
    "log.jpg",
    "leaves.png",
    "",
    ""
]
holdingBlock = 0

blockPreview = Entity(
    parent=camera.ui,
    model='cube',
    texture=blocks[holdingBlock],
    scale=0.4,  # Adjust size
    position=(0.8, -0.4, 0),  # Adjust position (right bottom corner)
    rotation=Vec3(40, 35, 30)  # Slight rotation to show 3D effect
)

class Block(Button):
    def __init__(self, texture,position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture=texture,  # You can use 'brick', 'stone', or other textures as well
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=1
        )

    # Method to add and delete blocks on left/right mouse click
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                    if blocks[holdingBlock] != "":
                        block = Block(texture=blocks[holdingBlock], position=self.position + mouse.normal)
            elif key == 'right mouse down':
                if self.texture.name != "bedrock.png":
                    destroy(self)



heightMap = []
for z in range(15):
    row = []
    for x in range(15):
        height = noise([x*0.02, z*0.02])
        height = math.floor(height * 7.5)
        block = Block(texture="grass.png" ,position=(x, height, z))
        block = Block(texture="dirt.jpg", position=(x, height-1, z))
        for y in range(2):
            block = Block(texture="stone.jpg", position=(x, height-y-2, z))
        for y in range(height+4):
            block = Block(texture="bedrock.png", position=(x, height-y-4, z))
        
        row.append(height)
    heightMap.append(row)

sky = Entity(model='sphere', texture='sky_default', scale=1000, double_sided=True)

fps_counter = Text(
    text='FPS: 0',  # Initial text
    position=(-0.8, -0.45),  # Adjust the position (top-left corner)
    origin=(0, 0),
    scale=1,
    color=color.white
)

# Tree generation
def generate_trees(height_map, tree_count=10):
    for _ in range(tree_count):
        x = random.randint(0, 11)
        z = random.randint(0, 11)
        y = height_map[z][x]  # Get the terrain height at (x, z)

        # Only place a tree if the block is at ground level
        if y > -4:  # Avoid water or very low levels
            generate_tree(x, y + 1, z)  # Place the tree above the terrain

def generate_tree(x, y, z):
    # Trunk
    for i in range(3):  # Adjust the trunk height as needed
        Block(position=(x, y + i, z), texture='log.jpg')  # Trunk block (e.g., brick texture)

    # Leaves (pyramid-shaped)
    height = 3  # Height of the pyramid-shaped leaves
    for level in range(height):
        size = height - level - 1  # Decrease size as we go higher
        for dx in range(-size, size + 1):
            for dz in range(-size, size + 1):
                # Only place leaves if not on the corners to make it rounded
                if abs(dx) + abs(dz) <= size:
                    Block(position=(x + dx, y + 3 + level, z + dz), texture='leaves.png')  # Leaf block

generate_trees(heightMap, random.randint(1,4))

def update():
    global holdingBlock
    # Check for number key presses (1-4)
    for i in range(8):  # Adjust the range if you add more block types
        try:
            if held_keys[str(i+1)]:  # Keys are '1', '2', '3', etc.
                if blocks[i] != "":
                    holdingBlock = i
                    blockPreview.texture = blocks[holdingBlock]  # Update block preview texture
        except IndexError:
            pass

    if held_keys["alt"]:
        player.speed = 10
    else:
        player.speed = 5

    fps_counter.text = f'FPS: {int(1 / time.dt)}'


inventory_slots = []
inventory_size = 8  # Number of slots in the inventory
inventory = Entity(
    parent=camera.ui,
    model='quad',
    texture="inventory.png",
    scale=(1, 0.12),
    position=(0, -0.4)
)

for i in range(inventory_size):
    try:
        if blocks[i] != "":
            slot = Entity(
                parent=camera.ui,
                model='quad',
                texture=blocks[i],
                scale=(0.1, 0.1),
                position=(-0.4365 + (i * 0.125), -0.4)
            )
    except IndexError:
        pass
    
    inventory_slots.append(slot)

# Update the texture of the inventory slots
def update_inventory():
    for i in range(inventory_size):
        try:
            inventory_slots[i].texture = blocks[i]  # Update each slot with the correct texture
        except IndexError:
            pass
# Set initial inventory display
update_inventory()

seedNum = Text(
    parent=camera.ui,
    text=f"Seed: {seed}",
    position=(-0.87, 0.47),
    scale=1
)

blockPreviewHere = True

app.run()