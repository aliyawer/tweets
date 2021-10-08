#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def counter():
    return "A massage from counter function!"

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
