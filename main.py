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
import helpers
 
colorama.init()
class Screen:

    def __init__(self):
        self.screen_height = terminal_ht
        self.screen_width = terminal_width
        self.screen = np.full((self.screen_height,self.screen_width), ' ', dtype=np.unicode)
    
    def clear(self):
        self.screen = np.full((self.screen_height,self.screen_width), '.', dtype='str')

    def move_right(self):
        for base in self.screen:
            for i in range(0,len(base)):
                if i == screen.screen_width-1:
                    pass
                else:
                    base[i] = base[i+1]
    
    def move_left(self):
         for base in self.screen:
            for i in range(len(base)-1,0,-1):
                if i == len(base):
                    pass
                else:
                    base[i] = base[i-1]
    
    def draw(self):
        for base in self.screen:
            for stone in base[20:-10]:
                print(stone, end=" ")
            print(' ')


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
    
    def large_pit(self,surface):
        if np.all(surface.screen[-3:42:44]=='#') and np.all(surface.screen[-3:49:51] =='#'):
            surface.screen[-3:,46:49] = ' '
    
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

def make_scene(screen,board):
    helpers.clear()
    helpers.clear()
    print(Fore.RED+"                         Mario               "+Style.RESET_ALL)
    screen.draw() 
            
screen = Screen()
board = Board()
def initScreen(screen,board):
    #player to be added
    board.draw(screen)
    for i in range(0,10):
        board.clouds(screen,8,25,39)

initScreen(screen,board)
board.bridge(screen,30)
board.pipe(screen,15)
board.pit(screen)   
def createObstacle(board,screen):
    board.clouds(screen,8,50,58)
    options = [board.pipe(screen,54),board.pit(screen),board.bridge(screen,56)]
    choice = random.randint(0,2)
    return options[choice]

make_scene(screen,board)
count = 0
iter =0
while True:
    iter +=1 
    if iter % 5 == 0:
        createObstacle(board,screen)
    try:
        keypress = input.get_input()

        if keypress == 'd':
            screen.move_right()
            make_scene(screen,board)   
        elif keypress == 'a':
            screen.move_left()
            make_scene(screen,board)
        elif keypress == 'w':
            count = 0
        elif keypress == 'q':
            break
    except:
        pass