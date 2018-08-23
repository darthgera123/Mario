class Player():
    
    def __init__(self,x=15,y=26):
        self.x = x
        self.y = y
        self._topl_char = '>'
        self._topr_char = '<'
        self._bottom_char = '0'
        
    
    def draw(self,surface,dir=0):
        surface.screen[self.x][self.y-1] = self._bottom_char
        surface.screen[self.x-1][self.y-1] = self._topl_char
        surface.screen[self.x-1][self.y] = self._topr_char
        surface.screen[self.x][self.y] = self._bottom_char 
        
        if dir == 0:
            if surface.screen[self.x][self.y-3] == self._bottom_char:
                surface.screen[self.x][self.y-3] = ' '
            if surface.screen[self.x-1][self.y-2] == self._topl_char:
                surface.screen[self.x-1][self.y-2] = ' '
            if surface.screen[self.x-1][self.y-2] == self._topr_char:
                surface.screen[self.x-1][self.y-2] = ' '
            if surface.screen[self.x][self.y-2] == self._bottom_char:
                surface.screen[self.x][self.y-2] = ' '
        elif dir == 1:
            if surface.screen[self.x][self.y+2] == self._bottom_char:
                surface.screen[self.x][self.y+2] = ' '
            if surface.screen[self.x-1][self.y+2] == '/':
                surface.screen[self.x-1][self.y+2] = ' '
            if surface.screen[self.x-1][self.y+1] == self._topr_char:
                surface.screen[self.x-1][self.y+1] = ' '
            if surface.screen[self.x][self.y+1] == self._bottom_char:
                surface.screen[self.x][self.y+1] = ' '
    
    def jump(self,surface):
        #Need to work on it now
        if surface.screen[self.x-2][self.y-1] == ' ' and surface.screen[self.x-2][self.y] == ' ':
            surface.screen[self.x][self.y]= ' '
            surface.screen[self.x][self.y-1]= ' '
            surface.screen[self.x-1][self.y]= ' '
            surface.screen[self.x-1][self.y-1]= ' '
            if surface.screen[self.x+1][self.y-1] == '?' or surface.screen[self.x+1][self.y] == '?':
                self.x -=5
            if surface.screen[self.x+1][self.y-1] == '#' or surface.screen[self.x+1][self.y] == '#':
                self.x -=2
            if surface.screen[self.x+1][self.y-1] == ' ' or surface.screen[self.x+1][self.y] == ' ':
                self.x -=1
            if surface.screen[self.x+1][self.y-1] == 'x' or surface.screen[self.x+1][self.y] == 'x':
                self.x -=2
            if surface.screen[self.x+1][self.y-1] == '8' or surface.screen[self.x+1][self.y] == '8':
                self.x -=4
            if surface.screen[self.x+1][self.y-1] == '!' or surface.screen[self.x+1][self.y] == '!':
                self.x -=5
        else:
            pass

    def fall(self,surface):
        if surface.screen[self.x+1][self.y] == '!' or surface.screen[self.x+1][self.y-1] == '!':
            return 1
        if surface.screen[self.x+1][self.y] == ' ' and surface.screen[self.x+1][self.y-1] == ' ':
            #The without moving case
            if surface.screen[self.x-1][self.y-1] == self._topl_char:
                surface.screen[self.x-1][self.y-1] = ' '
            if surface.screen[self.x-1][self.y] == self._topr_char:
                surface.screen[self.x-1][self.y] = ' '
            #The moving case
            if surface.screen[self.x-1][self.y-2] == self._topl_char:
                surface.screen[self.x-1][self.y-2] = ' '
            if surface.screen[self.x][self.y-2] == self._bottom_char:
                surface.screen[self.x][self.y-2] = ' '
            if surface.screen[self.x-1][self.y+1] == self._topr_char:
                surface.screen[self.x-1][self.y+1] = ' '
            if surface.screen[self.x][self.y+1] == self._bottom_char:
                surface.screen[self.x][self.y+1] = ' '
            
            if surface.screen[self.x-1][self.y] == self._topl_char:
                surface.screen[self.x-1][self.y] = ' '
            if surface.screen[self.x-1][self.y-1] == self._topr_char:
                surface.screen[self.x-1][self.y-1] = ' '
            self.x += 1
            return 0
    
    def clean(self,surface):
        surface.screen[self.x-1][self.y] = ' '
        surface.screen[self.x-1][self.y-1] = ' '
        surface.screen[self.x][self.y-1] = ' '
        surface.screen[self.x][self.y] = ' ' 
   
    def retx(self):
        return self.x
    def rety(self):
        return self.y