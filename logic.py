import random
from enemy import Enemy
from constants import enemyList, coin
from sound import play

def checkMove(screen,player):
    x = player.retx()
    y = player.rety()
    if screen.screen[x][y+1] == '8' or screen.screen[x][y+1] == 'x' or screen.screen[x][y+1] == 'x' or screen.screen[x-1][y+1] == 'x' or screen.screen[x-1][y+1] == 'x'\
            or screen.screen[x][y+1] == '#':
        return 2
    elif screen.screen[x][y-2] == '8' or screen.screen[x][y-2] == 'x' or screen.screen[x][y-2] == 'x' or screen.screen[x-1][y-2] == 'x' or screen.screen[x-1][y-2] == 'x' \
            or screen.screen[x][y-2] == '8':
        return 3

def make_enemy(screen):
    choice = random.randint(45,55)
    e = Enemy(choice)
    enemyList.append(e)
    if len(enemyList) %5 == 0:
        e.switch_smart()
    e.draw(screen)

def killPlayer(screen,player):
    x = player.retx()
    y = player.rety()
    if screen.screen[x][y+1] == 'O' or screen.screen[x][y+1] == '!':
        return 1
    if screen.screen[x][y-2] == 'O' or screen.screen[x][y-2] == '!':
        return 1
    return 0

def killEnemy(screen,player):
    x = player.retx()
    y = player.rety()
    flag =0
    if player.fall(screen) and len(enemyList)>0:
        if screen.screen[x+1][y-1] == ' ' and screen.screen[x+1][y] == '!':
            screen.screen[x+1][y] = ' '  
            screen.screen[x+1][y+1] = ' '
            screen.screen[x+2][y] = ' '
            screen.screen[x+2][y+1] = ' '
            flag = 0
        if screen.screen[x+1][y-1] == '!' and screen.screen[x+1][y] == ' ':
            screen.screen[x+1][y-1] = ' '  
            screen.screen[x+1][y-2] = ' '
            screen.screen[x+2][y-1] = ' '
            screen.screen[x+2][y-2] = ' '
            flag = 1
        if screen.screen[x+1][y-1] == '!' and screen.screen[x+1][y] == '!':
            screen.screen[x+1][y] = ' '  
            screen.screen[x+1][y-1] = ' '
            screen.screen[x+2][y] = ' '
            screen.screen[x+2][y-1] = ' '
            flag = 2
        for e in enemyList:
            y_enemy = e.rety()
            if flag == 0:
                if  y == y_enemy-1:
                    enemyList.remove(e)
                    break
            elif flag == 1:
                if  y == y_enemy+1:
                    enemyList.remove(e)
                    break
            elif flag == 2:
                if  y == y_enemy:
                    enemyList.remove(e)
                    break
        play(coin)
        return 1  
    return 0

def moveEnemy(screen):
    for e in enemyList:
        if e.obstruct(screen):
            e.switch()
        if e.is_smart():
            x = e.retx()
            y = e.rety()
            if (screen.screen[x][y+1] == '0' or screen.screen[x][y+2] == 0) and e.what_state() == 1:
                e.switch()
        e.move(screen)
        e.draw(screen)
        e.clear(screen)