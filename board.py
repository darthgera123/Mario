import random
import numpy as np
from background import Screen


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
        choicy = random.randint(8,10)
        if np.all(surface.screen[13+choice:17,y_start-choicy:y_start+choicy]==' '):
            surface.screen[12+choice:17,y_start:y_start+3]="8"