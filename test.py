from ursina import Entity, Mesh, Ursina
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
def test_mesh():
    flatEntity = Entity(
        model=Mesh(
            vertices=[
                (-0.5, -0.5, 0),
                (0.5, -0.5, 0),
                (0.5, 0.5, 0),
                (-0.5, 0.5, 0),
            ],
            mode='faces',
        ),
        texture="grass.png",
        position=(0, 0, 0),
    )
    app.run()

test_mesh()
