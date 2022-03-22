# Modules 
import pygame
import math



# Main

height = 600
width = 600

c = (0,150,255)

pygame.init()
win = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()

# Images
white = [ 255,255,255]
black = [ 0,0,0]
bg = pygame.image.load('back.png')

# fill

d1 = 0
d2 = 0

# Variables
run = True

# Functions

def redraGameWindow():
    win.fill(white)
    #win.blit(bg, (0, 0))
     
"""
def drawrect():
    #
"""
# Main loop
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    redraGameWindow()

    # Actions
    
    if keys[pygame.K_SPACE]:
        run = False
    
    if keys[pygame.K_a]:
        d1 = d1 + 1

    if keys[pygame.K_s]:
        d2 = d2 + 1
 
    
    mk = (0 + 50 * d1,0 + 50 * d2, 50, 50)
    
    # Grid
    for x in range(0,600,50):
    
        pygame.draw.line(win,c,(1,x),(600,x), 2)
        pygame.draw.line(win,c,(x,1),(x,600), 2)
        
            
    pygame.draw.rect(win, black, mk, 0)
    
    
    pygame.display.update()

    
    #print("test")
    #checkColision(x, y, widht, height)
    
 

#pygame.display.update()
pygame.quit()
