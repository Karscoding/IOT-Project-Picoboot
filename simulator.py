import pygame
from time import sleep
import threading
import random
pygame.init()
info = pygame.display.Info()
SIZE = info.current_w, info.current_h

# flags = pygame.DOUBLEBUF | pygame.FULLSCREEN
win = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Water Simulator")

ex=1080+600
x=500
y=500

vel=5

spawnenemy=False
run=True


lucass= pygame.image.load('./Images/LucasBit.png')
def lucas(image):
    size= pygame.transform.scale(image,(150,200))
    win.blit(size,(x+200,y-250))

image= pygame.image.load('./Images/noordpolderzijl.jpg')
def background(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,0))

zand=pygame.image.load('./Images/zand.png')
def add_zand(zand):
    size=pygame.transform.scale(zand,(1920,200))
    win.blit(size,(0,700))

boat=pygame.image.load('./Images/boot.png')
def add_boat(boat):
    size=pygame.transform.scale(boat,(600,300))
    win.blit(size,(x,y-200))

enemy=pygame.image.load('./Images/boot2.png')
def add_enemy(enemy):
    size=pygame.transform.scale(enemy,(600,200))
    win.blit(size,(ex,y-100))

water= pygame.image.load('./Images/water.png')
def polder(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,y))

schuif=pygame.image.load('./Images/schuif.png')
def add_schuif(schuif):
    global y
    size=pygame.transform.scale(schuif,(100,150))
    if y>575:
        sy=y-(y-575)
    else:
        sy=y
    win.blit(size,(x+550,sy))

mnr=1
motor=pygame.image.load('./Images/motor.png')

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
    global mnr
    global x
    global ex

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
        add_enemy(enemy)
        lucas(lucass)


        pygame.display.update()

def adjusttide():
     global y
     global run
     global spawnenemy
     global ex
     i=0
     wy= random.randint(500,575)
     if abs(y-wy)<=50:
        if y-wy<0:
            wy+=50
        else: 
            wy-=50

     while run:
        if y!=wy:
            if y-wy<0:
                y+=1
                sleep(0.01)
            elif y-wy>0:
                y-=1
                sleep(0.01)
        else:
            i+=1
            if i == 2:
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
            sleep(3)
            if random.randint(0,4)==0:
                if spawnenemy==False:
                    spawnenemy=True
                    threading.Thread(target=spawne).start()


def spawne():
    global y
    global ex
    global spawnenemy

    while spawnenemy and ex>=-600:
        print('')
        ex-=0.2
        circle_pos = (x+465, y-185)
        circle_radius = 15
        pygame.draw.circle(win, WHITE, circle_pos, circle_radius)
    spawnenemy=False
    ex=1080+600

            


thread1 = threading.Thread(target=runengine).start()
thread2 = threading.Thread(target=adjusttide).start()


