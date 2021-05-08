from flask import Flask
from flask_cors import CORS
from flask import render_template, jsonify, request



app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/move', methods=['GET'])
def move():
    return ({'body':"hello"})


app.run('127.0.0.1', 5000)