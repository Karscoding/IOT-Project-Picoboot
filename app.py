from flask import request, jsonify
from databasevuller import Temperatuur,Afstand,db,app,actielog
import datetime
import random
from translate import translate
current=3

def generatediepte(current):
    verschil=random.randrange(-10,10)
    verschil=verschil/10
    if (current+verschil) >2 and (current+verschil)<4:
        return (current+verschil)
    else:
        return generatediepte(current) 

@app.route("/temperature", methods=["POST"])
def temperature():
    data = request.json

    f = open('./Texts/temp.txt', 'w')
    printedData = round(float(data), 2)
    f.write(str(printedData))
    f.close()


    tijd=translate()
    with app.app_context():
            if Temperatuur.query.all()==[]:
                id=1
            else:
                highestid = Temperatuur.query.all()
                id=(highestid[-1].id+1)
    db.session.add_all([Temperatuur(id,tijd, printedData)])
    db.session.commit()

    diepte=generatediepte(current)
    nap = float(open('./Texts/nap.txt', 'r').read())
    
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

    if diepte + nap + slib < maxdiepte:
        f = open('./Texts/afstand.txt', 'w')
        f.write(f"Schuif omlaag\nDiepte: {schuifhoogte}")
        f.close()
        return ""
    else:
        f = open('./Texts/afstand.txt', 'w')
        f.write(f"Schuif omhoog\n Diepte: {schuifhoogte}")
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
@app.route('/log',methods=["POST"])
def loggen():
    data=request.json
    with app.app_context():
        if actielog.query.all()==[]:
            id=1
        else:
            highestid = actielog.query.all()
            id=(highestid[-1].id+1)
    db.session.add_all([actielog(id,data,"Ingelogd")])
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
    f = open('./Texts/opdracht.txt', 'r')
    opdracht = f.read()
    return jsonify(opdracht)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)