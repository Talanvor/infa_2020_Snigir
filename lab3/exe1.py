import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

cWhite = (255, 255, 255)
cRed = (255, 0, 0)
cGreen = (0, 255, 0)
cBlue = (0, 0, 255)
cBlack = (0, 0, 0)

def wline (xb, yb, xe, ye, color, width):
    line(screen, color, (xb, yb), (xe, ye), width)
def wrect (xLU, yLU, xRD, yRD, color, width):
    rect(screen, color, (xLU, yLU, xRD - xLU, yRD - yLU), width)
def wpolygon (xLU, yLU, xLD, yLD, xRD, yRD, xRU, yRU, color, width):
    polygon(screen, color, [(xLU,yLU), (xLD,yLD), (xRD,yRD), (xRU,yRU)], width)
def wcircle (x, y, R, color, width):
    circle(screen, color, (x, y), R, width)

wrect(0, 0, 400, 400, (100, 100, 100), 0)

wcircle(200, 200, 100, cRed, 0)
wrect(100, 240, 300, 250, cBlack, 0) 

wpolygon(100, 100, 80, 120, 160, 200, 180, 180, cWhite, 0)
wpolygon(300, 100, 320, 120, 240, 200, 220, 180, cWhite, 0)

wcircle(270, 180, 10, cBlack, 0)
wcircle(130, 180, 10, cBlack, 0)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()