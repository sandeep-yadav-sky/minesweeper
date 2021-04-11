from piece import Piece
from random import random
class Board():
    def __init__(self,size,prob):
        self.size = size
        self.prob = prob
        self.lost = False
        # self.win = False
        self.numClicked =0
        self.numNonBombs = 0
        self.setBoard()
    
    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hashBomb = random() < self.prob
                if(not hashBomb):
                    self.numNonBombs+=1;
                piece = Piece(hashBomb) 
                row.append(piece)
            self.board.append(row)
        self.setNeighbors()
        
    def getSize(self):
        return self.size
    def getPiece(self, row,col):
        return self.board[row][col]
    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece(row,col)
                neighbors = self.getListOfNeighbors((row,col))
                piece.setNeighbors(neighbors)
    
    def getListOfNeighbors(self,index):
        neighbors = []
        for row in range(index[0]-1,index[0]+2):
            for col in range(index[1]-1,index[1]+2):
                if(row>=0 and row<self.size[0] and col>=0 and col<self.size[1]):
                    if(not(row==index[0] and col == index[1])):
                        neighbors.append(self.getPiece(row,col))
                        # print(row,col)
        return neighbors
                    
    def handleClick(self,piece,flag):
        # print(piece.getNumAround())
        if(piece.getClicked() or (not flag and piece.getFlagged())):
            return
        if(flag):
            piece.toggleFlag()
            return
        piece.click()
        self.numClicked +=1
        if(piece.getHashBomb()):
            self.lost = True
            return
        if(piece.getNumAround()!=0):
            return
        
        for neighbor in piece.getNeighbors():
            if not neighbor.getHashBomb() and not neighbor.getClicked():
                self.handleClick(neighbor, False)
    
    def getLost(self):
        return self.lost
    def getWon(self):
        return self.numNonBombs == self.numClicked
            
