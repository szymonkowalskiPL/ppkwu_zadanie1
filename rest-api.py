from flask import Flask, request

app = Flask(__name__)

@app.route('/calculate',  methods=['GET', 'POST'])
def calculateChecksum():
    string = request.args.get('string')
    return 'your string to hash: '.string

app.run()