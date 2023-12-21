from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000))
treeX = random.randint(-10, 10)
treeZ = random.randint(-10, 10)
world_width = 20
world_depth = 20
selectedBlock = "dirt.png"
app = Ursina(title="minecraft")
player = FirstPersonController(
    mouse_sensesivity=Vec2(100, 100),
    position=(0, 5, 0),
    speed=5
)
class Mob(Entity):
    def __init__(self, position=(0, 0, 0), scale=1, texture="slime.png"):
        super().__init__(
            model="cube",
            texture=texture,
            collider="box",
            scale=scale,
            position=position,
        )
mobs = []
def create_mobs(height=1):
    mob_position = (random.uniform(-10, 10), height, random.uniform(-10, 10))
    mob = Mob(position=mob_position, scale=1)
    mobs.append(mob)

def Block(position, blocktype):
    texture_path = blocktype
    texture = load_texture(texture_path)
    return Entity(model="cube", position=position, scale=1, origin_y=-0.5, texture=texture, collider="box")
def create_tree(position, trunk_height=5, leaves_height=3):
    # Create trunk
    for k in range(trunk_height):
        Block((position[0], position[1] + k, position[2]), "wood.png")

    # Create leaves
    leaves_radius = 2
    for i in range(-leaves_radius, leaves_radius + 1):
        for j in range(-leaves_radius, leaves_radius + 1):
            for k in range(1, leaves_height + 1):
                if i**2 + j**2 + (k - 1)**2 <= leaves_radius**2:
                    Block((position[0] + i, position[1] + trunk_height + k - 1, position[2] + j), "leaf.png")
def create_mini_drop(position, block_type):
    # Create a mini drop entity at the given position
    mini_drop = Entity(model='cube', position=position, scale=0.5, collider='box', texture=block_type)
    mini_drops.append(mini_drop)

mini_drops = []
treeSeed = random.uniform(0, 0.05)
treeLeaves = random.randint(1, 3)
if treeLeaves == 1:
    treeTrunk = 2
if treeLeaves == 2:
    treeTrunk = 3
if treeLeaves == 3:
    treeTrunk = 5
min_height = -5
for i in range(-10, 10):
    for j in range(-10, 10):
        height = noise([i * 0.02, j * 0.02])
        height = math.floor(height * 7.5)
        for k in range(height, min_height - 1, -1):
            if k == min_height:
                Block((i, k - min_height, j), "bedrock.png")
            elif k == height:
                Block((i, k - min_height, j), "grass.png")
                if random.random() < treeSeed:
                    create_tree(position=(i, k - min_height + 1, j), trunk_height=treeTrunk,leaves_height=treeLeaves)
                create_mobs(height+1)
            elif k > 2:
                Block((i, k - min_height, j), "stone.png")
            else:
                Block((i, k - min_height, j), "dirt.png")
def input(key):
    global selectedBlock
    if key == "1":
        selectedBlock = "grass.png"
    if key == "2":
        selectedBlock = "dirt.png"
    if key == "3":
        selectedBlock = "stone.png"
    if key == "4":
        selectedBlock = "bedrock.png"
    if key == "5":
        selectedBlock = "wood.png"
    if key == "6":
        selectedBlock = "leaf.png"
    if key == "left mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=3)
        if hit_info.hit:
            Block(hit_info.entity.position + hit_info.normal, selectedBlock)
    if key == "right mouse down" and mouse.hovered_entity:
        # Check if the player is clicking on a block
        if mouse.hovered_entity.texture:
            block_type = mouse.hovered_entity.texture

            # Store the position before destroying the block
            block_position = mouse.hovered_entity.position

            # Destroy the block
            destroy(mouse.hovered_entity)

            # Create a mini drop at the stored position
            create_mini_drop(block_position, block_type)

def jump(object):
    object.jump_height = 1
    object.gravity = 1.6
    object.grounded = True
    object.speed = 3
    jumpChance = random.randint(0,3)
    if jumpChance == 0 and object.grounded:
        random_direction = Vec3(random.uniform(-1, 1), 1, random.uniform(-1, 1)).normalized()
        object.y += 0.1  # Lift the player slightly to start the jump
        object.position += random_direction * object.jump_height
        object.grounded = False  # Set grounded to False to prevent double jumps

    # Apply gravity to the player
    object.y -= object.gravity * time.dt

    # Check if the player has reached the ground
    object.x = clamp(object.x, -world_width / 2, world_width / 2)
    object.z = clamp(object.z, -world_depth / 2, world_depth / 2)
    height_info = raycast(object.position, Vec3(0, -1, 0), distance=2, ignore=[object])

    # Check if random_jump_mob is below the ground
    if height_info.hit and height_info.entity.y > object.y:
        object.y = object.entity.y
        object.grounded = True

def update():
    global mini_drops

    # Iterate over mini drops in reverse order to avoid issues with modifying the list during iteration
    for mini_drop in reversed(mini_drops):
        # Check if the player is close enough to collect the mini drop
        if distance(player.position, mini_drop.position) < 1.5:
            # Collect the mini drop
            mini_drops.remove(mini_drop)
            destroy(mini_drop)
    
    for mob in mobs:
        jump(mob)
Sky()
app.run()