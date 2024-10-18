HEX_CHAR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def zet_om(getal):
    # Bereken de eerste digit
    first = getal // 16
    # Bereken het tweede digit van het hexadecimale getal
    second = getal % 16

    # Selecteer uit de lijst en geef terug
    return HEX_CHAR[first] + HEX_CHAR[second]

def kleur_naar_hexadecimaal(r, g, b):
    if (r < 0 or g < 0 or b < 0) or (r > 255 or g > 255 or b > 255):
        print("Gegeven getal buiten range 0-255")
        return None

    # Zet elk individueel getal om naar twee karakters (bijv. 00 of FF)
    new_r, new_g, new_b = zet_om(r), zet_om(g), zet_om(b)

    # Plak 0x aan de rood-waarde, groen-waarde en dan blauw-waarde
    return "0x" + new_r + new_g + new_b

print(kleur_naar_hexadecimaal(0, 0,0))          # Zwart
print(kleur_naar_hexadecimaal(255, 255, 255))   # Wit
print(kleur_naar_hexadecimaal(0, 0, 255))       # Blauw
print(kleur_naar_hexadecimaal(245, 0, 0))       # Rood