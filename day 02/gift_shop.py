from functools import reduce

def get_puzzle_input(directory):
    with open(directory) as f:
        return list(map(lambda x: list(map(int, x.split("-"))), f.read().split(",")))

def get_products(product_ranges):
    return reduce(lambda x, y: x + y, list(map(lambda x: list(range(x[0], x[1] + 1)), product_ranges)))

def sum_invalid_products(products):
    return sum(map(lambda x: get_invalid(str(x)), products))

def get_invalid(product):
    return int(product) if product[:len(str(product)) // 2] == product[len(str(product)) // 2:] else 0

product_ranges = get_puzzle_input(r"./puzzle_input.txt")
print(sum_invalid_products(get_products(product_ranges)))
