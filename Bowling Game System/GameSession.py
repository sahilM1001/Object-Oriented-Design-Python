class GameSession:
    def __init__(self):
        self.counter = 0
        self.alley = -1
        self.id = self.getUniqueId()
        self.players = []
        print("inside gamesession constructor")
        

    def setPlayers(self, player):
        self.players.extend(player)
        
    
    def setAlley(self,alley):
        self.alley = alley
    
    def getId(self):
        return self.id

    def getUniqueId(self):
        self.counter +=1
        return self.counter
    
    def declareWinner(self):
        maxScore = 0
        winner =None
        for i in self.players:
            if i.getCanPlay():
                print("Player: ", i.getName(), " can still play and current score is: ", i.getScore())
            else:
                if(i.getScore() > maxScore):
                    maxScore = i.getScore()
                    winner = i
        if winner is not None:
            print("Player: ", winner.getName(), " has won the game with score: ", winner.getScore())
            return [True, self.alley]

    def makeRoll(self, player, pins):
        print("self.players: ", self.players)
        for i in self.players:
            if i.getName() == player.getName():
                i.roll(pins) 