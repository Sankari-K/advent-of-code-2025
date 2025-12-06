def get_puzzle_input(directory):
    with open(directory) as f:
        return f.read().split()
    
def get_joltage(bank, digits):
    if digits == 0:
        return ""
    highest = max(bank)
    index = bank.index(max(bank))
    if len(bank) - index >= digits:
        return str(highest) + get_joltage(bank[index + 1:], digits - 1)
    else:
        return get_joltage(bank[:index], digits - (len(bank) - index)) + bank[index:]

def get_total_joltage(banks, digits):
    return sum(map(lambda x: int(get_joltage(x, digits)), banks))

banks = get_puzzle_input(r"./puzzle_input.txt")
print(get_total_joltage(banks, 2))
print(get_total_joltage(banks, 12))