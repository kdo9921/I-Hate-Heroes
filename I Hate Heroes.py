import pygame
import random
import sys
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

SiGongJoA = pygame.image.load('heroes.png')
pygame.display.set_icon(SiGongJoA)


def paintEntity(entity, x, y):
    monitor.blit(entity, (x, y))

def getHX(twox):
    onex = random.randrange(0,width-70)
    if (onex < twox + 90) and (onex + 90 > twox):
        getHX(twox)
    return onex

def getH2X(onex):
    twox = random.randrange(0,width-70)
    if (twox < onex + 90) and (twox + 90 > onex):
        getH2X(onex)
    return twox

def playGame():
    global monitor, person, heroes
    personX = width/2 - (personSize[0]/2)
    dx = 0

    heroes = pygame.image.load('heroes.png')
    heroesSize = heroes.get_rect().size
    heroesX = random.randrange(0,width-heroesSize[0])
    heroesY = 0-heroesSize[0]
    heroesSpeed = random.randrange(5,10)

    heroes2 = pygame.image.load('heroes.png')
    heroes2Size = heroes.get_rect().size
    heroes2X = getH2X(heroesX)
    heroes2Y = 0-heroesSize[0]
    heroes2Speed = random.randrange(10,15)

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
        heroes2Y += heroes2Speed

        if heroesY > height:
            heroesY = -heroesSize[0]
            heroesX = getHX(heroes2X)
            heroesSpeed = random.randrange(7, 20)

        if heroes2Y > height:
            heroes2Y = -heroes2Size[0]
            heroes2X = getH2X(heroesX)
            heroes2Speed = random.randrange(7, 20)

        paintEntity(heroes, heroesX, heroesY)
        paintEntity(heroes2, heroes2X, heroes2Y)

        if (height - 120 < heroesY < height):
            if (personX < heroesX + 55) and (heroesX < personX + 25):
                messagebox.showinfo("Game Over", "시공속으로 빨려들어갔습니다")
                break

        if (height - 120 < heroes2Y < height):
            if (personX < heroes2X + 55) and (heroes2X < personX + 25):
                messagebox.showinfo("Game Over", "시공속으로 빨려들어갔습니다")
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