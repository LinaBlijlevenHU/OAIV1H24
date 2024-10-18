grondtal = 2
exponent = 10

def machtsverheffen(grondtal, exponent):
    # Door te vermenigvuldigen met 1 blijft het resultaat hetzelfde
    res = 1

    # We gaan exponent aantal keer het grondtal vermenigvuldigen
    for i in range(exponent):
        # Vermenigvuldig het huidige resultaat nog een keer met het grondtal
        res *= grondtal

    return res

# Gebruik onze functie om te machtsverheffen
resultaat = machtsverheffen(grondtal, exponent)

# Testen tegen de functie van Python zelf
assert grondtal**exponent == resultaat