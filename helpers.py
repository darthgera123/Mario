from os import name
from os import system
import colorama
from colorama import Fore
import random
from player import Player 
from constants import enemy_kill, mission_comp, missions,count
#Used for clearing screen
colorama.init(autoreset=True)
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def checkMissions(mission_comp):
    if enemy_kill == 5 and missions['Kill 5 enemies'] == False:
        print(Fore.GREEN+"Mission 1 completed Points added = 100")
        mission_comp +=1
        missions['Kill 5 enemies'] = True
    
    elif count == 50 and  missions['Collect 50 Points'] == False:
        print(Fore.GREEN+"Mission 2 completed Points added = 100")
        mission_comp +=1
        missions['Collect 50 Points'] = True
    
    elif count*10+enemy_kill*30+mission_comp*100 == 500 and missions['Score 500 points'] == False:
        print(Fore.GREEN+"Mission 3 completed Points added = 100")
        mission_comp +=1
        missions['Score 500 points'] = True
    
    return mission_comp

#Restarts the player after it has been killed
def restart(screen,player):
    player.clean(screen)
    y = player.rety()
    del(player)
    player = Player(14,y-2)
    return player
    
#Randomly generates coins
def make_coins(screen,y,coin_count):
    
    for i in range(0,2): 
        x_coins = random.randint(13,16)
        y_coins = random.randint(y,y+20)  
        if screen.screen[x_coins][y_coins] == ' ' and coin_count <= 5:
            screen.screen[x_coins][y_coins] = '$'
            coin_count += 1
        return coin_count

#Check for whether a coin is eaten
def eat_coins(screen,player):
    x_player = player.retx()
    y_player = player.rety()
    options = [screen.screen[x_player][y_player+1],screen.screen[x_player][y_player-2],screen.screen[x_player-1][y_player-2],\
                screen.screen[x_player-1][y_player+1],screen.screen[x_player-1][y_player+1]]
    for o in options:
        if  o == '$':
            return 1
    return 0      

