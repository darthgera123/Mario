from os import name
from os import system

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 


def make_scene(screen,player,board):
    clear()
    clear()
    board.draw(screen)
    screen.draw()
    player.draw(screen)
    
