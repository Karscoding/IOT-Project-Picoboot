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

x=500
y=500

vel=5


run=True


image= pygame.image.load('noordpolderzijl.jpg')
def background(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,0))

zand=pygame.image.load('zand.png')
def add_zand(zand):
    size=pygame.transform.scale(zand,(1920,200))
    win.blit(size,(0,700))

boat=pygame.image.load('boot.png')
def add_boat(boat):
    size=pygame.transform.scale(boat,(600,300))
    win.blit(size,(x,y-200))

water= pygame.image.load('water.png')
def polder(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,y))

schuif=pygame.image.load('schuif.png')
def add_schuif(schuif):
    global y
    size=pygame.transform.scale(schuif,(100,150))
    if y>575:
        sy=y-(y-575)
    else:
        sy=y
    win.blit(size,(x+550,sy))

mnr=1
motor=pygame.image.load('motor.png')

def add_motor(motor):
    size=pygame.transform.scale(motor,(100,100))
    win.blit(size,(x+100,y))

# Define color constants
BLACK = (0, 0, 0)
WHITE=(255,255,255)

run=True

def runengine():
    global y
    global run
    global mnr
    global x

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

        '''# Draw black box around "esp" text
        font = pygame.font.SysFont(None, 25)
        text = font.render("Computer/ESP", True, WHITE)
        pygame.draw.rect(win, BLACK, (x+300, y-20, 150, 50))
        win.blit(text, (x+300, y))    '''

        pygame.display.update()

def adjusttide():
     global y
     global run
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
            if i == 10:
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
            sleep(1)


thread1=threading.Thread(target=runengine).start()
thread2 = threading.Thread(target=adjusttide).start()


