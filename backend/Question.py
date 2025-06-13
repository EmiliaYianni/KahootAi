

class Question:
    def __init__(self, question, correctAnswer, incorrectAnswers):
        self.question = question
        self.correctAnswer = correctAnswer
        self.incorrectAnswers = incorrectAnswers

    def getQuestion(self):
        return self.question
        
    def getCorrectAnswer(self):
        return self.correctAnswer
        
    def getIncorrectAnswers(self):
        return self.incorrectAnswers