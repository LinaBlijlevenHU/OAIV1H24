"""
api_example.py

Voorbeeld voor het versturen van een verzoek naar een API.
"""
# We gebruiken in veel gevallen de request library. Deze kan verzoeken sturen
# naar elke URL. Soms bieden API's ook wel hun eigen libraries met handige code aan.
import requests

# In dit geval gebruiken we even de Rick & Morty API, die geen authenticatie nodig heeft met
# een API key. Als we deze wel hadden, zouden we deze aan de string moeten plakken!
url = "https://rickandmortyapi.com/api/character/108"

# Met een HTTP GET verzoek, ingebouwd in requests.get, vragen we om informatie
# via een internetverbinding. In dit geval over karakter met ID 108 van Rick & Morty.
response = requests.get(url)

# Als alles goed is gegaan, krijgen we statuscode 200OK.
# Zie ook: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code == 200:
    # Als we inderdaad een OK response krijgen, kunnen we de informatie van de
    # API omzetten naar JSON en het resultaat printen.
    character = response.json()
    print("Received the following info from API:", character)

    # We kunnen nu ook losse eigenschappen selecteren, op dezelfde manier
    # als een standaard python dictionary.
    print(f"{character['name']} is een {character['species']} karakter in Rick & Morty.")
else:
    # Er is iets fout gegaan. Hopelijk kan de error code ons vertellen wat!
    print("Failed to get text. Status code:", response.status_code)
