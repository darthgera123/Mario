import random
from constants import enemy,player

#Functions to draw the initial main board
def initScreen(screen,board):  
    
    board.pipe(screen,28)
    board.draw(screen)
    player.draw(screen)
    enemy.draw(screen)
    for i in range(0,10):
        board.clouds(screen,8,25,39)

#Function to create obstacle
def createObstacle(board,screen):
    board.clouds(screen,6,50,58)
    options = [board.pipe(screen,50),board.pit(screen),board.bridge(screen,56)]
    choice = random.randint(0,2)
    return options[choice]