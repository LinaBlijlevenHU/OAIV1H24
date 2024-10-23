"""
rijen.py

Hoe zou het resultaat eruit zien voor een meetkundige rij?
"""

def rekenkundige_rij(c, stap, lengte):
    rij = [c]

    for i in range(lengte-1):
        # Berekenen door steeds één stap te nemen
        # We pakken het vorige getal uit de lijst en tellen daar de stap bij op
        rij.append(rij[-1] + stap)

    return rij

def rekenkundige_rij2(c, stap, lengte):
    rij = [c]

    for i in range(lengte-1):
        # Pak de constante en tel er het aantal keer de stap bij op
        # Dus voor het tweede getal tellen we er 2x de stap bij op.
        rij.append(c + stap*i)

    return rij

print(rekenkundige_rij(5, 10, 20))
print(rekenkundige_rij2(5, 10, 20))