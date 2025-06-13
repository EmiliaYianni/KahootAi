import random, string

class Game:
    def __init__(self, topic):
        self.gameCode = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 4))
        self.players = []
        self.questions = [] 
        self.topic = topic

    def getGameCode(self):
        return self.gameCode

    def getPlayers(self):
        return self.players

    def getTopic(self):
        return self.topic
    
    def getQuestions(self):
        return self.questions

    def addQuestion(self, question):
        self.questions.append(question)

    def replaceQuestion(self, oldQuestion, newQuestion):
        for i in range(len(self.questions)):
            if self.questions[i] == oldQuestion:
                self.questions[i] = newQuestion
