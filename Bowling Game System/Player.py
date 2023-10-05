class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.score = 0
        self.MAX_ROLLS_ALLOWED = 23
        self.rolls = [0]*self.MAX_ROLLS_ALLOWED
        self.firstRoll = True
        self.frameIndex = 0
        self.canPlay = True
        self.currentRoll = 0


    def getName(self):
        return self.name
    def getScore(self):
        return self.score
    def getCanPlay(self):
        return self.canPlay
    
    def isStrike(self):
        return (self.firstRoll and self.rolls[self.frameIndex] == 10)
        
    def isSpare(self):
        return (self.rolls[self.frameIndex] + self.rolls[self.frameIndex+1] == 10 )
    
    def roll(self,pins):
        if self.getCanPlay():
            self.rolls[self.currentRoll] = pins
            self.currentRoll+=1
            self.updateScore()

    def updateScore(self):
        if self.isStrike():
            self.score+=20
            self.roll[self.currentRoll+1]=0
            self.currentRoll+=1
            self.frameIndex+=2
            if self.frameIndex > self.MAX_ROLLS_ALLOWED:
                self.canPlay = False
        else:
            if(self.frameIndex >= self.MAX_ROLLS_ALLOWED-1):
                self.score +=self.rolls[self.frameIndex]
                self.canPlay = False
            elif self.firstRoll== True:
                self.firstRoll=False
            else:
                if self.isSpare():
                    self.score += 5
                self.score += (self.rolls[self.frameIndex] + self.rolls[self.frameIndex+1])
                self.frameIndex +=2
                self.firstRoll = True
                if self.frameIndex >= self.MAX_ROLLS_ALLOWED-3:
                    self.canPlay = False

