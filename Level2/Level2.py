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
sprinkX = 1875
sprinkY = 20
donutX = 750
donutY = 0
lives = 20

#Images
donut = pygame.image.load("donut.png")
rat = pygame.image.load("rat.png")
sprinkles = pygame.image.load("sprinkles.png")
explosion = pygame.image.load("explosion.png")
table = pygame.image.load("tabletop.png")
vert_rat = pygame.image.load("rat copy.png")
reversed_rat = pygame.image.load("reversed_rat.png")
sprinkle_donut = pygame.image.load("sprinkle_donut.png")
cat = pygame.image.load("cat.png")

#Resize images
donut = pygame.transform.scale(donut, (100, 100))
rat = pygame.transform.scale(rat, (300, 300))
sprinkles = pygame.transform.scale(sprinkles, (150, 75))
vert_rat = pygame.transform.scale(vert_rat, (200, 200))
explosion = pygame.transform.scale(explosion, (100, 100))
sprinkle_donut = pygame.transform.scale(sprinkle_donut, (400, 400))
cat = pygame.transform.scale(cat, (250, 250))

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
    message = font.render('{} lives left'.format(lives), False, (255, 255, 255))
    display.blit(message, (600, 300))

    #Rat movement conditions
    if ratX <= 1720 and ratY == 0:
        ratX += 75
    elif ratX >= 1720 and ratY in range(0, 400):
        ratY += 75
    elif ratX > 100 and ratY in range(400, 800):
        ratX -= 75
    elif ratX >= 0 and ratY in range(400, 800):
        ratY += 75
    elif ratX <= 1400 and ratY in range(800, 1200):
        ratX += 75

    #Sprinkle Movement Conditions
    if sprinkX > 750 and sprinkY in range(0, 200):
        sprinkX -= 75
    elif sprinkX <= 750 and sprinkY in range(0, 200):
        sprinkY = 420
    elif sprinkY == 420 and sprinkX <= width:
        sprinkX += 75
    elif sprinkX  >= width and sprinkY == 420:
        sprinkY = 820
    elif sprinkY == 820 and sprinkX > 750:
        sprinkX -= 75

    #All events happening by player
    for event in pygame.event.get():
        #If user quits in the middle
        if event.type == pygame.QUIT:
            won = True
        #Donut movement conditions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and donutX > 0:
                donutX -= 75
            elif event.key == pygame.K_RIGHT and donutX < width:
                donutX += 75
            elif event.key == pygame.K_UP and donutY > 0:
                donutY -= 75
            elif event.key == pygame.K_DOWN and donutY < height:
                donutY += 75

    #Refill Screen
    time.sleep(0.1)
    display.fill((0, 0, 0)) #Background

    #display.blit(donut, (donutX, donutY))
    display.blit(pygame.transform.scale(table, (1920, 200)), (0, 0))
    display.blit(pygame.transform.scale(table, (200, 400)), (1720, 0))
    display.blit(pygame.transform.scale(table, (1920, 200)), (0, 400))
    display.blit(pygame.transform.scale(table, (200, 400)), (0, 400))
    display.blit(pygame.transform.scale(table, (1920, 200)), (0, 800))
    display.blit(pygame.transform.scale(table, (200, 400)), (1720, 800))
    display.blit(sprinkles, (sprinkX, sprinkY))

    #Add explosions, sprinkle donuts or donuts based on player coordinates
    if donutY in range (200, 400) and donutX < 1720:
        display.blit(explosion, (donutX, donutY))
    elif donutY in range (600, 800) and donutX > 200:
        display.blit(explosion, (donutX, donutY))
    elif donutY in range(1000, height) and donutX < 1720:
        display.blit(explosion, (donutX, donutY))
    elif lives > 0 and donutX >= 1720 and donutY >= 900:
        display.blit(sprinkle_donut, (donutX, donutY))
    else:
        display.blit(donut, (donutX, donutY))

    #Adds the rat and/or cat based on ratX and ratY
    if ratX > 100 and ratY in range(400, 800):
        display.blit(reversed_rat, (ratX, ratY))
    elif (ratX >= 1720 and ratY in range(0, 400)) or (ratX >= 0 and ratY in range(400, 800)):
        display.blit(vert_rat, (ratX, ratY))
    elif ratX >= 1400 and ratY in range(800, 1000):
        display.blit(rat, (ratX, ratY))
        display.blit(cat, (ratX - 120, ratY- 100))
    else:
        display.blit(rat, (ratX, ratY))

    #Point loss conditions

    #If caught by rat
    if donutY in range(0, 200) and ratY in range(0, 200) and ratX == donutX:
        lives -=5
    elif donutY in range(400, 600) and ratY in range(400, 600) and ratX == donutX:
        lives -= 5
    elif donutY in range(800, 1000) and ratY in range(800, 1000) and ratX == donutX:
        lives -= 5

    #If donut runs into sprinkle
    elif donutY in range(0, 200) and sprinkY in range(0, 200) and donutX == sprinkX:
        lives -= 5
    elif donutY in range(400, 600) and sprinkY in range(400, 600) and donutX == sprinkX:
        lives -= 5
    elif donutY in range(800, 1000) and sprinkY in range(800, 1000) and donutX == sprinkX:
        lives -= 5

    #If donut falls off table
    elif donutY in range (200, 400) and donutX < 1720:
        lives -= 1
    elif donutY in range (600, 800) and donutX > 200:
        lives -= 1
    elif donutY in range(1000, height) and donutX < 1720:
        lives -= 1

    if lives <= 0 and donutX < 1720 and donutY < 900: #Loss condition
        message = font.render('Sorry, you ran out of points', False, (255, 255, 255))
        display.blit(message, (600, 300))

    elif lives > 0 and donutX >= 1720 and donutY >= 800: #Win condition
        time.sleep(1)
        display.fill((0, 0, 0))
        message = font.render('LEVEL BEATEN', False, (255, 255, 255))
        display.blit(message, (800, 200))
        display.blit(sprinkle_donut, (740, 300))
        message = font.render('You got all the sprinkles with {} lives remaining'.format(lives), False, (255, 255, 255))
        display.blit(message, (530, 700))

    else: #If game is not won or lost yet
        message = font.render('{} lives left'.format(lives), False, (255, 255, 255))
        display.blit(message, (600, 300))

pygame.quit()
