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
            for stone in base[10:-10]:
                print(stone, end=" ")
            print(' ')


class Board(Screen):

    def __init__(self):
        Screen.__init__(self)
        self._board_base_char = '#'
        self._board_bridge_char = '%'
        
    def draw(self,surface):
        surface.screen[-3:] = self._board_base_char

    def bridge(self,surface):
        surface.screen[-7][screen.screen_width-12:screen.screen_width-10] = self._board_bridge_char
        surface.screen[-6][screen.screen_width-12:screen.screen_width-10] = self._board_bridge_char
        surface.screen[-7][screen.screen_width-10:screen.screen_width-8] = '?'
        surface.screen[-6][screen.screen_width-10:screen.screen_width-8] = '?'
        surface.screen[-7][screen.screen_width-8:screen.screen_width-6] = self._board_bridge_char
        surface.screen[-6][screen.screen_width-8:screen.screen_width-6] = self._board_bridge_char
        surface.screen[-7][screen.screen_width-6:screen.screen_width-4] = '?'
        surface.screen[-6][screen.screen_width-6:screen.screen_width-4] = '?'
    def pit(self,surface):
        surface.screen[-3:,45:48] = ' '
    
    def clouds(self,surface,x_max,y_start,y_end):
        x = random.randint(x_max-3,x_max)
        y = random.randint(y_start,y_end)
        if surface.screen[x-1][y-4] == ' ':
            surface.screen[x-1][y-4]='('
        if surface.screen[x-2][y-3] == ' ':
            surface.screen[x-2][y-3]='/'
        if surface.screen[x-3][y-2] == ' ':
            surface.screen[x-3][y-2]='-'
        if surface.screen[x-2][y-1] == ' ':
            surface.screen[x-2][y-1]='\\'
        if surface.screen[x-1][y] == ' ':
            surface.screen[x-1][y]=')'
        if surface.screen[x][y-3] == ' ' and surface.screen[x][y-2] == ' ' and surface.screen[x][y-1] == ' ':
            surface.screen[x][y-3:y]='-'

    def pipe(self,surface,y_start):
        choice = random.randint(0,3)
        surface.screen[12+choice:17,y_start:y_start+3]="8"


def make_scene(screen,board):
    helpers.clear()
    helpers.clear()
    print(Fore.RED+"                         Mario               "+Style.RESET_ALL)
    #board.draw(screen)
    screen.draw()
    
            



screen = Screen()
board = Board()
board.draw(screen)
board.bridge(screen)
board.pipe(screen,20)
board.pit(screen)
for i in range(0,10):

    board.clouds(screen,8,15,39)

make_scene(screen,board)
count = 0

while True:
    
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