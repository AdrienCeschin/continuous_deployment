from flask import Flask, jsonify
import hashlib

app = Flask(__name__)

@app.route('/md5/<param>', methods=['GET'])
def hashMd5(param):
    hashedText = hashlib.md5(param.encode())
    return {"hash":"md5","cleartext": param,"hashedtext": hashedText.hexdigest()}

@app.route('/sha256/<param>', methods=['GET'])
def hashSha256(param):
    hashedText = hashlib.sha256(param.encode())
    return {"hash":"sha256","cleartext": param,"hashedtext": hashedText.hexdigest()}

app.run(host='0.0.0.0')