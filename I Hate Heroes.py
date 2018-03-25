import pygame
import random
import sys
import multiprocessing
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

SiGongJoA = pygame.image.load('heroes.png')
pygame.display.set_icon(SiGongJoA)

width, height = 400, 600

class Heroes:
    heroes = pygame.image.load('heroes.png')
    heroesSize = heroes.get_rect().size
    heroesX = 0
    heroesY = 0 - heroesSize[0]
    heroesSpeed = 7

def GetHeroesSpeed():
    return random.randrange(7,20)
    
def gameover():
    messagebox.showinfo("Game Over", "시공속으로 빨려들어갔습니다")
    sys.exit()

def paintEntity(entity, x, y):
    monitor.blit(entity, (x, y))

def playGame():
    global monitor, person, heroes
    personX = width/2 - (personSize[0]/2)
    dx = 0

    h1 = Heroes()
    h2 = Heroes()
    h3 = Heroes()

    h1.heroesX = random.randrange(0,width-70)
    h2.heroesX = random.randrange(0,width-70)
    h3.heroesX = random.randrange(0,width-70)

    h1.heroesSpeed = random.randrange(5,10)
    h2.heroesSpeed = random.randrange(7,13)
    h3.heroesSpeed = random.randrange(10,15)

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

        h1.heroesY += h1.heroesSpeed
        h2.heroesY += h2.heroesSpeed
        h3.heroesY += h3.heroesSpeed

        if h1.heroesY > height:
            h1.heroesY = -h1.heroesSize[0]
            h1.heroesX = random.randrange(0,width-h1.heroesSize[0])
            h1.heroesSpeed = GetHeroesSpeed()

        if h2.heroesY > height:
            h2.heroesY = -h2.heroesSize[0]
            h2.heroesX = random.randrange(0,width-h2.heroesSize[0])
            h2.heroesSpeed = GetHeroesSpeed()
        
        if h3.heroesY > height:
            h3.heroesY = -h3.heroesSize[0]
            h3.heroesX = random.randrange(0,width-h3.heroesSize[0])
            h3.heroesSpeed = GetHeroesSpeed()

        paintEntity(h1.heroes, h1.heroesX, h1.heroesY)
        paintEntity(h2.heroes, h2.heroesX, h2.heroesY)
        paintEntity(h3.heroes, h3.heroesX, h3.heroesY)

        if (height - 120 < h1.heroesY < height):
            if (personX < h1.heroesX + 55) and (h1.heroesX < personX + 25):
                gameover()

        if (height - 120 < h2.heroesY < height):
            if (personX < h2.heroesX + 55) and (h2.heroesX < personX + 25):
                gameover()

        if (height - 120 < h3.heroesY < height):
            if (personX < h3.heroesX + 55) and (h3.heroesX < personX + 25):
                gameover()

        pygame.display.update()

monitor = None
person, personSize = None, 0

pygame.init()
monitor = pygame.display.set_mode((width, height))
pygame.display.set_caption("시.공.시.러!")

person = pygame.image.load('person.png')
personSize = person.get_rect().size

playGame()