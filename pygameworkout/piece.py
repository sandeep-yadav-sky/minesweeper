class Piece():
    def __init__(self, hasBomb):
        self.hashBomb = hasBomb
        self.clicked = False
        self.flagged = False
    
    def getHashBomb(self):
        return self.hashBomb
    
    def getClicked(self):
        return self.clicked
    
    def getFlagged(self):
        return self.flagged
    
    def setNeighbors(self,neighbors):
        self.neighbors = neighbors
        self.setNumAround()
        
    def setNumAround(self):
        self.NumAround = 0
        for piece in self.neighbors:
            if(piece.getHashBomb()):
                self.NumAround+=1
    
    def getNumAround(self):
        return self.NumAround 
    
    def toggleFlag(self):
        self.flagged = not self.flagged
    
    def click(self):
        self.clicked = True
        
    def getNeighbors(self):
        return self.neighbors
        