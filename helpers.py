from os import name
from os import system
import colorama
from colorama import Fore,Style
colorama.init()

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def make_scene(enemy,screen,board):
    clear()
    clear()
    print(Fore.RED+"                         Mario               "+Style.RESET_ALL)
    enemy.clear(screen)
    screen.draw()
    
