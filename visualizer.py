__author__ = 'Alexandre & Romain & Laura'

#import sdl2
# import audioread
import OpenGL
# import tkinter.filedialog
#
# def main():
#
#     filepath = tkinter.filedialog.askopenfile(mode="r").name
#     print("Filepath = ", filepath)
#     audiofile = audioread.audio_open(filepath)
#     print("Lenght = ",  audiofile.duration)
#
#
# main()

from OpenGL.GL import *
from OpenGL.GLUT import *
import time
import pygame
import sys
from pygame.locals import *

# ---------------------- Init

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

# ------------- TO CHANGE
pathSound = 'C:\\Users\Romain\Music\\test'
# -----------------------

pathButton = 'C:\\Users\Romain\Pictures\projectPY'
pathBackground = 'C:\\Users\Romain\Pictures\projectPY'

gameScreen = pygame.display.set_mode((500, 500))

btnstart = pygame.image.load(pathButton + '\\btnstart.png')
backgrd = pygame.image.load(pathBackground + '\\blackscreen.png')
anim1 = pygame.image.load(pathBackground + '\\anim.png')
anim2 = pygame.image.load(pathBackground + '\\anim2.png')
player = pygame.image.load(pathBackground + '\playerVM.png')
mu0 = pygame.image.load(pathButton + '\\btnmusic.png')
mu1 = pygame.image.load(pathButton + '\\btnmusic2.png')
mu2 = pygame.image.load(pathButton + '\\btnmusic.png')
mu3 = pygame.image.load(pathButton + '\\btnmusic2.png')
mu4 = pygame.image.load(pathButton + '\\btnmusic.png')
muContour = pygame.image.load(pathButton + '\\contourr.png')

musicList = [mu0, mu1, mu2, mu3, mu4, muContour]
pressed = False


pygame.mouse.set_visible(True)

keyList = [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r]

# pygame.mixer.music.set_volume(0.5)


# ----------------- Functionalities

def button_func(x, y, w, h, imgSurf, function_call=None):
    mousepos = pygame.mouse.get_pos()
    mouseclick = pygame.mouse.get_pressed()
    gameScreen.blit(imgSurf, (x,y))
    rect = pygame.Rect(x,y,w,h)
    global pressed
    if rect.collidepoint(mousepos):
        if mouseclick[0] == 1 and not(pressed):
            function_call()
            pressed = True
        elif mouseclick[0] == 0:
            pressed = False

# ----------------- Animation


# # window = 0                                             # glut window number
# width, height = 1000, 1000                               # window size
# right = 100
# left = 100
# recx = 10
# recy = 10
# velx = 24
# vely = 22
#
# def refresh2d(width, height):
#     glViewport(0, 0, width, height)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()
#
# def draw_rect(x, y, width, height):
#     glBegin(GL_QUADS)                                  # start drawing a rectangle
#     glVertex2f(x, y)                                   # bottom left point
#     glVertex2f(x + width, y)                           # bottom right point
#     glVertex2f(x + width, y + height)                  # top right point
#     glVertex2f(x, y + height)                          # top left point
#     glEnd()
#
#
#
# def draw():
#     global recx
#     global recy
#     global velx
#     global vely                                         # ondraw is called all the time
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
#     glLoadIdentity()
#     refresh2d(width, height)                                  # reset position
#
#
#     glColor3f(0.0, 0.0, 1.0)
#
#     #while  xaxis < 200 and yaxis < 200:
#
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
#
#     draw_rect(recx, recy, right, left)
#     draw_rect(recx + 100, recy - 100, right - 50, left - 50)
#
#
#
#     recx = recx + velx
#     recy = recy + vely
#     # ToDo draw rectangle
#     if recx < 0:
#         velx = 24
#     if recy < 0:
#         vely = 22
#     if recx > 1000:
#         velx = -24
#     if recy > 1000:
#         vely = -22
#
#
#     glutSwapBuffers()                                  # important for double buffering
#
#
# # initialization
# glutInit()                                                 # initialize glut
# glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
# glutInitWindowSize(width, height)                          # set window size
# #glutInitWindowPosition(0, 0)                              # set window position
# # window = glutCreateWindow("Display Window")              # create window with title
#                                                            # start everything


def animation(animart, xsize, ysize):
    velx = 10
    vely = 8
    x = xsize
    y = ysize
    while True:
        if x < 20:
            velx = 10
        if y < 20:
            vely = 8
        if y > 480:
            vely = -10
        if x > 480:
            velx = -8
        x += velx
        y += vely
        gameScreen.blit(animart, (x, y))

# ----------------- Music Player System

