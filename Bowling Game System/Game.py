from GameSession import GameSession 
class Game:
    
    def __init__(self):
        self.gameSessions={}
        self.alleys=[1,2,3,4]
    def makeActive(self,alleyNum):
        self.alleys.append(alleyNum)
    def createSession(self, players):
        if len(self.alleys) > 0:
            print("alleys > 0")
            session = GameSession()
            session.setPlayers(players)
            session.setAlley(self.alleys.pop())
            self.gameSessions[session.getId()] = session
            return session.getId()
        else:
            print("All alleys are occupied, please wait for sometime")

    def roll(self, gameId, player, hits):
        self.gameSessions[gameId].makeRoll(player, hits)
    def declareWinner(self,gameId):
        winnerFlag = self.gameSessions[gameId].declareWinner()
        if winnerFlag[0] == False:
            print("No winners for the game yet")
        else:
            
            self.makeActive(winnerFlag[1])
        pass
