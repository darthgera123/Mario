from os import name
from os import system
import random
from player import Player 

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



def restart(screen,player):
    player.clean(screen)
    y = player.rety()
    del(player)
    player = Player(14,y-2)
    return player
    
def make_coins(screen,y,coin_count):
    
    for i in range(0,2): 
        x_coins = random.randint(13,16)
        y_coins = random.randint(y,y+20)  
        if screen.screen[x_coins][y_coins] == ' ' and coin_count <= 5:
            screen.screen[x_coins][y_coins] = '$'
            coin_count += 1
        return coin_count
def eat_coins(screen,player):
    x_player = player.retx()
    y_player = player.rety()
    options = [screen.screen[x_player][y_player+1],screen.screen[x_player][y_player-2],screen.screen[x_player-1][y_player-2],screen.screen[x_player-1][y_player+1],\
               screen.screen[x_player-2][y_player-2],screen.screen[x_player-1][y_player+1]]
    for o in options:
        if  o== '$':
            return 1
    return 0      
