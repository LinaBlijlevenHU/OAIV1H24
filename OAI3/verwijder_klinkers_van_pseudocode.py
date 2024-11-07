"""
verwijder_klinkers_van_pseudocode.py

Deze code richt zich op het vertalen van pseudocode naar Python.
"""

# De klinkers slaan we op in een globale variabele, zo kunnen we deze overal in het
# programma gebruiken. We geven dit ook aan met de naam in hoofdletters.
KLINKERS = "aeiou"

def is_klinker(letter):
    """ Hulpfunctie die we kunnen inzetten om te checken of iets een klinker is. """
    # Eigenlijk moeten we hier ook nog even checken voor uppercase klinkers
    return letter in KLINKERS

# 1. ontvang tekst t (vertaald naar functiedefinitie)
def verwijder_klinkers(t):
    """ Doel: verwijder alle klinkers uit een stuk tekst """
    # Nieuwe string om de medeklinkers in te bewaren (nodig voor stap 3 zo)
    n = ""

    # 2. herhaal stap 3. voor elke letter l in t (herhaal betekent vaak loop)
    for l in t:
        # 3. als l geen klinker is, voeg deze toe aan de nieuwe tekst n
        # Deze regel heeft een if-statement (als) nodig en bewerkt daarnaast ook n!
        if not is_klinker(l):
            n += l

    # 4. geef n terug
    # "Geef terug" verwijst vrijwel altijd naar een return-statement als we functies schrijven :)
    return n

# Voor de volledigheid testen we even of de hulperfunctie
# het juiste antwoord geeft. (eigenlijk is dit testcode en kan dit beter los!)
assert is_klinker('a')              # Verzeker dat a een klinker is
assert not is_klinker('z')          # Verzeker dat z geen klinker is

# Nu kunnen we het geheel testen
t = "Ik ben een tekstje met klinkers enzo uuuuu"
print(verwijder_klinkers(t))