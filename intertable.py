import pgzrun
import itertools

# Screen Settup
HEIGHT = 600
WIDTH = 600

# Shape
Shapes = itertools.cycle([ "circle" , "square" ,"rectangle" ])
Current_Shape = next(Shapes)
def draw():
    screen.clear()
    screen.draw.text("Press Space to Change Shape",(0,0) )
    if Current_Shape == "circle":
        screen.draw.filled_circle((300,300), 100 ,"red")
    elif Current_Shape == "square":
        screen.draw.filled_rect(Rect((300,300),(100,100) ),"red")
    elif Current_Shape == "rectangle":
        screen.draw.filled_rect(Rect((300,300),(100,200)),"red")

def on_key_down(key):
    global Current_Shape
    if key == keys.SPACE:
        Current_Shape = next(Shapes)

pgzrun.go()