from player import Player
import numpy as np

#Enemy class inherits from Player in the sense that jump, fall and retx and rety are derived from it
class Enemy(Player):

    def __init__(self,y=45):
        Player.__init__(self)
        self.x = 16
        self.y = 40
        self.state = 1
        self._top_char = '!'
        self._bottom_char = 'O'
        self.smart = 0
    
    def switch(self):
        if self.state ==0:
            self.state =1
        else:
            self.state =0
    
    def switch_smart(self):
        self._top_char = '%'
        self.smart = 1
    
    def is_smart(self):
        return self.smart
    
    def what_state(self):
        return self.state
    def draw(self,surface):
        if np.all(surface.screen[self.x-1:self.x,self.y-1:self.y] == ' '):
            surface.screen[self.x-1][self.y-1] = self._top_char
            surface.screen[self.x-1][self.y] = self._top_char
            surface.screen[self.x][self.y-1] = self._bottom_char
            surface.screen[self.x][self.y] = self._bottom_char
    
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
            if surface.screen[self.x-1][self.y+2] == self._top_char:
                surface.screen[self.x-1][self.y+2] = ' '
            if surface.screen[self.x-1][self.y+1] == self._top_char:   
                surface.screen[self.x-1][self.y+1] = ' '
            if surface.screen[self.x][self.y+2] == self._bottom_char:  
                surface.screen[self.x][self.y+2] = ' '
            if surface.screen[self.x][self.y+1] == self._bottom_char:
                surface.screen[self.x][self.y+1] = ' '
        if self.state == 0 and self.y >= 6:    
            if surface.screen[self.x-1][self.y-3] == self._top_char:
                surface.screen[self.x-1][self.y-3] = ' '
            if surface.screen[self.x-1][self.y-4] == self._top_char:
                surface.screen[self.x-1][self.y-4] = ' '
            if surface.screen[self.x-1][self.y-2] == self._top_char:   
                surface.screen[self.x-1][self.y-2] = ' '
            if surface.screen[self.x][self.y-3] == self._bottom_char:  
                surface.screen[self.x][self.y-3] = ' '
            if surface.screen[self.x][self.y-2] == self._bottom_char:
                surface.screen[self.x][self.y-2] = ' '
            if surface.screen[self.x][self.y-4] == self._bottom_char:
                surface.screen[self.x][self.y-4] = ' '
    
    def obstruct(self,surface):
        if (surface.screen[self.x][self.y+2] == '8' or surface.screen[self.x][self.y+1] == '8') and self.state == 0 :
            if self.y <= 55:
                return 1
            else:
                return 0
        elif surface.screen[self.x][self.y-2] == '8'  and self.state == 1:
            return 1
        if (surface.screen[self.x+1][self.y+2] == ' ' or surface.screen[self.x+1][self.y+1] == ' ') and self.state == 0 :
            if self.y <= 55:
                return 1
            else:
                return 0
        elif surface.screen[self.x+1][self.y-2] == ' '  and self.state == 1:
            return 1
        return 0