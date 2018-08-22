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
from helpers import make_scene, test
import constants
import time
from background import Screen
from board import Board 
colorama.init()


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
            if surface.screen[self.x][self.y-2] == 'O' and surface.screen[self.x-1][self.y-2]=='^':
                surface.screen[self.x][self.y-2]= ' '
                surface.screen[self.x-1][self.y-2]= ' '
        else:
            if surface.screen[self.x][self.y+2] == 'O' and surface.screen[self.x-1][self.y+2]=='^':
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
        if surface.screen[self.x+1][self.y+1] == ' ':
            surface.screen[self.x][self.y] = ' '
            surface.screen[self.x-1][self.y] = ' '
            return 1
        return 0
    
    def retx(self):
        return self.x
    
    def rety(self):
        return self.y

class Player(Screen):
    
    def __init__(self):
        self.x = 16
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
        surface.screen[self.x][self.y]= ' '
        surface.screen[self.x][self.y-1]= ' '
        surface.screen[self.x-1][self.y]= ' '
        surface.screen[self.x-1][self.y-1]= ' '
        self.x -=2

    def fall(self,surface):
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
            
            if surface.screen[self.x-1][self.y+2] == '/':
                surface.screen[self.x-1][self.y+2] = ' '
            if surface.screen[self.x-1][self.y-3] == '\\':
                surface.screen[self.x-1][self.y-3] = ' '
            
            
            self.x += 1
    
    def clean(self,surface):
        surface.screen[self.x-1][self.y] = ' '
        surface.screen[self.x-1][self.y-1] = ' '
        surface.screen[self.x][self.y-1] = ' '
        surface.screen[self.x][self.y] = ' ' 
   
    def retx(self):
        return self.x
    def rety(self):
        return self.y

screen = Screen()
board = Board()
enemyList = []
player = Player()

def createEnemy():
    if len(enemyList) == 0:
        enemy = Enemy(38)
        enemy2 = Enemy(30)
        enemy3 = Enemy(40)
        enemyList.append(enemy)
        enemyList.append(enemy2)
        enemyList.append(enemy3)


def initScreen(screen,board):
    createEnemy()
    player.draw(screen)
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
    if enemy.fall(screen) == 1:
        return 1
    enemy.draw(screen)

def all_enemy(screen,board):
    for e in enemyList:
        if enemyWork(e,screen):
            screen.screen[e.retx()][e.rety()+1] = ' '
            screen.screen[e.retx()-1][e.rety()+1] = ' '
            del(e)
            
        else:
            make_scene(e,screen,board)     

def checkMove(screen,player):
    x = player.retx()
    y = player.rety()
    if screen.screen[x][y+1] == 'O':
        return 1
    elif screen.screen[x][y+1] == '8' or screen.screen[x-1][y+1] == 'x' or screen.screen[x][y+1] == 'x':
        return 2
    elif screen.screen[x][y-2] == '8' or screen.screen[x-1][y-2] == 'x' or screen.screen[x][y-2] == 'x':
        return 3
    elif screen.screen[x-2][y] == '?':
        screen.screen[x-2][y] = 'x'
        return 4

count = 0
iter =0
dir =0
while True:
    iter +=1 
    if iter % 5 == 0:
        createObstacle(board,screen)
    test(screen)    
    if iter %2 == 0:
        try:
            player.fall(screen)
        except:
            player.clean(screen)
    player.draw(screen,dir)
    createEnemy()
    all_enemy(screen,board)   
    
    try:
        keypress = input.get_input()
        if keypress == 'd':
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
            count = 0
            player.jump(screen)
        elif keypress == 'q':
            break
        
    except:
        pass     
print(len(enemyList))