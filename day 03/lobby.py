def get_puzzle_input(directory):
    with open(directory) as f:
        return f.read().split()

# def get_joltage(bank):
#     # find max in string, its index -- then max in string[index + 1:]
#     # if the max is the last digit, find the second max in string and swap
#     maximum = max(bank)
#     index = bank.index(maximum)
#     if index == len(bank) - 1:
#         bank = bank.replace(maximum, "")
#         return int(max(bank) + maximum)
#     else:
#         return int(maximum + max(bank[index + 1:]))

def get_joltage(current, bank, battery_limit):
    if len(current) == battery_limit:
        return int(current)
    if not bank or len(current) + len(bank) < battery_limit:
        return 0
    return max(get_joltage(current + bank[0], bank[1:], battery_limit), get_joltage(current, bank[1:], battery_limit))

def get_total_joltage(banks, battery_limit):
    ans = 0
    for index, bank in enumerate(banks):
        print(index)
        ans += get_joltage("", bank, battery_limit)
    print(ans)
    # return sum(map(lambda x: get_joltage("", x, battery_limit), banks))

banks = get_puzzle_input(r"./puzzle_input.txt")
print(get_total_joltage(banks, 2))
print(get_total_joltage(banks, 12))
