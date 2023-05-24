from flask import Flask, request, jsonify
from databasevuller import Temperatuur,Afstand,db,app
import datetime
import random

def generatediepte(current):
    verschil=random(range(-1,1,0.1))
    if (2<(current+verschil)<4):
        return current+verschil
    else:
        generatediepte(current) 

@app.route("/temperature", methods=["POST"])
def temperature():
    data = request.json

    f = open('./Texts/temp.txt', 'w')
    printedData = round(float(data), 2)
    f.write(str(printedData))
    f.close()

    now = datetime.datetime.now()
    tijd=(now.strftime("%A, %B %d %Y %H:%M:%S"))
    with app.app_context():
            if Temperatuur.query.all()==[]:
                id=1
            else:
                highestid = Temperatuur.query.all()
                id=(highestid[-1].id+1)
    db.session.add_all([Temperatuur(id,tijd, printedData)])
    db.session.commit()

    if data>25:
        opdracht='BAAN'
        return jsonify(opdracht)  
    else:
        opdracht='HK'
        return jsonify(opdracht)

@app.route("/afstand", methods=["POST"])
def afstand():
    data=request.json

    now = datetime.datetime.now()
    tijd=(now.strftime("%A, %B %d %Y %H:%M:%S"))
    with app.app_context():
            if Afstand.query.all()==[]:
                id=1
            else:
                highestid = Afstand.query.all()
                id=(highestid[-1].id+1)
    db.session.add_all([Afstand(id,tijd, data)])
    db.session.commit()

    diepte=generatediepte(3)
    nap = open('./Texts/nap.txt', 'r').read()
    slib=0.04
    schuifhoogte= diepte +slib
    maxdiepte=4

    if diepte + nap + slib <maxdiepte:
        'schuif omlaag tot diepte + slib'
    else:
        'schuif omhoog tot 0'
     
    if data==0:
        f = open('./Texts/afstand.txt', 'w')
        f.write(f"Afstand groot, Niks aan de hand. Schuifhoogte:{schuifhoogte}")
        f.close()
        return ""
    elif data==1:
        f = open('./Texts/afstand.txt', 'w')
        f.write(f"Afstand klein, schuif omhoog! Schuifhoogte:{schuifhoogte}")
        f.close()
        return ""

    
    
#Krijgt input van placeholder.py en schrijft het in opdracht.txt
@app.route("/input", methods=["POST"])
def input():
    data=request.json
    
    if data=='Bakboord':
        f = open('./Texts/opdracht.txt', 'w')
        f.write("Bakboord")
        f.close()
        return ""
    elif data=='Stuurboord':
        f = open('./Texts/opdracht.txt', 'w')
        f.write("Stuurboord")
        f.close()
        return ""
    else:
        print("Nothing")
        return ""
    
#Returned opdracht
@app.route("/get", methods=["POST"])
def get():
    f = open('./Texts/opdracht.txt', 'r')
    opdracht = f.read()
    return jsonify(opdracht)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)