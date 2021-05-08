from flask import Flask
from flask_cors import CORS
from flask import render_template, jsonify, request
import chess


app = Flask(__name__)
CORS(app)

global board

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/start')
def start_game():
    global board
    board = chess.Board()
    return ({'body': board.fen()})

@app.route('/move', methods=['POST'])
def move():
    move = request.get_json()['move']
    


app.run('127.0.0.1', 5000)