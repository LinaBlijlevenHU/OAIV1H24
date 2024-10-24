"""
reeksen.py
"""

def fibonacci(length) -> list:
    """
    Determine a fibonacci sequence of a given length.

    :param length:  Desired list length
    :return:        List of fibonacci sequence
    """
    fib = [0, 1]

    # We hebben al twee getallen, de rest gaan we nu toevoegen.
    for i in range(length-2):
        # Vraag vorige twee getallen op
        previous, previouser = fib[-1], fib[-2]

        # Nieuwe getal voor de reeks
        fib.append(previous + previouser)

    return fib

length = 400
fib = fibonacci(length)
print(f"First {length} numbers of the Fibonacci sequence: \n"
      f"{fib}")

def powersof2(length) -> list:
    """
    Determine powers of two

    :param length:  Gewenste lengte van de lijst
    :return:
    """

    # Alternatief met list comprehension
    #pows = [2 ** i for i in range(1, length + 1)]

    pows = []

    for i in range(1, length+1):
        pows.append(2**i)

    return pows


base = 2
pows = powersof2(length)
print(f"First {length} powers of {base}:\n"
      f"{pows}")