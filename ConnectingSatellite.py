# Import
import pgzrun
import random
import time

# Screen
HEIGHT = 500
WIDTH = 500

# Satellite
Satellites =[]
SLines = []

# Satellite No.
Number = 8
NextSatellite = 0
# Time
starttime = 0
endtime = 0
totaltime = 0

# Satellite Create
def create_Satellite():
    global starttime
    for i in range(Number):
        satellite = Actor("satellite")
        satellite.pos = random.randint(20,WIDTH-50),random.randint(20,HEIGHT-50)
        Satellites.append(satellite)
    starttime = time.time()
def update():
    pass

def draw():
    global totaltime
    num = 1
    screen.blit("background",(0,0))
    for i in Satellites:
        screen.draw.text(str(num),(i.pos[0],i.pos[1]+20)) 
        i.draw()
        num = num+1 
    for i in SLines:
        screen.draw.line(i[0],i[1],(255,255,255))
    if NextSatellite <Number:
        totaltime = time.time()-starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    
def on_mouse_down(pos):
    global NextSatellite,SLines
    if NextSatellite <Number:
        if Satellites[NextSatellite].collidepoint(pos):
            if NextSatellite:
                SLines.append((Satellites[NextSatellite-1].pos,Satellites[NextSatellite].pos))
                NextSatellite=NextSatellite+1
            else:
                SLines=[]
                NextSatellite=0
create_Satellite()
pgzrun.go()