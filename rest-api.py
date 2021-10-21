from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/calculate',  methods=['GET', 'POST'])
def calculateChecksum():
    string = request.args.get('string')
    md5hash = hashlib.md5(string.encode('utf-8')).hexdigest()
    return jsonify(
        md5=md5hash
    )

app.run()