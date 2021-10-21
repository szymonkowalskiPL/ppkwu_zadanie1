from flask import Flask, request, jsonify
import hashlib
import zlib
import binascii

app = Flask(__name__)

@app.route('/calculate',  methods=['GET', 'POST'])
def calculateChecksum():
    string = request.args.get('string')
    md5hash = hashlib.md5(string.encode('utf-8')).hexdigest()

    crc32hash = binascii.crc32(string.encode('utf8'))
    
    
    return jsonify(
        md5=md5hash,
        crc32=crc32hash,
    )

app.run()