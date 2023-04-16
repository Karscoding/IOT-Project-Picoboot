from flask import Flask, request, jsonify

app = Flask(__name__)

f = open('temp.txt', 'w')

@app.route('/temperature', methods=['POST'])
def temperature():
    data = request.json
    
    f.write(data)
    
    if data >= 25.0:
        print('Boven 25')
        opdracht = 'On'
        return jsonify(opdracht)
    else:
        print('Onder 25')
        opdracht = 'Off'
        return jsonify(opdracht)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
