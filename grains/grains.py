def square(number):
    if number <1 or number>64:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2**(number-1)


def total():
    total_grains = 0
    for power in range(64):
        total_grains+=2**power
    return total_grains
