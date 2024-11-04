# Import
import pgzrun
import random
#Screen Settings 
WIDTH = 500
HEIGHT = 500
# Game
Score = 0
Gameover = False
# Characters
Bee = Actor("bee")
Bee.pos = 100,100
Flower = Actor("flower")
Flower.pos = 200,200
def draw():
    screen.blit("green",(0,0))
    Bee.draw()
    Flower.draw()
    screen.draw.text("Score"+ str(Score),topleft = (15,15))


    if Gameover: 
        screen.fill("Blue")
        screen.draw.text("Time is up and Your final score is..."+ str(Score))

def place_flower():
    Flower.x = random.randint(50,WIDTH-50)
    Flower.y = random.randint(50,WIDTH-50) 
def time_up():
    global Gameover
    Gameover = True
def update():
    global Score
    if keyboard.left:
        Bee.x = Bee.x-2
    if keyboard.right:
        Bee.x = Bee.x+2
    if keyboard.up:
        Bee.y = Bee.y-2
    if keyboard.down:
        Bee.y = Bee.y+2
    Flower_collected = Bee.colliderect(Flower)
    if Flower_collected:
        Score = Score+10
        place_flower()
clock.schedule(time_up,120.0)
pgzrun.go() 