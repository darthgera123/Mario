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
        self.screen = np.full((self.screen_height,self.screen_width), ' ', dtype='str')

    def move_right(self):
        for base in self.screen:
            for i in range(len(base)):
                if i == 0:
                    pass
                else:
                    base[i-1] = base[i]
    
    def move_left(self):
        for base in self.screen:
            for i in range(len(base)):
                if i == screen.screen_width-1:
                    pass
                else:
                    base[i+1] = base[i]
    
    def draw(self):
        for base in self.screen:
            for stone in base:
                print(stone, end=" ")
            print('')


class Board(Screen):

    def __init__(self):
        Screen.__init__(self)
        self._board_base_char = '#'
        self._board_bridge_char = '%'
        
    def draw(self,surface):
        surface.screen[-3:] = self._board_base_char

    def bridge(self,surface):
        surface.screen[25][screen.screen_width-5:screen.screen_width-1] = self._board_bridge_char

    
            
class Player(Screen):

    def __init__(self):
        Screen.__init__(self)
        self.x = terminal_ht-4
        self.top_y = 25
        
    
    def draw(self,surface):
        surface.screen[self.x][self.top_y] = 'X' 
        surface.screen[self.x-1][self.top_y-1] = '<' 
        surface.screen[self.x-1][self.top_y] = 'O'
        surface.screen[self.x-1][self.top_y+1] = '>'

    def move_left(self,surface):
        #self.top_y = self.top_y-1
        pass           

    def move_right(self,surface):
       #self.top_y = self.top_y+1
       pass
                  
    
    def jump(self,surface):
        if surface.screen[self.x-1][self.top_y] == '%':
            pass
        else:
            self.x = self.x - 2
    
    def fall(self,surface):
        if surface.screen[self.x+1][self.top_y] == '#':
            pass
        if surface.screen[self.x+1][self.top_y] == '%':
            pass        
        else:
            self.x = self.x + 1
    
    def notfly(self,surface):
        if surface.screen[self.x+1][self.top_y] == '#':
            return True

    def topy(self):
        return self.top_y
    
    def doublejump(self,surface):
        if surface.screen[self.x+4][self.top_y] == '#':
            return True


screen = Screen()
board = Board()

player= Player()
board.bridge(screen)
helpers.make_scene(screen,player,board)
count = 0
while True:
    helpers.make_scene(screen,player,board)
    if not player.notfly(screen):
        if count == 3:
            player.fall(screen)
            count = 0
        else:
            count += 1
        helpers.make_scene(screen,player,board)
    try:
        keypress = input.get_input()

        if keypress == 'd':
            player.move_right(screen)
            screen.move_right()
            
        elif keypress == 'a':
            player.move_left(screen)
            screen.move_left()
            
        elif keypress == 'w':
            count = 0
            player.jump(screen)
            helpers.make_scene(screen,player,board)
        elif keypress == 'q':
            break
    except:
        pass
