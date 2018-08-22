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
        surface.screen[self.x][self.top_y-1] = ' ' 
        surface.screen[self.x-1][self.top_y-2] = ' ' 
        surface.screen[self.x-1][self.top_y-1] = ' '
        surface.screen[self.x-1][self.top_y] = ' '
        
    def move_right(self,surface):
        surface.screen[self.x][self.top_y-1] = ' ' 
        surface.screen[self.x-1][self.top_y-2] = ' ' 
        surface.screen[self.x-1][self.top_y-1] = ' '
        surface.screen[self.x-1][self.top_y] = ' '
                  
    
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