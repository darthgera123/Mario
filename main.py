from __future__ import print_function
import os
from os import system
from os import name
import numpy as np
import colorama
from colorama import Fore, Back, Style
import random

#Inheriting all important functions to main
import input
from sound import play,kill
from helpers import  make_coins,eat_coins,clear,restart, checkMissions
from logic import make_enemy, checkMove, killEnemy, killPlayer, moveEnemy
from constants import *
from board_draw import initScreen,createObstacle

colorama.init(autoreset=True)


main = play(theme)

# Basic function for printing the above info
def make_scene(screen):
    clear()
    clear()
    print(Fore.RED+"                         Mario               "+Style.RESET_ALL)
    print(Fore.GREEN+"  Health               "+str(health)+Fore.YELLOW+"   Score             "+str(count*10+enemy_kill*30+mission_comp*100))
    print(Fore.RED+"  Kills               "+str(enemy_kill)+Fore.YELLOW+"   Coins             "+str(count))
    screen.draw()

initScreen(screen,board) 
enemyList.append(enemy)
coin_count = make_coins(screen,15,coin_count)

while True:
    iter +=1 

    # Speed of obstacle creation 
    if iter % 5 == 0:
        createObstacle(board,screen)
    
    #This will increase enemy creation speed
    if iter_count % 50 == 0:
        if speed != 5:
            speed -=5
        else:
            pass    
    if iter % speed == 0:
        make_enemy(screen)

    #Keeping Track of count so that it doesnt litter the board
    coin_count = make_coins(screen,38,coin_count)     
    moveEnemy(screen)
    
    #The fall is implemented wvery 2 iterations
    if iter %2 == 0:
        if player.retx() + 1 == 20:
            player = restart(screen,player)
            health -= 1
            if health == 0:
                break
    #Enemy is killed if the player is supposeed to fall on him
        if killEnemy(screen,player):
            enemy_kill += 1
        
    if eat_coins(screen,player):
        play(coin)
        count += 1
        coin_count -= 1 
    
    if killPlayer(screen,player):
        player = restart(screen,player)
        health -= 1 
        if health == 0:
                break
    
    player.draw(screen,dir)
    mission_comp = checkMissions(mission_comp)
    make_scene(screen)   
    try:
        keypress = input.get_input()
        if keypress == 'd':
            iter_count +=1
            dir=0
            move = checkMove(screen,player)
            if move != 2 and move != 1:
                screen.move_right()
        elif keypress == 'a':
            dir=1
            move = checkMove(screen,player)
            if move != 3 and move!= 1:
                screen.move_left()
        elif keypress == 'w':
            play(jump)
            player.jump(screen)
            make_scene(screen) 
        elif keypress == 'q':
            break
    except:
        pass
            

if health == 0:
    print(Fore.YELLOW+"   Score             "+str(count*10+enemy_kill*30+mission_comp*100)+" Better luck next time")
else :
    print(Fore.GREEN+"  Health               "+str(health)+Fore.YELLOW+"   Score             "+str(count*10+enemy_kill*30+mission_comp*100))

comp = 0
for v in missions.values():
    if v == True:
        comp+=1
print(Fore.BLUE+"  Missions Completed =               "+str(comp))
#Killing the main sound
kill(main)
