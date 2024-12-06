# Game Date : 6 december 2024

# Import 
import pgzrun
import random 

#Screen Settings 
WIDTH = 800
HEIGHT = 800
Centerx = WIDTH/2
Centery = HEIGHT/2
Center = (Centerx , Centery)
# Game Setting
Finallevel = 4
Startspeed = 10
# Game items
Recycle_items = ["battery","bag","chips","bottle"]
Game_Complete = False 
Game_over = False
Current_level = 1
items = []
# Making the Game
def draw():
    global items , Current_level , Game_over , Game_Complete
    screen.clear()
    screen.blit("bground",(0,0))
    if Game_Complete:
        display_message("GoodJob you won the game")
    elif Game_over:
        display_message("Game over try again")
    else:
        for i in items:
            i.draw()
def update():
    global items
    if len(items) == 0:
        items = make_items(Current_level)