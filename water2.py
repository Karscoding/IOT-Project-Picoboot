import pygame

def simulator(x,y):
    pygame.init()
    info = pygame.display.Info()
    SIZE = info.current_w, info.current_h

    # flags = pygame.DOUBLEBUF | pygame.FULLSCREEN
    win = pygame.display.set_mode(SIZE)

    pygame.display.set_caption("Water Simulator")

    vel=5
    sy=0

    image= pygame.image.load('noordpolderzijl.jpg')
    def background(image):
        size=pygame.transform.scale(image,(1920,1080))
        win.blit(size,(0,0))

    zand=pygame.image.load('zand.png')
    def add_zand(zand):
        size=pygame.transform.scale(zand,(1920,200))
        win.blit(size,(0,800))

    boat=pygame.image.load('boot.png')
    def add_boat(boat):
        size=pygame.transform.scale(boat,(600,200))
        win.blit(size,(x,y-50))

    water= pygame.image.load('water.png')
    def polder(image):
        size=pygame.transform.scale(image,(1920,1080))
        win.blit(size,(0,y))

    schuif=pygame.image.load('schuif.png')
    def add_schuif(schuif):
        size=pygame.transform.scale(schuif,(100,150))
        win.blit(size,(x+550,y-sy))


    mnr=1
    motor=pygame.image.load('motor.png')
    greenmotor=pygame.image.load('motorgeel.png')
    def add_motor(motor):
        size=pygame.transform.scale(motor,(100,100))
        win.blit(size,(x+100,y-50))

    # Define color constants
    BLACK = (0, 0, 0)
    WHITE=(255,255,255)

    '''run=True

    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type== pygame.quit:
                run=False

        
        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP] and y >500:
            y-=vel

        if keys[pygame.K_DOWN] and y < 700:
            y+=vel
        
        if keys[pygame.K_q]:
            pygame.quit()

        if mnr==0:
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

        if keys[pygame.K_RIGHT]:
                if x+vel==1000:
                    x=x
                else:
                    x+=vel
            
            if keys[pygame.K_LEFT]:
                if x+vel==100:
                    x=x
                else:
                    x-=vel
            
        if keys[pygame.K_SPACE]:
            if mnr ==1:
                mnr=0
                sleep(0.1)
            elif mnr==0:
                mnr=1 
                sleep(0.1)'''
        
    background(image)
    add_zand(zand)
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
    pygame.draw.rect(win, BLACK, (x+300, y-20, 150, 50))
    win.blit(text, (x+300, y))    

    pygame.display.update()

