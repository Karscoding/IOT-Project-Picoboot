# - Flask App - 
#
# Dit bestand is de Flask server die open zal moeten zijn op de achtergrond tijdens het gebruiken van de dashboard.
# Wanneer dit bestand geopend is zal de ESP32 kunnen communiceren met alles.
#
# - Picoboot Team 2023 - 
#


from flask import request, jsonify
from CreateDB import Temperatuur,Afstand,db,app,actielog
from jsonhandler import Writer, Reader
import datetime
import random
import json
from translate import translate
current=3
verwacht_teamnaam = 'TeamH1'

def generatediepte(current):
    verschil=random.randrange(-10,10)
    verschil=verschil/10
    if (current+verschil) >2 and (current+verschil)<4:
        return (current+verschil)
    else:
        return generatediepte(current)
    
@app.route("/temperature", methods=["POST"])
def temperature():
    auth = request.json[1]
    data=request.json[0]

    if (auth==verwacht_teamnaam):
        print("goed")
    elif auth == None:
        print("geen")
    elif auth != verwacht_teamnaam:
        print("verkeerd")
        
    #Function, see Jsonhandler.py
    Writer("Temp", data)
                
    tijd=translate()
    with app.app_context():
            if Temperatuur.query.all()==[]:
                id=1
            else:
                highestid = Temperatuur.query.all()
                id=(highestid[-1].id+1)
    db.session.add_all([Temperatuur(id,tijd, data)])
    db.session.commit()

    diepte=generatediepte(current)
    nap = Reader("NAP")
    nood = Reader("NOOD")
    
    slib=0.04
    schuifhoogte= diepte +slib
    maxdiepte=4

    
    with app.app_context():
            if Afstand.query.all()==[]:
                id=1
            else:
                highestid = Afstand.query.all()
                id=(highestid[-1].id+1)
    db.session.add_all([Afstand(id,tijd, diepte,nap)])
    db.session.commit()

    if nood:
        Writer("InstructionSchuif", "Omhoog")

    elif diepte + float(nap) + slib < maxdiepte:
        Writer("InstructionSchuif", "Omlaag")
        
    else:
        Writer("InstructionSchuif", "Omhoog")
    
    Writer("Diepte", schuifhoogte)
    return ""


@app.route('/log',methods=["POST"])
def loggen():
    auth = request.json[1]
    data=request.json[0]
    reason=request.json[2]

    if (auth==verwacht_teamnaam):
        print("goed")
    elif auth == None:
        print("geen")
        with app.app_context():
            if actielog.query.all()==[]:
                id=1
            else:
                highestid = actielog.query.all()
                id=(highestid[-1].id+1)
            db.session.add_all([actielog(id,data,"geen auth")])
            db.session.commit()
        return""
    elif auth != verwacht_teamnaam:
        print("verkeerd")
        with app.app_context():
            if actielog.query.all()==[]:
                id=1
            else:
                highestid = actielog.query.all()
                id=(highestid[-1].id+1)
            db.session.add_all([actielog(id,data,"verkeerd auth")])
            db.session.commit()
        return""
    with app.app_context():
        if actielog.query.all()==[]:
            id=1
        else:
            highestid = actielog.query.all()
            id=(highestid[-1].id+1)
    db.session.add_all([actielog(id,data,reason)])
    db.session.commit()
    loglijst=[]
    with app.app_context():
        for x in actielog.query.all():
            loglijst.append((x.tijd,x.actions))
            
    return jsonify(loglijst)

@app.route('/nood',methods=["POST"])
def noodstop():
    data=request.json
    with app.app_context():
        if actielog.query.all()==[]:
            id=1
        else:
            highestid = actielog.query.all()
            id=(highestid[-1].id+1)
    db.session.add_all([actielog(id,data,"Noodstop")])
    db.session.commit()
    return ""
     
    
#Returned opdracht
@app.route("/get", methods=["POST"])
def get():
    auth=request.json
    if (auth==verwacht_teamnaam):
        print("goed")
    elif auth == None:
        print("geen")
    elif auth != verwacht_teamnaam:
        print("verkeerd")
    data = {"InstructionAll": Reader("InstructionAll"),
            "InstructionPass": Reader("InstructionPass"),
            "NOOD": Reader("NOOD")}
    return data
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)