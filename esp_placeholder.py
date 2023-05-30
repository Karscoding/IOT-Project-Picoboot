#Dit bestand doet posts naar de server zoals een ESP zou doen, Ik heb geen zin om mijn ESP aan te sluiten :) - Kars
import requests
import json
import config

url = f"http://localhost:5000/temperature"

temp = 39.250
requests.post(url, json=temp)