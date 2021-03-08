import os
from flask import Flask, render_template, abort, url_for, json, jsonify
from flask import request
import json

app = Flask(__name__)

@app.route("/")
def index():
    useragent = request.headers.get('User-Agent')
    return render_template('index.html', title="page", myuseragent=useragent)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
