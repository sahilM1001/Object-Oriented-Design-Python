class Player:
    def __init__(self,name,symbol):
        self.name = name
        self.moves = []
        self.moveNumber = 0
        self.symbol=symbol

    def move(self, row,col,matrix):
        print("self.symbol: ",self.symbol)     
        if matrix[row][col] == -1:
            matrix[row][col] = self.symbol

            self.moves.append({
                'moveNum':self.moveNumber+1,
                'row': row,
                'col': col,
                'symbol': self.symbol

            })
            self.moveNumber+=1
        return matrix
       
    def showMoves(self):
        for move in self.moves:
            print("\n-------------------------------------------------\n")
            print(move)

