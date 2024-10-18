"""
set_demo.py

Demo van sets in python
"""
# Maak een set aan
l = ['a', 'b', 'c', 'c', 'c']
s = {'a', 'b', 'c', 'c', 'c'}

# Print de set
print(s)
print(l)

# Sets mogen geen dubbele items bevatten, dus we kunnen de unieke elementen uit een lijst
# filteren. Dit doen we door de lijst om te zetten naar een set en deze vervolgens weer een lijst te
# maken. Let op: sets hebben geen vaste volgorde.
print(list(set(l)))

# Zit de 'd' erin?
print('d' in s)
print('d' not in s)

# Sets zijn heel handig om te werken met verschillende verzamelingen, met name
# als we ze willen vergelijken.
# https://www.w3schools.com/python/python_sets_join.asp