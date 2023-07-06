#Dit bestand doet posts naar de server zoals een ESP zou doen, Ik heb geen zin om mijn ESP aan te sluiten :) - Kars
import requests
import json
import config

url = f"http://localhost:5000/temperature"
furl= f"http://localhost:5000/log"
nurl= f"http://localhost:5000/nood"
gurl= f"http://localhost:5000/get"
auth = "TeamH1"
verkeerde_auth ="Team1"
temp = 39.250
tijd= "04 July 2023 17:00"
reason = 'Ingelogd'
# url="http://192.168.68.72:5000/get"
# try:
#     requests.post(url, json=(auth))
# except requests.exceptions.RequestException as e:
#     print("dit is hem")
# except :
#     print("verkeerde IP")

# lijst met foutive post requests

requests.post(url, json=(temp,verkeerde_auth))
requests.post(url, json=temp)
requests.post(furl , json=(f"{tijd}",reason))
requests.post(furl , json=(f"{tijd}",verkeerde_auth,reason))
requests.post(nurl , json=f"{tijd}")
requests.post(nurl , json=(f"{tijd}",verkeerde_auth))
requests.post(gurl, json=verkeerde_auth)
requests.post(gurl, json=None)
