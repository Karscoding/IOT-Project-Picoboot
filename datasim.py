import pygame
from time import sleep
from databasevuller import app,Temperatuur,Afstand
import os

def run():
    templist=[]
    distlist=[]
    with app.app_context():
        for x in Temperatuur.query.all():
            datum=x.tijd
            templist.append((datum,x.temperatuur))
        for x in Afstand.query.all():
            distlist.append((x.afstand,x.nap))

    if len(templist) < 1:
        return 'foute templist'
    else:
        if os.getcwd().split("\\")[-1]=='Picoboot':
            '''Images'''
            image= pygame.image.load('./Images/noordpolderzijl.jpg')
            zand=pygame.image.load('./Images/zand.png')
            boat=pygame.image.load('./Images/boot.png')
            water= pygame.image.load('./Images/water.png')
            schuif=pygame.image.load('./Images/schuif.png')
            motor=pygame.image.load('./Images/motor.png')
        else:
            image= pygame.image.load('../Images/noordpolderzijl.jpg')
            zand=pygame.image.load('../Images/zand.png')
            boat=pygame.image.load('../Images/boot.png')
            water= pygame.image.load('../Images/water.png')
            schuif=pygame.image.load('../Images/schuif.png')
            motor=pygame.image.load('../Images/motor.png')

        '''Functions'''
        def background(image):
            size=pygame.transform.scale(image,(1920,1080))
            win.blit(size,(0,0))
        def add_boat(boat):
            size=pygame.transform.scale(boat,(600,300))
            win.blit(size,(bootx,waterlevel-200))
        def add_motor(motor):
            size=pygame.transform.scale(motor,(100,100))
            win.blit(size,(bootx+100,waterlevel))
        def add_zand(zand,x,y):
            size=pygame.transform.scale(zand,(100,1000))
            win.blit(size,(x,y))
        def polder(image):
            size=pygame.transform.scale(image,(1920,1080))
            win.blit(size,(0,waterlevel))

        bootx=250
        nap=0
        waterlevel=537
        pygame.init()
        info = pygame.display.Info()
        SIZE = info.current_w, info.current_h
        win = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Data Simulator")

        pygame.font.init()
        my_font = pygame.font.SysFont('Arial', 40)

        def add_schuif(schuif,i):
            size=pygame.transform.scale(schuif,(100,200))
            zandhoogte=750-((distlist[i][0]-2)*50)
            win.blit(size,(bootx+550,zandhoogte-190))

        def genzand(offset):
            if offset==0:
                for i in range(8):
                    add_zand(zand,100*i,750)
                for i in range(len(distlist)):
                    add_zand(zand,800+(100*i),750-((distlist[i][0]-2)*50))
            else:
                for i in range(8):
                    add_zand(zand,(100*i)-offset*100,700)
                for i in range(len(distlist)):
                    add_zand(zand,(800+(100*i)-offset*100),750-((distlist[i][0]-2)*50))
                    add_zand(zand,((100*len(distlist))+(100*i)-offset*100),750)

        def myround(x, base=5):
            return base * round(x/base)

        for i in range(len(templist)):
            temp= templist[i]
            afst= distlist[i]
            waterlevel= myround(537 - (afst[1]*38),1)   

            background(image)
            genzand(i)
            polder(water)
            add_boat(boat)
            add_schuif(schuif,i)
            add_motor(motor)

            temperatuur = my_font.render(f"Tijd: {temp[0]}, Temperatuur: {temp[1]}, Afstand: {afst[0]}, NAP: {afst[1]}" , False, (0, 0, 0))
            win.blit(temperatuur, (0,0))
            
            pygame.display.update()
            
            sleep(1)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    exit()

if __name__=="__main__":
    run()