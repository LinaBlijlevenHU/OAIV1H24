"""
gemiddelde_functie_van_pseudocode.py

Gemiddelde-functie zoals we kunnen afleiden uit pseudocode gegeven in de slides.
"""
# 1. Ontvang getallen a en b
def gemiddelde(a, b):
    # 2. Bereken de som
    som = a + b

    # 3. Bereken het gemiddelde
    gemiddelde = som / 2

    # 4. Geef terug
    return gemiddelde

print(gemiddelde(10, 20))

# Hoe ziet deze functie eruit als je meer dan twee getallen hebt? (zie lijst_gemiddelde.py)