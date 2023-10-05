from Player import Player
class Game:
    def __init__(self, p1Name, p2Name,p1Sym,p2Sym):
        self.p1 = Player(p1Name,p1Sym)
        self.p2 = Player(p2Name,p2Sym)
        self.matrix = [[-1,-1,-1] for i in range(0,3)]
        self.winnerName = "No Winner"
        print("Game was initiated")

        self.startGame()
    def startGame(self):
        last = "p2"
        print("winnername var: ", self.winnerName)
        while self.winnerName == "No Winner":
            print("showing matrix for decision: ")
            print(self.matrix)
            if last == "p2":
                inp = input("Turn for Player one, input comma-separated 0-index based values to mark your symbol")
                pos = [int(x) for x in inp.split(",")]
                self.matrix = self.p1.move(pos[0],pos[1],self.matrix)
                last = "p1"
            print(self.matrix)
            self.checkWinner()
            if self.winnerName == "No Winner":
                if last=="p1":
                    inp = input("Turn for Player two, input comma-separated 0-index based values to mark your symbol")
                    pos = [int(x) for x in inp.split(",")]
                    self.matrix = self.p2.move(pos[0],pos[1],self.matrix)
                    last = "p2"

            
        print("while loop was exited")
            
    
    def checkWinner(self):
        import numpy as np
        for board in [self.matrix, np.transpose(self.matrix)]:
            result = self.checkRows(board)
            
            if result != -1:
                self.winnerName = "We have a winner"
                self.findWinnerName(result)
                self.printMatrix()
                return True
                

            res2 = self.checkDiagonals(board)
            if res2 != -1:
                self.winnerName = "We have a winner"
                self.findWinnerName(result)
                self.printMatrix()
                return True

        
    def findWinnerName(self,result):
        if result == 1:
            if self.p1.symbol == 1: 
                print("Player: ", self.p1.name, " has won the game")
                print("Below are the moves the user took during the game")
                self.p1.showMoves()
            else:
                print("Player: ", self.p2.name, " has won the game")
                print("Below are the moves the user took during the game")
                self.p2.showMoves()
        if result == 0:
            if self.p1.symbol == 0: 
                print("Player: ", self.p1.name, " has won the game")
                print("Below are the moves the user took during the game")
                self.p1.showMoves()
            else:
                print("Player: ", self.p2.name, " has won the game")
                print("Below are the moves the user took during the game")
                self.p1.showMoves()

    def checkRows(self,board):
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return -1

    def checkDiagonals(self,board):
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return board[0][len(board)-1]
        return -1
    
            
    def printMatrix(self):
        for row in self.matrix:
            print(row)

           

        
    
