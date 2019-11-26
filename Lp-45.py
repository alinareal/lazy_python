# A small and hungry python

import pygame, random, sys, time


def privet():
    error = pygame.init()
    if error[1] == 0:
        print "Hello! It's been a rainy summer, so the weather is not that important so far."
    else:
        print "Errors detected!"
        sys.exit()
privet()

playSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("A small and hungry python")
time.sleep(56)

position = [50, 50]  # Python's coordinates
body = [[80, 50], [70, 50], [60, 50]]  # Python's structure
bait = [random.randrange(1, 80)*10, random.randrange(1, 60)*10]
baitVisible = True
fpsController = pygame.time.Clock()
direction = "RIGHT"
changeto = direction
score = 0

white = pygame.Color(255, 255, 255)  # Background
black = pygame.Color(0, 0, 0)  # The end of the game
red = pygame.Color(255, 0, 0)  # Fount
green = pygame.Color(0, 255, 0)  # Python
blue = pygame.Color(0, 0, 255)
lightslateblue = pygame.Color(132, 112, 255)  # Food


def music():
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(0)

def gameOver():
    gaOFont = pygame.font.SysFont('Garamond', 48)
    gaOSurface = gaOFont.render('Game over!', True, red)
    gaORectangular = gaOSurface.get_rect()
    gaORectangular.midtop = (400, 25)
    playSurface.blit(gaOSurface, gaORectangular)
    showScore(2)
    pygame.display.flip()
    time.sleep(8)
    pygame.quit()
    sys.exit()


def showScore(choice=1):
    scoreFont = pygame.font.SysFont('Garamond', 24)
    scoreSurface = scoreFont.render('Score: {0}'.format(score), True, red)
#   scoreSurface = scoreFont.render('Score:' + str(score), True, red)
    scoreRectangular = scoreSurface.get_rect()
    if choice == 1:
        scoreRectangular.midtop = (50, 25)
    else:
        scoreRectangular.midtop = (400, 125)
    playSurface.blit(scoreSurface, scoreRectangular)
    # pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = "LEFT"
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = "UP"
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = "DOWN"
            if event.key == pygame.K_ESCAPE:
                #pygame.event.post(pygame.event.Event(QUIT))
                gameOver()
            if event.key == ord('m'):
                music()

# Work with directions of Python
    if direction != "LEFT" and changeto == "RIGHT":
        direction = "RIGHT"
    if direction != "RIGHT" and changeto == "LEFT":
        direction = "LEFT"
    if direction != "DOWN" and changeto == "UP":
        direction = "UP"
    if direction != "UP" and changeto == "DOWN":
        direction = "DOWN"
# Change of position depending on the direction
    if direction == "RIGHT":
        position[0] += 10
    if direction == "LEFT":
        position[0] -= 10
    if direction == "UP":
        position[1] -= 10
    if direction == "DOWN":
        position[1] += 10


# Work with the length of python
    body.insert(0, list(position))
    if position[0] == bait[0] and position[1] == bait[1]:
        baitVisible = False
        score += 1
    else:
        body.pop()
# Visuality of food
    if baitVisible == False:
        baitVisible = True
        bait = [random.randrange(1, 80) * 10, random.randrange(1, 60) * 10]

    playSurface.fill(white)

    for element in body:
        pygame.draw.rect(playSurface, green, pygame.Rect(element[0], element[1], 10, 10))

# Drawing food
    pygame.draw.rect(playSurface, lightslateblue, pygame.Rect(bait[0], bait[1], 10, 10))

# Not to come out of screen
    if position[0] > 790 or position[0] < 0:
        position[0] = 400
    if position[1] > 590 or position[1] < 0:
        position[1] = 300
# Not to eat himself
    for element in body[1: ]:
        if position[0] == element[0] and position[1] == element[1]:
            position = [50, 50]  # Python's coordinates
            body = [[80, 50], [70, 50], [60, 50]]  # Python's structure


    showScore()
    pygame.display.flip()
    fpsController.tick(12)
# gameOver()
