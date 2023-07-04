#Dit bestand doet posts naar de server zoals een ESP zou doen, Ik heb geen zin om mijn ESP aan te sluiten :) - Kars
import requests
import json
import config

url = f"http://localhost:5000/temperature"
gurl= f"http://localhost:5000/get"
furl= f"http://localhost:5000/log"
auth = ('TeamH1')
temp = 39.250
tijd= "04 July 2023 17:00"
requests.post(url, json=(temp,auth))
requests.post(gurl, json=auth)
requests.post(furl, json=(tijd,auth))