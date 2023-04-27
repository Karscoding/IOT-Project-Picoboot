from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/temperature", methods=["POST"])
def temperature():
    data = request.json

    f = open('./Texts/temp.txt', 'w')
    printedData = round(float(data), 2)
    f.write(str(printedData))
    f.close()
    
    if data>25:
        opdracht='BAAN'
        return jsonify(opdracht)  
    else:
        opdracht='HK'
        return jsonify(opdracht)

@app.route("/afstand", methods=["POST"])
def afstand():
    data=request.json

    if data==0:
        f = open('./Texts/afstand.txt', 'w')
        f.write("Afstand groot, Niks aan de hand")
        f.close()
        return ""
    elif data==1:
        f = open('./Texts/afstand.txt', 'w')
        f.write("Afstand klein, schuif omhoog!")
        f.close()
        return ""
    else:
        print("fout")
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