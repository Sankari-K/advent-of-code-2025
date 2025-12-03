def get_puzzle_input(directory):
    with open(directory) as f:
        return f.read().split()

def get_joltage(bank):
    # find max in string, its index -- then max in string[index + 1]
    # if the max is the last digit, find the second max in string and swap
    maximum = max(bank)
    index = bank.index(maximum)
    if index == len(bank) - 1:
        bank = bank.replace(maximum, "")
        return int(max(bank) + maximum)
    else:
        return int(maximum + max(bank[index + 1:]))

def get_total_joltage(banks):
    return sum(map(get_joltage, banks))

banks = get_puzzle_input(r"./puzzle_input.txt")
print(get_total_joltage(banks))