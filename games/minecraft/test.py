from ursina import *

class Minecraft(Ursina):
    def __init__(self):
        super().__init__()

        self.block_size = 1
        self.chunk_size = (8, 8, 8)  # Define the size of the chunk (X, Y, Z)

        # Generate the chunk and mesh
        self.mesh = Mesh()
        self.generate_chunk()
        self.chunk_entity = Entity(
            model=self.mesh,
            texture='white_cube',  # Apply a simple texture
            collider='mesh',       # Add collision
        )

    def generate_chunk(self):
        vertices = []
        triangles = []
        colors = []
        uv_map = []

        # Define cube vertices relative to a center (0, 0, 0)
        cube_vertices = [
            Vec3(-0.5, -0.5, -0.5), Vec3(0.5, -0.5, -0.5),
            Vec3(0.5, 0.5, -0.5), Vec3(-0.5, 0.5, -0.5),  # Back face
            Vec3(-0.5, -0.5, 0.5), Vec3(0.5, -0.5, 0.5),
            Vec3(0.5, 0.5, 0.5), Vec3(-0.5, 0.5, 0.5),    # Front face
        ]

        # Define cube triangles (faces) using vertex indices
        cube_triangles = [
            (0, 1, 2), (0, 2, 3),  # Back face
            (4, 5, 6), (4, 6, 7),  # Front face
            (0, 4, 7), (0, 7, 3),  # Left face
            (1, 5, 6), (1, 6, 2),  # Right face
            (3, 2, 6), (3, 6, 7),  # Top face
            (0, 1, 5), (0, 5, 4),  # Bottom face
        ]

        # Generate blocks for the chunk
        for x in range(self.chunk_size[0]):
            for y in range(self.chunk_size[1]):
                for z in range(self.chunk_size[2]):
                    # Create a cube at (x, y, z)
                    offset = Vec3(x, y, z) * self.block_size
                    cube_index_offset = len(vertices)

                    # Add vertices, triangles, and colors for each cube
                    vertices.extend([v + offset for v in cube_vertices])
                    triangles.extend([(a + cube_index_offset, b + cube_index_offset, c + cube_index_offset) for a, b, c in cube_triangles])
                    colors.extend([color.random_color() for _ in range(len(cube_vertices))])

        # Assign data to the mesh
        self.mesh.vertices = vertices
        self.mesh.triangles = triangles
        self.mesh.colors = colors
        self.mesh.generate()

    def input(self, key):
        # Example interaction: Delete a block when clicking
        if self.chunk_entity.hovered and key == 'left mouse down':
            hit_info = mouse.world_point
            print(f'Clicked at {hit_info}')  # Can be used for block selection

    def update(self):
        # Add any updates like interaction or dynamic chunk management
        pass


if __name__ == '__main__':
    minecraft_game = Minecraft()
    minecraft_game.run()
