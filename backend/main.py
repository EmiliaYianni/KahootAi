from flask import Flask, request
app = Flask(__name__)
import openai
from Game import Game
from Player import Player
from Question import Question

#TODO move key
#openai.api_key = ""
client = openai.OpenAI(api_key="")

games = {}

# Create new game and add generated questions
@app.route('/generateQuiz', methods=['POST'])
def generateQuiz():
    data = request.get_json()
    topic = data.get("topic")

    newGame = Game(topic) 
    games[newGame.getGameCode()] = newGame
    
    response = [
        {
            "question": "What is the capital city of Cyprus?",
            "correct_answer": "Nicosia",
            "incorrect_answers": ["Limassol", "Paphos", "Larnaca"]
        },
        {
            "question": "Which goddess is said to have been born near Cyprus according to Greek mythology?",
            "correct_answer": "Aphrodite",
            "incorrect_answers": ["Athena", "Hera", "Demeter"]
        },
        {
            "question": "In which year did Cyprus gain independence from British rule?",
            "correct_answer": "1960",
            "incorrect_answers": ["1950", "1974", "1990"]
        },
        {
            "question": "Which sea surrounds Cyprus?",
            "correct_answer": "The Mediterranean Sea",
            "incorrect_answers": ["The Aegean Sea", "The Black Sea", "The Adriatic Sea"]
        },
        {
            "question": "Which mountain range runs through Cyprus?",
            "correct_answer": "Troodos Mountains",
            "incorrect_answers": ["Alps", "Pyrenees", "Carpathians"]
        }
    ]
    for question in response:
        newQuestion = Question(question["question"], question["correct_answer"], question["incorrect_answers"])
        newGame.addQuestion(newQuestion)

    return newGame.getGameCode()

# Replace one question in question list
@app.route('/replaceQuestion', methods=['POST'])
def replaceQuestion():
    data = request.get_json()
    oldQuestion = data.get("oldQuestion")
    gameCode = data.get("gameCode")

    game = games.get(gameCode)
    response = generateQuestions(1, game.getTopic())
    newQuestion = Question(response["question"], response["correct_answer"], response["incorrect_answers"])
    game.replaceQuestion = (oldQuestion, newQuestion)

    return newQuestion

# Add player to a game if correct code is given
@app.route('/joinGame', methods=['POST'])
def joinGame():
    data = request.get_json()
    gameCode = data.get("gameCode")
    playerName = data.get("playerName")

    if gameCode in games:
        games[gameCode].addPlayer(Player(playerName));
        return "Game joined!", 200
        
    return "Game not available!", 400

# Generate n quiz questions on a topic
def generateQuestions(n, topic):
    messages = [
        {"role": "system", "content": "You are an assistant that generates quiz questions"},
        {"role": "user", "content": f"Generate {n} on the topic {topic}. Return in json format with question, one correct answer, and three incorrect answers"},
    ]
#completion = openai.ChatCompletion.create()
    try:
        completion = client.chat.completions.create(
            model = "???", # TODO
            messages = messages,
        )
        response = completion.choices[0].message.content
    except openai.RateLimitError as e:
        print("Quota exceeded:", e)
        response =""

    return response

# submit and check answer, update and get scores

if __name__ == "__main__":
    app.run()