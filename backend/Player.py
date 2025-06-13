

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score

    def increaseScore(self, increase):
        self.score += increase
