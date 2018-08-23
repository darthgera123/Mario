from __future__ import print_function
import os
from sys import argv as rd
from os import system
from os import name
import numpy as np
import colorama
from colorama import Fore, Back, Style
import random
import input
from constants import terminal_ht, terminal_width
from helpers import  make_coins,eat_coins,clear,restart
import constants
import time
from player import Player
from background import Screen
from board import Board 
colorama.init()


class Enemy:

    def __init__(self,y=45):
        self.x = 16
        self.y = 29
        self.state = 0
    
    def switch(self):
        if self.state ==0:
            self.state =1
        else:
            self.state =0
    
    def draw(self,surface):
        if np.all(surface.screen[self.x-1:self.x,self.y-1:self.y] == ' '):
            surface.screen[self.x-1][self.y-1] = '!'
            surface.screen[self.x-1][self.y] = '!'
            surface.screen[self.x][self.y-1] = 'O'
            surface.screen[self.x][self.y] = 'O'
    
    def move(self,surface):
        if self.state == 0:
            if self.y <=55:
                self.y = self.y + 2
            else:
                pass
        else :
            if self.y>=6:
                self.y = self.y - 1
            else:
                pass
    
    def clear(self,surface):
        if self.state == 1 and self.y <=55:    
            if surface.screen[self.x-1][self.y+2] == '!':
                surface.screen[self.x-1][self.y+2] = ' '
            if surface.screen[self.x-1][self.y+1] == '!':   
                surface.screen[self.x-1][self.y+1] = ' '
            if surface.screen[self.x][self.y+2] == 'O':  
                surface.screen[self.x][self.y+2] = ' '
            if surface.screen[self.x][self.y+1] == 'O':
                surface.screen[self.x][self.y+1] = ' '
        if self.state == 0 and self.y >= 6:    
            if surface.screen[self.x-1][self.y-3] == '!':
                surface.screen[self.x-1][self.y-3] = ' '
            if surface.screen[self.x-1][self.y-4] == '!':
                surface.screen[self.x-1][self.y-4] = ' '
            if surface.screen[self.x-1][self.y-2] == '!':   
                surface.screen[self.x-1][self.y-2] = ' '
            if surface.screen[self.x][self.y-3] == 'O':  
                surface.screen[self.x][self.y-3] = ' '
            if surface.screen[self.x][self.y-2] == 'O':
                surface.screen[self.x][self.y-2] = ' '
            if surface.screen[self.x][self.y-4] == 'O':
                surface.screen[self.x][self.y-4] = ' '
    
    def obstruct(self,surface):
        if (surface.screen[self.x][self.y+2] == '8' or surface.screen[self.x][self.y+1] == '8') and self.state == 0 :
            if self.y <= 55:
                return 1
            else:
                return 0
        elif surface.screen[self.x][self.y-2] == '8'  and self.state == 1:
            return 1
        return 0
    
    
    
    def retx(self):
        return self.x
    
    def rety(self):
        return self.y





screen = Screen()
board = Board()
enemy =  Enemy()
enemyList = []
player = Player(16)
health = 3
count = 0
enemy_kill = 0
score = count*10 + (enemy_kill*30)
def make_scene(screen):
    clear()
    clear()
    print(Fore.RED+"                         Mario               "+Style.RESET_ALL)
    print(Fore.GREEN+"  Health               "+str(health)+Style.RESET_ALL+Fore.YELLOW+"   Score             "+str(count*10+enemy_kill*30)+Style.RESET_ALL)
    screen.draw()

def initScreen(screen,board): 
    
    enemy.draw(screen)
    board.pit(screen)
    board.draw(screen)
    player.draw(screen)
    for i in range(0,10):
        board.clouds(screen,8,25,39)

initScreen(screen,board) 
def createObstacle(board,screen):
    board.clouds(screen,6,50,58)
    options = [board.pipe(screen,54),board.pit(screen),board.bridge(screen,56)]
    choice = random.randint(0,2)
    return options[choice]


