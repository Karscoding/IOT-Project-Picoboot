import pygame
from time import sleep
import threading
import random

pygame.init()
info = pygame.display.Info()
SIZE = info.current_w, info.current_h

win = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Water Simulator")

ex=1080+600
x=500
y=500
vel=5
spawnenemy=False
run=True

'''Images'''
lucass= pygame.image.load('./Images/LucasBit.png')
image= pygame.image.load('./Images/noordpolderzijl.jpg')
zand=pygame.image.load('./Images/zand.png')
boat=pygame.image.load('./Images/boot.png')
enemy=pygame.image.load('./Images/boot2.png')
water= pygame.image.load('./Images/water.png')
schuif=pygame.image.load('./Images/schuif.png')
motor=pygame.image.load('./Images/motor.png')

'''Functions'''
def lucas(image):
    size= pygame.transform.scale(image,(150,200))
    win.blit(size,(x+200,y-250))
def background(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,0))
def add_zand(zand):
    size=pygame.transform.scale(zand,(1920,200))
    win.blit(size,(0,700))
def add_boat(boat):
    size=pygame.transform.scale(boat,(600,300))
    win.blit(size,(x,y-200))
def add_enemy(enemy):
    size=pygame.transform.scale(enemy,(600,200))
    win.blit(size,(ex,y-100))
def polder(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,y))
def add_schuif(schuif):
    global y
    size=pygame.transform.scale(schuif,(100,150))
    if y>575:
        sy=y-(y-575)
    else:
        sy=y
    win.blit(size,(x+550,sy))
def add_motor(motor):
    size=pygame.transform.scale(motor,(100,100))
    win.blit(size,(x+100,y))

# Define color constants
BLACK = (0, 0, 0)
WHITE=(124,252,0)
run=True

def runengine():
    global y
    global run
    global x
    global ex
    global spawnenemy
    i=0
    wy= random.randint(500,575)
    if abs(y-wy)<=50:
        if y-wy<0:
            wy+=50
        else: 
            wy-=50

    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    run=False
            
        background(image)
        add_zand(zand)
        polder(water)
        add_boat(boat)
        add_schuif(schuif)
        add_motor(motor)
        lucas(lucass)
        add_enemy(enemy)

        pygame.display.update()

        if y!=wy: #Als ze niet gelijk zijn
            if y-wy<0:
                y+=0.5 #boot omlaag
            elif y-wy>0:
                y-=0.5 #boot omhoog
        else: #als ze gelijk zijn
            i+=1
            if i == 12:
                run=False
            
            wy= random.randint(500,575)
            if abs(y-wy)<=50:
                if y-wy<0:
                    wy+=50
                else:
                    if wy-50 <=400:
                        wy=400 
                    else:
                        wy-=50
            if random.randint(0,0)==0:
                spawnenemy=True

        if spawnenemy:
            if ex>=-600:
                ex-=5
            else:
                spawnenemy=False
                ex= 1680


runengine()


