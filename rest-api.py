from flask import Flask

app = Flask(__name__)

@app.route('/calculate',  methods=['GET', 'POST'])
def calculateChecksum():
    return 'test'

app.run()