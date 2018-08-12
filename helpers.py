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
    screen.clear()
    board.draw(screen)
    player.draw(screen)
    screen.draw()
