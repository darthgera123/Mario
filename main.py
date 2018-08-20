from __future__ import print_function
import os
from sys import argv as rd
from os import system
from os import name
import numpy as np
import time

import input
from constants import terminal_ht, terminal_width
import helpers
 
class Screen:

    def __init__(self):
        self.screen_height = terminal_ht
        self.screen_width = terminal_width
        self.screen = np.full((self.screen_height,self.screen_width), ' ', dtype='str')
    
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
        surface.screen[25][screen.screen_width-15:screen.screen_width-11] = self._board_bridge_char

def make_scene(screen,board):
    #helpers.clear()
    #helpers.clear()
    board.draw(screen)
    screen.draw()
    #player.draw(screen)
            



screen = Screen()
board = Board()

#player= Player()
board.bridge(screen)
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