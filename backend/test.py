import Main
from Question import Question
from Game import Game

def generateQuestionTest():
    #response = main.generateQuestions(1, "cyprus")
    #print(response)

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

    newGame = Game("cyprus") 
    for question in response:
        newQuestion = Question(question["question"], question["correct_answer"], question["incorrect_answers"])
        newGame.addQuestion(newQuestion)

    for question in newGame.getQuestions():
        print(question.getQuestion())

if __name__ == "__main__":
    generateQuestionTest()