def music(nbr):
    pygame.mixer.music.stop()
    if nbr == 0:
        menuMusic = pygame.mixer.music.load(pathSound + '.mp3')
    if nbr == 1:
        optionMusic = pygame.mixer.music.load(pathSound + '2.mp3')
    if nbr == 2:
        optionMusic = pygame.mixer.music.load(pathSound + '.mp3')
    if nbr == 3:
        optionMusic = pygame.mixer.music.load(pathSound + '2.mp3')
    if nbr == 4:
        optionMusic = pygame.mixer.music.load(pathSound + '.mp3')
    if nbr == 5:
        optionMusic = pygame.mixer.music.load(pathSound + '2.mp3')
    pygame.mixer.music.play(-1, 0.0)


def ipodSelect(x,y,musi, currentMusic):
    mousepos = pygame.mouse.get_pos()
    mouseclick = pygame.mouse.get_pressed()
    gameScreen.blit(musicList[musi], (x, y))
    rect = pygame.Rect(x, y, 120, 20)
    if rect.collidepoint(mousepos):
        # print('testYolo')
        gameScreen.blit(musicList[5], (x, y))
        if mouseclick[0] == 1:
            music(musi)
            return musi
    return currentMusic


def device_func(using_t, playing_m, nbr_music):
    x = 50
    y = 50
    mousepos = pygame.mouse.get_pos()
    mouseclick = pygame.mouse.get_pressed()

    gameScreen.blit(player, (x-14, y-13))

    nbr_music = ipodSelect(x, y+20, 0, nbr_music)
    nbr_music = ipodSelect(x, y+50, 1, nbr_music)
    nbr_music = ipodSelect(x, y+80, 2, nbr_music)
    nbr_music = ipodSelect(x, y+110, 3, nbr_music)
    nbr_music = ipodSelect(x, y+140, 4, nbr_music)

    rectNext = pygame.Rect(x+76, y+207, 30, 25)
    rectPrev = pygame.Rect(x+11, y+207, 30, 25)
    rectPlay = pygame.Rect(x+36, y+237, 50, 30)


    if rectPlay.collidepoint(mousepos):
        if mouseclick[0] == 1 and not using_t:
            using_t = True
            if not playing_m:
                pygame.mixer.music.unpause()
                playing_m = True
            else:
                pygame.mixer.music.pause()
                playing_m = False

    if rectNext.collidepoint(mousepos):
        if mouseclick[0] == 1 and not using_t:
            using_t = True
            if nbr_music == 4:
                nbr_music = 0
            else:
                nbr_music += 1
            print (nbr_music)
            music(nbr_music)

    if rectPrev.collidepoint(mousepos):
        if mouseclick[0] == 1 and not using_t:
            using_t = True
            if nbr_music == 0:
                nbr_music = 4
            else:
                nbr_music -= 1
            print (nbr_music)
            music(nbr_music)

    if mouseclick[0] == 0:
        using_t = False

    return using_t, playing_m, nbr_music


def exit_game():
    pygame.quit()
    quit()

def playingm():
    music(0)
    ipodPress = False
    ipodPlay = False
    numberMusic = 0
    x = 10
    vx = 20
    vy = 20
    y = 10
    while True:
        gameScreen.blit(backgrd, (0, 0))
        # glutDisplayFunc(draw)                                  # set draw function callback
        # glutIdleFunc(draw)                                     # draw all the time
        # glutMainLoop()
        if x < 20:
            velx = 10
        if y < 20:
            vely = 8
        if y > 480:
            vely = -10
        if x > 480:
            velx = -8
        x += velx
        y += vely
        if vx < 20:
            velx = 22
        if vy < 20:
            vely = 20
        if vy > 480:
            vely = -22
        if vx > 480:
            velx = -20
        vx += velx
        vy += vely
        gameScreen.blit(anim1, (x, y))
        gameScreen.blit(anim2, (vx, vy))
        ipodPress, ipodPlay, numberMusic = device_func(ipodPress, ipodPlay, numberMusic)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game()


def visualizer():
    while True:
        # gameScreen.blit(menuBackground, (0,0))
        # gameScreen.blit(logoBack, (100,100))
        # Button(1100,900,100,50,btnExit,exitGame)

        button_func(210, 200, 100, 50, btnstart, playingm)

        # customCursor()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game()
                if event.key == pygame.K_q:
                    music(1)
                if event.key == pygame.K_w:
                    music(2)
                if event.key == pygame.K_e:
                    music(3)
                if event.key == pygame.K_r:
                    music(4)
                if event.key == pygame.K_t:
                    music(5)
                if event.key == pygame.K_y:
                    music(6)


# ------------- LAUNCHER
visualizer()

# ------------- ENDING
pygame.quit()
quit()