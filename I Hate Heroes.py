import pygame
import random
import sys

def paintEntity(entity, x, y):
    monitor.blit(entity, (x, y))

def playGame():
    global monitor, person, heroes

    personX = width/2 - (personSize[0]/2)
    dx = 0

    heroes = pygame.image.load('heroes.png')
    heroesSize = heroes.get_rect().size
    heroesX = random.randrange(0,width-heroesSize[0])
    heroesY = 0-heroesSize[0]
    heroesSpeed = random.randrange(10,20)


    while True:
        (pygame.time.Clock()).tick(100)
        monitor.fill((50,50,60))

        for i in pygame.event.get():
            if i.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if i.type in [pygame.KEYDOWN]:
                if i.key == pygame.K_LEFT:
                    dx = -5
                elif i.key == pygame.K_RIGHT:
                    dx = +5

            if i.type in [pygame.KEYUP]:
                if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                    dx = 0

        if (0 < personX + dx and personX + dx <= width - personSize[0]):
            personX += dx

        paintEntity(person, personX, height-81)

        heroesY += heroesSpeed

        if heroesY > height:
            heroesY = -heroesSize[0]
            heroesX = random.randrange(0,width-heroesSize[0])
            heroesSpeed = random.randrange(10, 20)

        paintEntity(heroes, heroesX, heroesY)

        if (height - 150 < heroesY < height):
            if (personX < heroesX + 70) and (heroesX < personX + 40):
                print("Game Over\n시공속으로 빨려들어갔습니다)
                break

        pygame.display.update()

width, height = 400, 600
monitor = None
person, heroes, personSize = None, None, 0

pygame.init()
monitor = pygame.display.set_mode((width, height))
pygame.display.set_caption("시공시러")

person = pygame.image.load('person.png')
personSize = person.get_rect().size

playGame()