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
from helpers import  make_coins,eat_coins,clear
import constants
import time
from background import Screen
from board import Board 
colorama.init()




class Player():
    
    def __init__(self,x):
        self.x = x
        self.y = 24
    
    def draw(self,surface,dir=0):
        surface.screen[self.x][self.y-1] = '0'
        surface.screen[self.x-1][self.y-1] = '/'
        surface.screen[self.x-1][self.y] = '\\'
        surface.screen[self.x][self.y] = '0' 
        
        if dir == 0:
            if surface.screen[self.x][self.y-3] == '0':
                surface.screen[self.x][self.y-3] = ' '
            if surface.screen[self.x-1][self.y-2] == '/':
                surface.screen[self.x-1][self.y-2] = ' '
            if surface.screen[self.x-1][self.y-2] == '\\':
                surface.screen[self.x-1][self.y-2] = ' '
            if surface.screen[self.x][self.y-2] == '0':
                surface.screen[self.x][self.y-2] = ' '
        elif dir == 1:
            if surface.screen[self.x][self.y+2] == '0':
                surface.screen[self.x][self.y+2] = ' '
            if surface.screen[self.x-1][self.y+2] == '/':
                surface.screen[self.x-1][self.y+2] = ' '
            if surface.screen[self.x-1][self.y+1] == '\\':
                surface.screen[self.x-1][self.y+1] = ' '
            if surface.screen[self.x][self.y+1] == '0':
                surface.screen[self.x][self.y+1] = ' '
    
    def jump(self,surface):
        if surface.screen[self.x-2][self.y-1] == ' ' and surface.screen[self.x-2][self.y] == ' ':
            surface.screen[self.x][self.y]= ' '
            surface.screen[self.x][self.y-1]= ' '
            surface.screen[self.x-1][self.y]= ' '
            surface.screen[self.x-1][self.y-1]= ' '
            if surface.screen[self.x+1][self.y-1] == '?' or surface.screen[self.x+1][self.y] == '?':
                self.x -=5
            if surface.screen[self.x+1][self.y-1] == '#' or surface.screen[self.x+1][self.y] == '#':
                self.x -=3
            if surface.screen[self.x+1][self.y-1] == ' ' or surface.screen[self.x+1][self.y] == ' ':
                self.x -=1
            if surface.screen[self.x+1][self.y-1] == 'x' or surface.screen[self.x+1][self.y] == 'x':
                self.x -=2
            if surface.screen[self.x+1][self.y-1] == '8' or surface.screen[self.x+1][self.y] == '8':
                self.x -=4
        else:
            pass

    def fall(self,surface):
        if surface.screen[self.x+1][self.y] == '^' and surface.screen[self.x+1][self.y-1] == '^':
            return 1
        if surface.screen[self.x+1][self.y] == ' ' and surface.screen[self.x+1][self.y-1] == ' ':
            #The without moving case
            if surface.screen[self.x-1][self.y-1] == '/':
                surface.screen[self.x-1][self.y-1] = ' '
            if surface.screen[self.x-1][self.y] == '\\':
                surface.screen[self.x-1][self.y] = ' '
            #The moving case
            if surface.screen[self.x-1][self.y-2] == '/':
                surface.screen[self.x-1][self.y-2] = ' '
            if surface.screen[self.x][self.y-2] == '0':
                surface.screen[self.x][self.y-2] = ' '
            if surface.screen[self.x-1][self.y+1] == '\\':
                surface.screen[self.x-1][self.y+1] = ' '
            if surface.screen[self.x][self.y+1] == '0':
                surface.screen[self.x][self.y+1] = ' '
            
            if surface.screen[self.x-1][self.y] == '/':
                surface.screen[self.x-1][self.y] = ' '
            if surface.screen[self.x-1][self.y-1] == '\\':
                surface.screen[self.x-1][self.y-1] = ' '
            self.x += 1
            return 1
    
    def clean(self,surface):
        surface.screen[self.x-1][self.y] = ' '
        surface.screen[self.x-1][self.y-1] = ' '
        surface.screen[self.x][self.y-1] = ' '
        surface.screen[self.x][self.y] = ' ' 
   
    def retx(self):
        return self.x
    def rety(self):
        return self.y
    def setx(self,x):
        self.x = x
    def sety(self,y):
        self.y = y

screen = Screen()
board = Board()
enemyList = []
player = Player(16)
health = 3
count = 0

def make_scene(screen):
    clear()
    clear()
    print(Fore.RED+"                         Mario               "+Style.RESET_ALL)
    print(Fore.GREEN+"  Health               "+str(health)+Style.RESET_ALL+Fore.YELLOW+"   Score             "+str(count*10)+Style.RESET_ALL)
    screen.draw()

def initScreen(screen,board): 
    player.draw(screen)
    board.bridge(screen,35)
    board.draw(screen)
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
    if screen.screen[x][y+1] == 'O':
        return 1
    elif screen.screen[x][y+1] == '8' or screen.screen[x][y+1] == 'x' or screen.screen[x][y+1] == 'x' or screen.screen[x-1][y+1] == 'x' or screen.screen[x-1][y+1] == 'x'\
            or screen.screen[x][y+1] == '#':
        return 2
    elif screen.screen[x][y-2] == '8' or screen.screen[x][y-2] == 'x' or screen.screen[x][y-2] == 'x' or screen.screen[x-1][y-2] == 'x' or screen.screen[x-1][y-2] == 'x' \
            or screen.screen[x][y-2] == '8':
        return 3
    elif screen.screen[x-2][y] == '?' or screen.screen[x-2][y-1] == '?':
        screen.screen[x-2][y] = ' '       
        return 4

def restart(screen,player):
    x = player.retx()
    y = player.rety()
    screen.screen[x][y] = ' '
    screen.screen[x-1][y] = ' '
    screen.screen[x][y-1] = ' '
    screen.screen[x-1][y-1] = ' '
    
    del(player)
    player = Player(14)
    return player



coin_count = int(0)

iter =0
dir =0

coin_count = make_coins(screen,15,coin_count)
while True:
    iter +=1 
    if iter % 5 == 0:
        createObstacle(board,screen)

    coin_count = make_coins(screen,38,coin_count)     
    if iter %2 == 0:
        if player.retx() + 1 == 20:
            player = restart(screen,player)
            health -= 1
            
        player.fall(screen)
    if eat_coins(screen,player):
        count += 1
        coin_count -= 1 
    player.draw(screen,dir)      
    make_scene(screen)   
    try:
        keypress = input.get_input()
        if keypress == 'd':
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
        elif keypress == 'q':
            break
        
    except:
        pass     
print(count*10)