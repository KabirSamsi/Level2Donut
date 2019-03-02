import pygame
import time
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Times', 50)

#Pygame variables
width = 1920
height = 1080
display = pygame.display.set_mode((width, height)) #Window size
clock = pygame.time.Clock() #Game clock (for programmer's use)
pygame.display.set_caption("Sprinkle Chase") #Window title

#Game variables
won = False
lost = False
ratX = 0
ratY = 0
sprinkX = width
sprinkY = 0
donutX = 800
donutY = 0
score = 20

#Images
donut = pygame.image.load("donut.png")
rat = pygame.image.load("rat.png")
sprinkles = pygame.image.load("sprinkles.png")
explosion = pygame.image.load("explosion.png")
table = pygame.image.load("tabletop.png")
vert_rat = pygame.image.load("rat copy.png")
reversed_rat = pygame.image.load("reversed_rat.png")

#Resize images
donut = pygame.transform.scale(donut, (100, 100))
rat = pygame.transform.scale(rat, (300, 300))
sprinkles = pygame.transform.scale(sprinkles, (150, 75))
vert_rat = pygame.transform.scale(vert_rat, (200, 200))
explosion = pygame.transform.scale(explosion, (100, 100))

display.fill((0, 0, 0)) #Background

#Table maze
display.blit(pygame.transform.scale(table, (1920, 200)), (0, 0))
display.blit(pygame.transform.scale(table, (200, 400)), (1720, 0))
display.blit(pygame.transform.scale(table, (1920, 200)), (0, 400))
display.blit(pygame.transform.scale(table, (200, 400)), (0, 400))
display.blit(pygame.transform.scale(table, (1920, 200)), (0, 800))
display.blit(pygame.transform.scale(table, (200, 400)), (1720, 800))

while not won:
    #Game loop
    pygame.display.update()
    clock.tick(700)

    #Display donut, sprinkles and rat
    display.blit(donut, (donutX, donutY))
    display.blit(sprinkles, (sprinkX, sprinkY))
    display.blit(rat, (ratX, ratY))
    message = font.render('{} point(s) left'.format(score), False, (255, 255, 255))
    display.blit(message, (600, 300))

    #Rat movement conditions
    if ratX <= 1800 and ratY == 0:
        ratX += 100
    elif ratX >= 1800 and ratY in range(0, 400):
        ratY += 100
    elif ratX > 100 and ratY in range(400, 800):
        ratX -=100
    elif ratX >= 0 and ratY in range(400, 800):
        ratY += 100
    elif ratX >= 1800 and ratY in range(800, 1200):
        ratX += 100

    #Sprinkle Movement Conditions
    if sprinkX > 800 and sprinkY in range(0, 200):
        sprinkX -= 50
    elif sprinkX <= 800 and sprinkY in range(0, 200):
        sprinkY = 400
    elif sprinkY == 400 and sprinkX <= width:
        sprinkX += 50
    elif sprinkX  >= width and sprinkY == 400:
        sprinkY = 800
    elif sprinkY == 800 and sprinkX > 800:
        sprinkX -= 50

    #All events happening by player
    for event in pygame.event.get():
        #If user quits in the middle
        if event.type == pygame.QUIT:
            won = True
        #Donut movement conditions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and donutX > 0:
                donutX -= 50
            elif event.key == pygame.K_RIGHT and donutX < width:
                donutX += 50
            elif event.key == pygame.K_UP and donutY > 0:
                donutY -= 50
            elif event.key == pygame.K_DOWN and donutY < height:
                donutY += 50

    #Refill Screen
    time.sleep(0.01)
    display.fill((0, 0, 0)) #Background

    #display.blit(donut, (donutX, donutY))
    display.blit(pygame.transform.scale(table, (1920, 200)), (0, 0))
    display.blit(pygame.transform.scale(table, (200, 400)), (1720, 0))
    display.blit(pygame.transform.scale(table, (1920, 200)), (0, 400))
    display.blit(pygame.transform.scale(table, (200, 400)), (0, 400))
    display.blit(pygame.transform.scale(table, (1920, 200)), (0, 800))
    display.blit(pygame.transform.scale(table, (200, 400)), (1720, 800))
    display.blit(sprinkles, (sprinkX, sprinkY))

    #Add explosions or donuts based on player coordinates
    if donutY in range (200, 400) and donutX < 1720:
        display.blit(explosion, (donutX, donutY))
    elif donutY in range (600, 800) and donutX > 200:
        display.blit(explosion, (donutX, donutY))
    else:
        display.blit(donut, (donutX, donutY))

    #Adds the rat based on ratX and ratY
    if ratX > 100 and ratY in range(400, 800):
        display.blit(reversed_rat, (ratX, ratY))
    elif (ratX >= 1800 and ratY in range(0, 400)) or (ratX >= 0 and ratY in range(400, 800)) or (ratX >= 1800 and ratY in range(1800, 1080)):
        display.blit(vert_rat, (ratX, ratY))
    else:
        display.blit(rat, (ratX, ratY))

    #Point loss condition
    if donutY in range(200, 400) and ratY == donutY:
        score -=5
    elif donutY in range(600, 800) and ratY == donutY:
        score -= 5
    elif donutX == ratX:
        score -= 5
    elif donutX == sprinkX:
        score -= 5
    elif donutY in range (200, 400) and donutX < 1720:
        score -= 1
    elif donutY in range (600, 800) and donutX > 200:
        score -= 1

    message = font.render('{} point(s) left'.format(score), False, (255, 255, 255))
    display.blit(message, (600, 300))

pygame.quit()
