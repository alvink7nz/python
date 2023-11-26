from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController(position=(0, 3, 0))
Sky()

boxes = []
for i in range(-10, 10):
    for x in range(-10, 10):
        box = Entity(color=color.green, model='cube', position=(x, 0, i))
        boxes.append(box)
for i in range(-10, 10):
    for x in range(-10, 10):
        box = Entity(color=color.brown, model='cube', position=(x, -1, i))
        boxes.append(box)
for i in range(-10, 10):
    for x in range(-10, 10):
        box = Entity(color=color.brown, model='cube', position=(x, -2, i))
        boxes.append(box)
for j in range(0, -5, -1):
    for i in range(-10, 10):
        for x in range(-10, 10):
            if j < -2:
                box = Entity(color=color.gray, model='cube', position=(x, j, i))
                boxes.append(box)
def input(key):
    for box in boxes:
        if key == "1":
            useditem = color.green
        if key == "2":
            useditem = color.brown
        if key == "3":
            useditem = color.gray
        if box.hovered:
            if key == "left mouse down":
                new = Entity(color=useditem, model='cube', position=box.position + mouse.normal, parent=scene, origin_y=0.5)
                boxes.append(new)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)
app.run()