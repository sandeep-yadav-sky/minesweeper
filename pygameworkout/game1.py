import pygame
import os
from time import sleep
pygame.init()


class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0]//self.board.getSize(
        )[1], self.screenSize[1]//self.board.getSize()[0]
        self.loadImages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while(running):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    # print(rightClick)
                    self.handleClick(position, rightClick)

            self.draw()
            pygame.display.flip()
            if self.board.getWon():
                running =False
                sound = pygame.mixer.Sound("win.wav")
                sound.play()
                sleep(3)
        pygame.quit()

    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.size[0]):
            for col in range(self.board.size[1]):
                piece = self.board.getPiece(row, col)
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0]+self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1]+self.pieceSize[1]

    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if (not (fileName.endswith(".png"))):
                continue
            image = pygame.image.load(r"images/"+fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image
        # print(self.images[0])

    def getImage(self, piece):
        string = "0"
        if piece.getClicked():
            if piece.getHashBomb():
                string = "bomb-at-clicked-block"
            else:
                num = piece.getNumAround()
                string = str(num)
        else:
            if(piece.getFlagged()):
                string = "flag"
            else:
                string = "empty-block"
            # print(piece.getFlagged())
        return self.images[string]

    def handleClick(self, position, rightClick):
        if self.board.getLost():
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index[0], index[1])
        self.board.handleClick(piece, rightClick)
