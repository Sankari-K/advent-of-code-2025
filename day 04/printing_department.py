from collections import defaultdict

DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def get_puzzle_input(directory):
    with open(directory) as f:
        puzzle_input = f.read().split()
        grid = defaultdict(str)
        for x, row in enumerate(puzzle_input):
            for y, item in enumerate(row):
                grid[x, y] = item
        return len(puzzle_input), len(puzzle_input[0]), grid

def check_accessibility(x, y, grid):
    return sum(map(lambda d: 1 if grid[x + d[0], y + d[1]] == "@" else 0, DIRECTIONS))

def get_accessible_rolls(grid, remove_rolls=False):
    total_accessible_rolls = 0
    condition = True
    while condition:
        accessible_rolls = 0
        for x in range(X_LIMIT):
            for y in range(Y_LIMIT):
                if grid[x, y] == "@" and check_accessibility(x, y, grid) < 4:
                    accessible_rolls += 1
                    if remove_rolls: grid[x, y] = "."
        if not remove_rolls:
            return accessible_rolls
        condition = accessible_rolls != 0
        total_accessible_rolls += accessible_rolls
    return total_accessible_rolls

X_LIMIT, Y_LIMIT, grid = get_puzzle_input(r"./puzzle_input.txt")
print(get_accessible_rolls(grid))
print(get_accessible_rolls(grid, remove_rolls=True))