def checkMove(screen,player):
    x = player.retx()
    y = player.rety()
    if screen.screen[x][y+1] == '8' or screen.screen[x][y+1] == 'x' or screen.screen[x][y+1] == 'x' or screen.screen[x-1][y+1] == 'x' or screen.screen[x-1][y+1] == 'x'\
            or screen.screen[x][y+1] == '#':
        return 2
    elif screen.screen[x][y-2] == '8' or screen.screen[x][y-2] == 'x' or screen.screen[x][y-2] == 'x' or screen.screen[x-1][y-2] == 'x' or screen.screen[x-1][y-2] == 'x' \
            or screen.screen[x][y-2] == '8':
        return 3
    elif screen.screen[x-2][y] == '?' or screen.screen[x-2][y-1] == '?':
        screen.screen[x-2][y] = ' '       
        return 4

def make_enemy(screen):
    choice = random.randint(45,55)
    e = Enemy(choice)
    enemyList.append(e)
    e.draw(screen)

def killPlayer(screen,player):
    x = player.retx()
    y = player.rety()
    if screen.screen[x][y+1] == 'O' or screen.screen[x][y+1] == '!':
        return 1
    if screen.screen[x][y-2] == 'O' or screen.screen[x][y-2] == '!':
        return 1
    return 0

def killEnemy(screen,player):
    x = player.retx()
    y = player.rety()
    if player.fall(screen) and len(enemyList)>0:
        if screen.screen[x+1][y-1] == ' ' and screen.screen[x+1][y] == '!':
            screen.screen[x+1][y] = ' '  
            screen.screen[x+1][y+1] = ' '
            screen.screen[x+2][y] = ' '
            screen.screen[x+2][y+1] = ' '
        if screen.screen[x+1][y-1] == '!' and screen.screen[x+1][y] == ' ':
            screen.screen[x+1][y-1] = ' '  
            screen.screen[x+1][y-2] = ' '
            screen.screen[x+2][y-1] = ' '
            screen.screen[x+2][y-2] = ' '
        if screen.screen[x+1][y-1] == '!' and screen.screen[x+1][y] == '!':
            screen.screen[x+1][y] = ' '  
            screen.screen[x+1][y-1] = ' '
            screen.screen[x+2][y] = ' '
            screen.screen[x+2][y-1] = ' '
        enemyList.pop()
        return 1  
    return 0

def moveEnemy(screen):
    for e in enemyList:
        if e.obstruct(screen):
            e.switch()
        e.move(screen)
        e.draw(screen)
        e.clear(screen)

coin_count = int(0)

iter =0
dir =0
enemyList.append(enemy)
iter_count = 0
speed = 30
coin_count = make_coins(screen,15,coin_count)
while True:
    iter +=1 
    if iter % 5 == 0:
        createObstacle(board,screen)
    if iter_count % 100 == 0:
        if speed != 5:
            speed -=5
        else:
            pass    
    """ if iter % speed == 0:
        make_enemy(screen) """
    #coin_count = make_coins(screen,38,coin_count)     
    if iter %2 == 0:
        if player.retx() + 1 == 20:
            player = restart(screen,player)
            health -= 1
            if health == 0:
                break

        if killEnemy(screen,player):
            enemy_kill += 1
        
    if eat_coins(screen,player):
        count += 1
        coin_count -= 1 
    
    if killPlayer(screen,player):
        player = restart(screen,player)
        health -= 1 
        if health == 0:
                break
    player.draw(screen,dir)
    moveEnemy(screen)
    make_scene(screen)   
    try:
        keypress = input.get_input()
        if keypress == 'd':
            iter_count +=1
            dir=0
            move = checkMove(screen,player)
            if move != 2 and move != 1:
                screen.move_right()
            if move == 4:
                count +=1  
        elif keypress == 'a':
            dir=1
            move = checkMove(screen,player)
            if move != 3 and move!= 1:
                screen.move_left()
            if move == 4:
                count +=1
        elif keypress == 'w':
            player.jump(screen)
            make_scene(screen) 
        elif keypress == 'q':
            break
        
    except:
        pass
            

if health == 0:
    print(Fore.YELLOW+"   Score             "+str(count*10+enemy_kill*30)+" Better luck next time"+Style.RESET_ALL)
else :
     print(Fore.GREEN+"  Health               "+str(health)+Style.RESET_ALL+Fore.YELLOW+"   Score             "+str(count*10+enemy_kill*30)+Style.RESET_ALL)
print(enemyList[0].state)