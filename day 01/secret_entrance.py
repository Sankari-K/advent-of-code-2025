from functools import reduce 

def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.read().split()
    return list(map(lambda x: (x[0], int(x[1:])), lines))

def get_expanded_rotation(rotation):
    return [(rotation[0], 1)] * rotation[1]

def get_position(current_position, rotation):
    match rotation[0]:
        case "L":
            return (current_position - rotation[1]) % 100
        case "R":
            return (current_position + rotation[1]) % 100

def get_position_frequency(target_position, current_position, rotations):
    frequency = 0
    for rotation in rotations:
        current_position = get_position(current_position, rotation)
        if current_position == target_position:
            frequency += 1
    return frequency
    # return sum(map(lambda x, y: get_position(x, y) == target_position, rotations))    

rotations = get_puzzle_input(r"./puzzle_input.txt")
print(get_position_frequency(0, 50, rotations))

expanded_rotations = reduce(lambda x, y: x + y, map(get_expanded_rotation, rotations))
print(get_position_frequency(0, 50, expanded_rotations))