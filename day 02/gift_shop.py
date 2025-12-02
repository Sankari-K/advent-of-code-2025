from functools import reduce

def get_puzzle_input(directory):
    with open(directory) as f:
        return list(map(lambda x: list(map(int, x.split("-"))), f.read().split(",")))

def get_products(product_ranges):
    return reduce(lambda x, y: x + y, list(map(lambda x: list(range(x[0], x[1] + 1)), product_ranges)))

def get_factors(number):
    return list(filter(lambda x: number % x == 0, range(2, number + 1)))

def sum_invalid_products(products, only_repeated_twice=False):
    return sum(map(lambda x: get_invalid(str(x), [2] if only_repeated_twice else get_factors(len(str(x)))), products))

def get_invalid(product, factors):
    for factor in factors:
        first_part = product[:len(product) // factor]
        for multiplier in range(1, factor):
            if product[multiplier * len(product) // factor: (multiplier + 1) * len(product) // factor] != first_part:
                break
        else:
            return int(product)
    return 0 

products = get_products(get_puzzle_input(r"./puzzle_input.txt"))

print(sum_invalid_products(products, only_repeated_twice=True)) # part a
print(sum_invalid_products(products)) # part b