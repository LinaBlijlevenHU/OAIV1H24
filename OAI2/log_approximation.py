base, target = 2, 7

def approximate_log(base, target):

    # We implementeren voor nu alleen positieve getallen
    if target < 0:
        raise Exception("Negative numbers are not supported. Please extend this function.")

    # We start with base^0
    power = 0
    res = 1

    # Ga door met vermenigvuldigen tot we boven ons doel uitkomen
    while target > res:
        res *= base
        # We houden de macht even handmatig bij
        power += 1

    # De waarde ligt op/onder deze macht en degene eronder
    return power, power-1

upper, lower = approximate_log(base, target)
print(f"To make {base} grow to {target} the exponent is or is between {lower} and {upper}.")