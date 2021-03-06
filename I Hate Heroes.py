import pygame
import random
import sys
import time
import multiprocessing
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

SiGongJoA = pygame.image.load('heroes.png')
pygame.display.set_icon(SiGongJoA)

width, height = 640, 480    #화면크기 설정
howManySigong = 7   #난이도 설정 (낮을수록 쉽고 높을수록 어렵습니다)

class Heroes:
    heroes = pygame.image.load('heroes.png')
    heroesSize = heroes.get_rect().size
    heroesX = 0
    heroesY = -height
    heroesSpeed = 7

def GetHeroesSpeed():
    return random.randrange(7,20)
    
def gameover():
    #pygame.mixer.music.stop()
    #배경음악 관련된 코드입니다. 저작권 문제로 깃허브에는 업로드 하지 않겠습니다.
    messagebox.showinfo("Game Over", "시공속으로 빨려들어갔습니다\n\n\n점수 : %d" % gamePoint)
    sys.exit()

def paintEntity(entity, x, y):
    monitor.blit(entity, (x, y))

def playGame():
    global monitor, person, gamePoint
    gamePoint = 0
    personX = width/2 - (personSize[0]/2)
    dx = 0
    hms = howManySigong

    SG = [0] * hms
    '''
    pygame.mixer.music.load('bgm.mp3')
    pygame.mixer.music.play(-1)
    #배경음악 관련된 코드입니다. 저작권 문제로 깃허브에는 업로드 하지 않겠습니다.
    '''
    for i in range(0,hms):
        SG[i] = Heroes()
        SG[i].heroesX = random.randrange(0,width-70)
        SG[i].heroesSpeed = random.randrange(5,15)
    
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

        for i in range(0, hms):
            SG[i].heroesY += SG[i].heroesSpeed
            if SG[i].heroesY > height:
                SG[i].heroesY = -SG[i].heroesSize[0]
                SG[i].heroesX = random.randrange(0,width-SG[i].heroesSize[0])
                SG[i].heroesSpeed = GetHeroesSpeed()
                gamePoint += 1

            paintEntity(SG[i].heroes, SG[i].heroesX, SG[i].heroesY)
            if (height - 120 < SG[i].heroesY < height-20):
                if (personX < SG[i].heroesX + 55) and (SG[i].heroesX < personX + 25):
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