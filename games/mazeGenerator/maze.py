import tkinter as tk
import random

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]  # 1 for walls, 0 for paths
        self.start_x, self.start_y = 1, 1  # Start point
        self.end_x, self.end_y = width - 2, height - 2  # End point
        self.visited = set()  # Keep track of visited cells
        self.path_stack = []  # Stack to track the current path

    def is_in_bounds(self, x, y):
        return 0 < x < self.width - 1 and 0 < y < self.height - 1

    def generate(self):
        # Start carving from the start point
        self.maze = [[1 for _ in range(self.width)] for _ in range(self.height)]
        self.maze[self.start_y][self.start_x] = 0
        self.visited.add((self.start_x, self.start_y))
        self.path_stack.append((self.start_x, self.start_y))

        while self.path_stack:
            # Current position
            x, y = self.path_stack[-1]

            # Find all unvisited neighbors
            neighbors = []
            for nx, ny in [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]:
                if self.is_in_bounds(nx, ny) and (nx, ny) not in self.visited:
                    neighbors.append((nx, ny))

            if neighbors:
                # Choose a random unvisited neighbor
                nx, ny = random.choice(neighbors)
                self.visited.add((nx, ny))
                self.path_stack.append((nx, ny))

                # Carve the wall between current cell and chosen neighbor
                self.maze[(y + ny) // 2][(x + nx) // 2] = 0
                self.maze[ny][nx] = 0
            else:
                # Backtrack if no neighbors are available
                self.path_stack.pop()

        return self.add_boundary()

    def add_boundary(self):
        bordered_maze = []
        for row in self.maze:
            bordered_maze.append([1] + row[1:-1] + [1])  # Add exactly 1 wall to the left and right
        bordered_maze.insert(0, [1] * len(bordered_maze[0]))  # Add 1 row of walls at the top
        bordered_maze.append([1] * len(bordered_maze[0]))  # Add 1 row of walls at the bottom
        return bordered_maze

    def solve_maze(self):
        # BFS to solve the maze
        queue = [(self.start_x, self.start_y)]
        visited = set()
        came_from = {}

        while queue:
            x, y = queue.pop(0)
            if (x, y) == (self.end_x, self.end_y):
                break

            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if self.is_in_bounds(nx, ny) and self.maze[ny][nx] == 0 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    came_from[(nx, ny)] = (x, y)

        # Reconstruct path
        path = []
        current = (self.end_x, self.end_y)
        while current != (self.start_x, self.start_y):
            path.append(current)
            current = came_from.get(current)
            if current is None:
                break
        path.reverse()
        return path

class MazeApp:
    def __init__(self, root, width, height, cell_size, canvas:tk.Canvas):
        # Increase height relative to width for a taller maze
        self.root = root
        self.width = width
        self.height = height  # Add extra rows for height
        self.cell_size = cell_size
        self.canvas = canvas

        # Adjust canvas height dynamically based on new maze height

        # Generate the maze
        self.maze_gen = MazeGenerator(self.width, self.height)
        self.maze = self.maze_gen.generate()
        self.path = []

        # Solve button

        # Draw the maze
        self.draw_maze()

    def draw_maze(self):
        """Draw the maze on the canvas."""
        self.canvas.delete("all")
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                color = "black" if cell == 1 else "white"
                self.canvas.create_rectangle(
                    x * self.cell_size,
                    (y-1) * self.cell_size,
                    (x + 1) * self.cell_size,
                    y * self.cell_size,
                    fill=color,
                    outline=""
                )

    def animate_solution(self, path):
        """Animate the solution path."""
        if not path:
            return

        def draw_step(index):
            if index < len(path):
                x, y = path[index]
                self.canvas.create_rectangle(
                    x * self.cell_size,
                    y * self.cell_size,
                    (x + 1) * self.cell_size,
                    (y + 1) * self.cell_size,
                    fill="green",
                    outline=""
                )
                self.root.after(20, draw_step, index + 1)  # Delay for smooth animation

        draw_step(0)

    def solve_maze(self):
        """Solve the maze and animate the solution."""
        self.path = self.maze_gen.solve_maze()
        self.animate_solution(self.path)

    def createNewMaze(self):
        self.canvas.delete("all")
        app = MazeApp(self.root, 45, 45, 10, self.canvas)

# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maze Solver")

    maze_width = 45  # Maze width
    maze_height = 45  # Maze height
    cell_size = 10  # Size of each cell in pixels
    canvas = tk.Canvas(root, width=maze_width * cell_size, height=maze_height * cell_size)
    canvas.pack()
    app = MazeApp(root, maze_width, maze_height, cell_size, canvas)
    solve_button = tk.Button(root, text="Solve Maze", command=app.solve_maze)
    solve_button.pack(side="bottom")
    newMazeButton = tk.Button(root, text="New Maze", command=app.createNewMaze)
    newMazeButton.pack(side="bottom")
    root.mainloop()
