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
from helpers import make_scene
import constants
from background import Screen 
colorama.init()

class Board(Screen):

    def __init__(self):
        Screen.__init__(self)
        self._board_base_char = '#'
        self._board_bridge_char = '%'
        
    def draw(self,surface):
        surface.screen[-3:] = self._board_base_char

    def bridge(self,surface,start):
        x = random.randint(0,1)
        if np.all(surface.screen[12+x:17,start-6:start+6] == ' '):
            surface.screen[12+x:14,start:start+1] = 'x'
            surface.screen[12+x:14,start+1:start+2] = '?'
            surface.screen[12+x:14,start+2:start+3] = 'x' 
        pass
    
    def pit(self,surface):
        if np.all(surface.screen[-3:42:46]=='#') and np.all(surface.screen[-3:49:52] =='#'):
            surface.screen[-3:,46:52] = ' '
    
    def clouds(self,surface,x_max,y_start,y_end):
        x = random.randint(x_max-3,x_max)
        y = random.randint(y_start,y_end)
        if np.all(surface.screen[x-3:x+1,y-4:y+1] == ' '):
            surface.screen[x-1][y-4]='('
            surface.screen[x-2][y-3]='/'
            surface.screen[x-3][y-2]='-'
            surface.screen[x-2][y-1]='\\'
            if surface.screen[x-1][y+1] == ' ':
                surface.screen[x-1][y]=')'
            surface.screen[x][y-3:y]='-'

    def pipe(self,surface,y_start):
        choice = random.randint(0,2)
        if np.all(surface.screen[13+choice:17,y_start-10:y_start+10]==' '):
            surface.screen[12+choice:17,y_start:y_start+3]="8"

    def nothing(self,surface):
        #surface.screen[14:17,55:59] = ' '
        pass

class Enemy(Screen):

    def __init__(self,y=45):
        self.x = 16
        self.y = y
        self.state = 1

    def switch(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0

    def move(self):
        if self.state == 0:
            self.y = self.y + 1
        else :
            self.y = self.y - 1

    def draw(self,surface):
        if self.state == 0:
            surface.screen[self.x][self.y-1] = ' '
            surface.screen[self.x-1][self.y-1]= ' '
            surface.screen[self.x][self.y]= 'O'
            surface.screen[self.x-1][self.y]= '^'
        elif self.state == 1:
            surface.screen[self.x][self.y+1] = ' '
            surface.screen[self.x-1][self.y+1]= ' '
            surface.screen[self.x][self.y]= 'O'
            surface.screen[self.x-1][self.y]= '^'
        elif self.y == -59:
            pass
    
    def clear(self,surface):
        if self.state == 0:
            surface.screen[self.x][self.y-2]= ' '
            surface.screen[self.x-1][self.y-2]= ' '
        else:
            surface.screen[self.x][self.y + 2] = ' '
            surface.screen[self.x-1][self.y + 2] = ' '
    def obstruct(self,surface):
        if surface.screen[self.x][self.y+2] != ' ' and self.state == 0:
            return 1
        elif surface.screen[self.x][self.y-2] != ' ' and self.state == 1:
            return 1
        elif self.y <= -50 :
            return 1
        else:
            return 0
    def fall(self,surface):
        if np.any(surface.screen[17:20,self.y:self.y+1] != '#'):
            if self.x == 19:
                surface.screen[self.x][self.y]==' '
                surface.screen[self.x-1][self.y]==' '
                return 2
            else:
                surface.screen[self.x-2][self.y]==' '
                self.x += 1
            return 1
        return 0
    
    def retx(self):
        return self.x
    
    def rety(self):
        return self.y


screen = Screen()
board = Board()
enemyList = []

def initScreen(screen,board):
    #player to be added
    enemy = Enemy()
    enemy2 = Enemy(30)
    enemy3 = Enemy(40)
    enemyList.append(enemy)
    enemyList.append(enemy2)
    enemyList.append(enemy3)
    board.pipe(screen,35)
    board.draw(screen)
    for i in range(0,10):
        board.clouds(screen,8,25,39)

initScreen(screen,board) 
def createObstacle(board,screen):
    board.clouds(screen,8,50,58)
    options = [board.pipe(screen,54),board.pit(screen),board.bridge(screen,56)]
    choice = random.randint(0,2)
    return options[choice]

def enemyWork(enemy,screen):
    if enemy.obstruct(screen):
        enemy.switch()
    if enemy.fall(screen) == 0:
        enemy.move()
    if enemy.fall(screen) == 2:
        return
    enemy.draw(screen)
def all_enemy(screen,board):
    for e in enemyList:
        enemyWork(e,screen)
        make_scene(e,screen,board)     

count = 0
iter =0
while True:
    iter +=1 
    if iter % 5 == 0:
        createObstacle(board,screen)

    all_enemy(screen,board)   
    
    try:
        keypress = input.get_input()
        if keypress == 'd':
            screen.move_right()  
        elif keypress == 'a':
            screen.move_left()
        elif keypress == 'w':
            count = 0
        elif keypress == 'q':
            break
        
    except:
        pass     
 