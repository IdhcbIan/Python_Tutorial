
import pygame
import math
import random

win = pygame.display.set_mode((288, 512))

Bird = [pygame.image.load('bird1.png'), pygame.image.load('bird2.png'), pygame.image.load('bird3.png')]
clock = pygame.time.Clock()
bg = pygame.image.load('bg.png')
pipe = pygame.image.load('pipe.png')
pipe2 = pygame.image.load('pipe2.png')

x = 80
y = 411
widht = 34
height = 28
vel = 5
speed = 1
action = 2
px = 288
ycor = random.random()
py = ycor * 100 + 200
by = ycor * 100 - 200
bx = 512
walkCount = 0
tube = 0
score = 0
"""
class tube():
    na
"""


def redraGameWindow():
    Animation = Bird[walkCount]
    win.blit(bg, (0, 0))  # makea the backgrond the png
    win.blit(Animation, (x, y))
    
    """
    if px and bx > - 52:
        win.blit(pipe, (px, py))
        win.blit(pipe2, (bx, by))
    """
    """
    else px < 10:
        px = 288
        win.blit(pipe, (px, py))
        win.blit(pipe2, (bx, by)
    """
        
    
   #pygame.display.update()



#main loop-----------------------------
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    """
    if y <= 512 - height:
        if keys[pygame.K_SPACE]:
            y -= 10
            speed = 1
            px -= 1
            pygame.time.delay(10)
             
            
    
        px -= 2 
        bx = px        
        speed += 0.3
        y = y + speed
        
    if px and bx > - 52:
        redraGameWindow()
        pygame.display.update()
    
    if walkCount >= 2:
        walkCount=0
    else:
        walkCount += 1
        pygame.display.update()
    """
    redraGameWindow()



#pygame.display.update()
pygame.quit()









