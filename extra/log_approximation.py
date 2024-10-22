"""
log_approximation.py

Example trying to estimate the value of a logarithmic expression.
Challenge: implement a solution for negative numbers too.
"""
# base log(target)
base, target = 3, 7

def approximate_logarithm(base, target):
    """ Try to approximate the value of a POSITIVE logarithmic function """
    if target < 1: raise Exception("Alleen positieve getallen makker")

    # Each number ^0 is 1
    res = 1
    # We start with the base number to the power of 0
    currpower = 0

    while target > res:
        currpower += 1
        res *= base

    return currpower-1, currpower

# laagste en hoogste macht waar de target tussen kan liggen
lower, upper = approximate_logarithm(base, target)
print(f"{target} is between {base}^{lower} and {base}^{upper}")
