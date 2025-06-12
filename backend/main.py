from flask import Flask, request, jsonify
app = Flask(__name__)
import json
import Game

games = []

@app.route('/generateQuiz', methods=['POST'])
def generateQuiz():
    newGame = Game() 
    # create questions
    newGame.addQuestions()
    games.append(newGame)
    return newGame.code

@app.route('/joinGame', methods=['POST'], params='gameCode')
def joinGame(gameCode):
    # search the games ARRAY for a matching game with this game code
    pass

if __name__ == "__main__":
    app.run()