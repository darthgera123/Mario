from constants import terminal_ht, terminal_width
import numpy as np

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
                if i == self.screen_width-1:
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
            for stone in base[20:45]:
                print(stone, end=" ")
            print(' ')
