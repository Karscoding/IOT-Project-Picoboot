import pygame
from time import sleep
pygame.init()

win = pygame.display.set_mode((1920,1080))

pygame.display.set_caption("Water Simulator")

y=600
width=20
height=20
vel=5
sy=0

image= pygame.image.load('noordpolderzijl.jpg')
def background(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,0))

boat=pygame.image.load('boot.png')
def add_boat(boat):
    size=pygame.transform.scale(boat,(600,200))
    win.blit(size,(600,y-50))

water= pygame.image.load('water.png')
def polder(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,y))

schuif=pygame.image.load('schuif.png')
def add_schuif(schuif):
    size=pygame.transform.scale(schuif,(100,150))
    win.blit(size,(1150,y-sy))

mnr=1
motor=pygame.image.load('motor.png')
greenmotor=pygame.image.load('motorgeel.png')
def add_motor(motor):
    size=pygame.transform.scale(motor,(100,100))
    win.blit(size,(700,y-50))

# Define color constants
BLACK = (0, 0, 0)
WHITE=(255,255,255)

run=True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type== pygame.quit:
            run=False
    
    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP] and y >500:
        y-=vel

    if keys[pygame.K_DOWN] and y < 880 - height:
        y+=vel

    if keys[pygame.K_q]:
        pygame.quit()

    if keys[pygame.K_w]:
        if sy+vel== 60:
            sy=sy
        else:
            sy+=vel
    
    if keys[pygame.K_s]:
        if sy-vel == -20:
            sy=sy
        else: 
            sy-=vel

    if keys[pygame.K_SPACE]:
        if mnr ==1:
            mnr=0
            sleep(0.1)
        elif mnr==0:
            mnr=1 
            sleep(0.1)

    background(image)
    polder(water)
    add_boat(boat)
    add_schuif(schuif)
    if mnr==1:
        add_motor(motor)
    elif mnr==0:
        add_motor(greenmotor)
    
    # Draw black box around "esp" text
    font = pygame.font.SysFont(None, 25)
    text = font.render("Computer/ESP", True, WHITE)
    pygame.draw.rect(win, BLACK, (900, y-20, 150, 50))
    win.blit(text, (900, y))
    
    pygame.display.update()

pygame.quit()
