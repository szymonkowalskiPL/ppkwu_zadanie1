from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate',  methods=['GET', 'POST'])
def calculateChecksum():
    string = request.args.get('string')
    
    return jsonify(string)

app.run()