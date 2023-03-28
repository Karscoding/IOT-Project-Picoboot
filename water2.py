import pygame

pygame.init()

win = pygame.display.set_mode((1920,1080))

pygame.display.set_caption("Water Simulator")

y=600
width=20
height=20
vel=10


image= pygame.image.load('noordpolderzijl.jpg')
def background(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,0))

'''boat=pygame.image.load('boot.png')
def add_boat(boat):
    size=pygame.transform.scale(boat,(600,200))
    win.blit(size,(1920/2,1080/2))
'''

water= pygame.image.load('water.png')
def polder(image):
    size=pygame.transform.scale(image,(1920,1080))
    win.blit(size,(0,y))
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


    background(image)
    polder(water)

    pygame.display.update()

pygame.quit()