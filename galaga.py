import pgzrun
import random

HEIGHT = 600
WIDTH = 600

ship = Actor("galaga")
bug = Actor("bug")
bullet = Actor("bullet")

ship.pos = (WIDTH/2,HEIGHT-60)
speed = 5
bullets = []
enemies = []
enemies.append(bug)
enemies [-1].x = 10
enemies [-1].y = -100
score = 0
enemies_speed = 0.5
def show_score():
    screen.draw.text(str(score),(3,4))

def on_key_down(key):
    if key == keys.UP:
        bullets.append(bullet)
        bullets [-1].x = ship.x
        bullets [-1].y = ship.y

def update():
    global score
    if keyboard.left:
        ship.x-= speed
        if ship.x <= 0:
            ship.x = 0
    elif keyboard.right:
        ship.x+= speed
        if ship.x >= 600:
            ship.x = 600
    for bullet in bullets[:]:
        bullet.y-=10
        if bullet.y<0:
            bullets.remove(bullet)
    for enemie in enemies[:]:
        enemie.y+=enemies_speed
        if enemie.y >HEIGHT:
            enemie.y = random.randint(-100,-50)
            enemie.x = random.randint(100 , 590)
        for bullet in bullets[:]:
            if enemie.colliderect(bullet):
                score = score+1
                bullets.remove(bullet)
                enemies.remove(enemie)
                new_enemie = Actor("bug")
                new_enemie.y = random.randint(-100,-50)
                new_enemie.x = random.randint(100 , 590)
                enemies.append(new_enemie)
        if ship.colliderect(enemie):
            print("Game Over")
            exit()
def draw():
    screen.clear()
    screen.fill("Blue")
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemie in enemies:
        enemie.draw()
    show_score()

pgzrun.go()