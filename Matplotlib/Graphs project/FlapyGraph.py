

import pygame
import math
import random
import matplotlib.pyplot as plt

pygame.init()
win = pygame.display.set_mode((288, 512))

Bird = [pygame.image.load('bird1.png'), pygame.image.load('bird2.png'), pygame.image.load('bird3.png')]
clock = pygame.time.Clock()
bg = pygame.image.load('bg.png')
pipe = pygame.image.load('pipe.png')
pipe2 = pygame.image.load('pipe2.png')


ran = random.random()
xtube = 288
ytube = 200 

widht = 34
height = 28

twidht = 52
theight = 320

x = 80
y = 411
ani = 0

aceleration = 0.3

score = 0
print(score)

position = []




class tube():
    def __init__(self, xtube, ytube, vel, ran):
        self.x = int(xtube)
        self.y = int(ytube)
        self.vel = int(vel)
        self.ran = int(ran)

    def Hitbox(self, xtube, ytube):
        self.hitbox = (xtube, ytube + 200, 52, 320)
        self.hitbox2 = (xtube, ytube - 200, 52, 320)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox2, 2)

    def DrawTube(self, x, y):
        win.blit(pipe, (x, y + 200))
        win.blit(pipe2, (x, y - 200))
        
        
    
class bird():
    def __init__(self, x, y, widht, height, speed):
        self.x = int(x)
        self.y = int(y)
        self.widht = int(widht)
        self.height = int(height)
        self.speed = int(speed)
        

    def Hitbox(self, x, y, widht, height):
        self.hitbox = (x, y, widht, height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


    def draw(self, x, y, ani, pace):
        Photo = Bird[int(ani)]
        win.blit(Photo, (x, y))
        
      


def redraGameWindow():
    win.blit(bg, (0, 0)) 
    font = pygame.font.SysFont("comicsans", 30, True)
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (50, 0))




def checkColision(x, y, widht, height):
    if xtube < x + widht:
        if xtube + twidht < x:
            pass
        else:
            if ytube + 200 > y + height - 5 and ytube - 200 + theight < y + 2:
                #print('nice')
                pass
            else:
                pygame.time.delay(1000)
                plt.show()
                pygame.quit()




#main loop-----------------------------
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    

    #Movement
    if y <= 490:
        if keys[pygame.K_SPACE]:
            y -= 10
            aceleration = 0.5
            position.append(int(- y))
            #print(position)
            
            plt.plot(position)
            plt.ylabel('some numbers')
            
            
        else:
            aceleration += 0.3
            y += aceleration
    else:
        pygame.time.delay(1000)
        run = False

    # tube wall detection
    if xtube <= 0:
        xtube = 288
        score += 1
        ran = random.random()
        ytube = ran * 200 
        print(ran)
        print(score)
        
    checkColision(x, y, widht, height)
        


    #animation
    if ani <= 2:
        ani += 0.5
    else:
        ani = 0

    #Tube Drawing

    xtube -= 3
    tubes = tube(100, ytube, 2, ran)
    
    tubes.DrawTube(xtube, ytube)
    

    #Bird mike 
    mike = bird(80, 441, 34, 28, 3)
    mike.draw(x, y, ani, 3)
    

    

    #mike.Hitbox(x, y, widht, height)
    #tubes.Hitbox(xtube, ytube)
    pygame.display.update()

    
    redraGameWindow()
    #checkColision(x, y, widht, height)
    


#pygame.display.update()
plt.show()
pygame.quit()


       #blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)
   


   
