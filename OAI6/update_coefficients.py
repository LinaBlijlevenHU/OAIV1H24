"""
update_coefficients.py

Voorbeeld van het updaten van de formule voor gradient descent, voor één iteratie en één datapunt.
"""
# Één observatie is één datapunt. In dit geval een student die 36% aanwezig was
# en een 4,3 heeft gehaald.
observatie = (36, 4.3)

# De learning rate bepaalt hoe sterk we corrigeren voor de error. Deze ligt meestal tussen de 0 en 1.
# Een hoge learning rate zorgt dat we de beste oplossing kunnen missen, terwijl een te lage learning rate zorgt
# dat het algoritme langzamer is of niet op de beste oplossing uitkomt.
learning_rate = 0.0001

# Deze coefficienten hebben we geleerd in de eerste iteratie (zie slide 32 in OAI6)
a, b = 0.00041, 0.01189

# Bereken het verschil tussen het verwachte cijfer en het echte cijfer.
error = (a + b * observatie[0]) - observatie[1]

# Stel a (nulpunt/intercept) en b (helling/coefficient) bij.
# Hiermee zouden we een betere fit moeten krijgen.
a = a - error * learning_rate
b = b - observatie[0] * error * learning_rate

# Print de nieuwe formule
print(f"Nieuwe formule is: {a} + {b}x")
