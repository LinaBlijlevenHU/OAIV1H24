"""
lijst_gemiddelde.py

Gemiddelde van >2 getallen.
"""

# Neem alle getallen aan
def gemiddelde(getallen):
    # Bereken de som en de lengte van de lijst
    som = sum(getallen)
    lengte = len(getallen)

    # Bereken het gemiddelde op basis van de som en lengte
    gemiddelde = som / lengte

    # Geef gemiddelde terug
    return gemiddelde

    # OF op 1 regel
    #return sum(getallen)/len(getallen)

getallen = [1, 3, 6, 6, 3, 7, 8]
print(gemiddelde(getallen))