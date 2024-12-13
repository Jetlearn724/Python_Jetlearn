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
        display_message("GoodJob","you won the game")
    elif Game_over:
        display_message("Game over","try again")
    else:
        for i in items:
            i.draw()
def update():
    global items
    if len(items) == 0:
        items = item_make(Current_level)

def item_make(number_of_extra_items):
    item_to_create = ["paper"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(Recycle_items)
        item_to_create.append(random_option)
    new_item = create_item( item_to_create )
    layout_item(new_item)
    return new_item

def create_item(item_to_create):
    new_item = []
    for f in item_to_create:
        item = Actor(f+"img")
        new_item.append(item)
    return new_item
def layout_item(item_to_layout):
    gaps = len(item_to_layout)+1
    gap_size = WIDTH/gaps
    random.shuffle(item_to_layout)
    for index,item in enumerate(item_to_layout):
        new_x_position = (index+1)*gap_size
        item.x = new_x_position

def handle_game_over():
    global Game_over
    Game_over = True
def on_mouse_down(pos):
    global items , Current_level
    for e in items:
        if e.collidepoint(pos):
            if "paper" in e.image:
                handle_game_Complete()
            else:
                handle_game_over()
def handle_game_Complete():
    global Current_level,items,Game_Complete
    if Current_level == Finallevel:
        Game_Complete = True
    else:
        Current_level+=1 
        items =[]
def display_message(text,sub_text):
    screen.draw.text(text,fontsize = 60,center=Center,color="white")
    screen.draw.text(sub_text,fontsize = 30,center=(Centerx,Centery+30),color="white")

pgzrun.go()