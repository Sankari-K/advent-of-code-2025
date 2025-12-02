from functools import reduce
from itertools import accumulate

DIRECTIONS = {"L": -1, "R": 1}

def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.read().split()
    return list(map(lambda x: (x[0], int(x[1:])), lines))

def get_expanded_rotation(rotation):
    return [(rotation[0], 1)] * rotation[1]

def get_position(current_position, rotation):
    return (current_position + DIRECTIONS[rotation[0]] * rotation[1]) % 100

def get_positions(current_position, rotations):
    return accumulate(rotations, get_position, initial=current_position)
    
def get_position_frequency(target_position, current_position, rotations):  
    return sum(map(lambda x: x == target_position, get_positions(current_position, rotations)))    

rotations = get_puzzle_input(r"./puzzle_input.txt")
expanded_rotations = reduce(lambda x, y: x + y, map(get_expanded_rotation, rotations))

print(get_position_frequency(0, 50, rotations)) # part a
print(get_position_frequency(0, 50, expanded_rotations)) # part b



# rotations = [r1, r2, r3]
# x = f(x, r1) => x = f(f(x, r1), r2) 

# r = [1, 2, 3, 4, 5]
# def f(a, b):
#     return a * b
# a = 1
# [f(a, r[0]), f(f(a, r[0]), r[1])]
 