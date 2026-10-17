import random


class MazeGenerator:
    EMPTY = 0
    WALL = 1
    NORTH, SOUTH, EAST, WEST = "n", "s", "e", "w"

    def __init__(self, width: int, height: int):
        if width < 3 or height < 3 or width % 2 == 0 or height % 2 == 0:
            raise ValueError("width and height must be odd numbers of at least 3")

        self.width = width
        self.height = height
        self.maze: dict[tuple[int, int], int] = {}
        self.has_visited: list[tuple[int, int]] = []

    def generate(self) -> dict[tuple[int, int], int]:
        """Create and return a new maze."""
        self.maze.clear()
        self.has_visited = [(1, 1)]
        self._initial_maze()
        self._visit(1, 1)
        return self.maze

    def _initial_maze(self) -> None:
        for x in range(self.height):
            for y in range(self.width):
                self.maze[(x, y)] = self.WALL

    def _visit(self, x: int, y: int) -> None:
        self.maze[(x, y)] = self.EMPTY
        while True:
            unvisited_neighbors = []
            # NORTH: row decreases
            if x > 1 and (x - 2, y) not in self.has_visited:
                unvisited_neighbors.append(self.NORTH)

            # SOUTH: row increases
            if x < self.height - 2 and (x + 2, y) not in self.has_visited:
                unvisited_neighbors.append(self.SOUTH)

            # WEST: column decreases
            if y > 1 and (x, y - 2) not in self.has_visited:
                unvisited_neighbors.append(self.WEST)

            # EAST: column increases
            if y < self.width - 2 and (x, y + 2) not in self.has_visited:
                unvisited_neighbors.append(self.EAST)

            if not unvisited_neighbors:
                return

            next_intersection = random.choice(unvisited_neighbors)
            if next_intersection == self.NORTH:
                next_x, next_y = x - 2, y
                self.maze[(x - 1, y)] = self.EMPTY
            elif next_intersection == self.SOUTH:
                next_x, next_y = x + 2, y
                self.maze[(x + 1, y)] = self.EMPTY
            elif next_intersection == self.WEST:
                next_x, next_y = x, y - 2
                self.maze[(x, y - 1)] = self.EMPTY
            else:
                next_x, next_y = x, y + 2
                self.maze[(x, y + 1)] = self.EMPTY

            self.has_visited.append((next_x, next_y))
            self._visit(next_x, next_y)


if __name__ == "__main__":
    WIDTH, HEIGHT = 31, 31
    generator = MazeGenerator(31, 31)
    maze = generator.generate()
    for x in range(HEIGHT):
        for y in range(WIDTH):
            if maze[(x, y)] == MazeGenerator.EMPTY:
                print("  ", end="")
            else:
                print("██", end="")
        print()