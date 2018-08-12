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
        self.screen = np.full((self.screen_height,self.screen_width), '.', dtype='str')
    
    def clear(self):
        self.screen = np.full((self.screen_height,self.screen_width), '.', dtype='str')

    def draw(self):
        for base in self.screen:
            for stone in base:
                print(stone, end=" ")
            print('')


class Board(Screen):

    def __init__(self):
        Screen.__init__(self)
        self._board_base_char = '#'
        
    def draw(self,surface):
        surface.screen[-1:] = self._board_base_char

    
            
class Player(Screen):

    def __init__(self):
        Screen.__init__(self)
        self.x = terminal_ht-2
        self.top_y = 0
        self.bottom_y = int(terminal_width/2)
    
    def draw(self,surface):
        surface.screen[self.x][self.top_y] = 'x' 
        surface.screen[self.x][self.top_y+1] = 'x' 
        surface.screen[self.x][self.bottom_y] = 'x'
        surface.screen[self.x][self.bottom_y+1] = 'x'

    def move_left(self):
        #this has to be worked out for the moment
        if self.top_y == terminal_width or self.top_y == 0:
            raise IndexError
        else:
            self.top_y = self.top_y - 1
            self.bottom_y = self.bottom_y - 1

    def move_right(self):
        #this has to be worked out for the moment
        if self.top_y >= terminal_width-1  or self.top_y == -1:
            raise IndexError
        else:
            self.top_y = self.top_y + 1
            self.bottom_y = self.bottom_y + 1       
    
    def jump(self):
        self.x = self.x - 1
    
    def fall(self,surface):
        if surface.screen[self.x+1][self.bottom_y] == '#':
            pass
        else:
            self.x = self.x +1
    
    def notfly(self,surface):
        if surface.screen[self.x+1][self.bottom_y] == '#':
            return True

    def topy(self):
        return self.top_y


screen = Screen()
board = Board()

player= Player()

helpers.make_scene(screen,player,board)
start = round(time.time())
while True:
    current = round(time.time())
    if not player.notfly(screen):
        if (current - start)%2 == 0:
            player.fall(screen)
            helpers.make_scene(screen,player,board)
    try:
        keypress = input.getchar()
        if keypress == 'd':
            player.move_right()
            helpers.make_scene(screen,player,board)
        if keypress == 'a':
            player.move_left()
            helpers.make_scene(screen,player,board)
        if keypress == 'w':
            player.jump()
            helpers.make_scene(screen,player,board)
        if keypress == 'q':
            break
    #This needs to be worked out
    except IndexError:    
        if player.topy() == terminal_width -2 :
            player.move_left()
        elif player.topy() <= 0:
            player.move_right()
        helpers.make_scene(screen,player,board)
    