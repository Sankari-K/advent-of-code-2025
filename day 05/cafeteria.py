from functools import reduce

def get_puzzle_input(directory):
    with open(directory) as f:
        fresh_ranges, ingredients = f.read().split("\n\n")
        # fresh_ranges = list(map(lambda x: (x.split("-")), fresh_ranges.split()))
        fresh_ranges = list(map(lambda x: list(map(int, (x.split("-")))), fresh_ranges.split()))
        ingredients = list(map(int, ingredients.split()))
        return fresh_ranges, ingredients

def get_fresh_ingredients_count(fresh_ranges, ingredients):
    return len(list(filter(lambda ingredient: any(map(lambda fresh_range: fresh_range[0] <= ingredient <= fresh_range[1], fresh_ranges)), ingredients)))

fresh_ranges, ingredients= get_puzzle_input(r"./puzzle_input.txt")
print(get_fresh_ingredients_count(fresh_ranges, ingredients))