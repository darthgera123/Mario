import os
from player import Player
from enemy import Enemy
from background import Screen
from board import Board


health = 3
count = 0
enemy_kill = 0
score = count*10 + (enemy_kill*30)
coin_count = int(0)

iter =0
dir =0
iter_count = 0
speed = 50
enemyList = []
base = os.getcwd()
theme = base + '/theme.wav'
coin = base + '/coin.wav'
jump = base + '/jump.wav'
missions = {'Kill 5 enemies':False,'Collect 50 coins':False,'Score 500 points':False}
mission_comp = 0

screen = Screen()
board = Board()
enemy =  Enemy()

player = Player(16)