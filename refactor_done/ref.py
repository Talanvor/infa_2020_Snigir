import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
window_width = 500
window_height = 700
screen = pygame.display.set_mode((window_width, window_height))

'''
Описание rect
rect(x, y, w, h)
x, y - координаты левой верхней вершины
w, h - ширина и высота прямоугольника
'''

def draw_background (screen):
	'''
	Рисует фон
	'''
	blue = (55, 12, 141)
	siren = (169, 118, 219)
	ros = (208, 137, 191)
	persik = (213, 133, 138)
	mightOrange = (246, 161, 75)
	greensea = (36, 117, 102)
	
	w = window_width
	h = window_height
	
	rect(screen, blue,        (0, 0,       w, h))
	rect(screen, siren,       (0, 1*h//10, w, h))
	rect(screen, ros,         (0, 2*h//10, w, h))
	rect(screen, persik,      (0, 3*h//10, w, h))
	rect(screen, mightOrange, (0, 4*h//10, w, h))
	rect(screen, greensea,    (0, 5*h//10, w, h))



def draw_fish (screen, x, y, w, h):
	'''
	Рисует рыбу внутри rect(x, y, w, h)
	'''
	
	MainColor = (46, 97, 192)
	SecondColor = (236, 83, 83)

	draw_fish_fins(screen, SecondColor, x, y, w, h)
	draw_fish_tail(screen, MainColor,   x, y, w, h)
	draw_fish_body(screen, MainColor,   x, y, w, h)
	draw_fish_eye (screen, x, y, w, h)

def draw_fish_fins(screen, color, x, y, w, h):
	'''
	Рисует плавники рыбы внутри rect(x, y, w, h)
	'''
	FinU  = [[x + 5*w//9, y         ], [x + 7*w//9, y + 3*h//6], [x + 5*w//9, y + 3*h//6]]
	FinDR = [[x + 6*w//9, y + 3*h//6], [x + 8*w//9, y + 6*h//6], [x + 6*w//9, y + 6*h//6]]
	FinDL = [[x + 3*w//9, y + 6*h//6], [x + 5*w//9, y + 3*h//6], [x + 5*w//9, y + 6*h//6]]

	polygon(screen, color, FinU)
	polygon(screen, color, FinDR)
	polygon(screen, color, FinDL)
	
def draw_fish_tail(screen, color, x, y, w, h):
	'''
	Рисует хвост рыбы внутри rect(x, y, w, h)
	'''
	Tail = [[x         , y + 1*h//6], [x + 3*w//9, y + 3*h//6], [x         , y + 5*h//6]]
	polygon(screen, color, Tail)
	
def draw_fish_body(screen, color, x, y, w, h):
	'''
	Рисует туловище выбы внутри rect(x, y, w, h)
	'''
	BodyRect = (x + 3*w//9, y + 1*h//6, 6*w//9, 4*h//6)
	ellipse(screen, color, BodyRect)
	
def draw_fish_eye(screen, x, y, w, h):
	'''
	Рисует глаз рыбы внутри rect(x, y, w, h)
	'''
	black = (0, 0, 0)
	EyeRect = (x + 7*w//9, y + 2*h//6, 1*w//9, 1*h//6)
	ellipse(screen, black, EyeRect)



def draw_bird (screen, x, y, w, h, d = 4):
	'''
	Рисует птичку  внутри rect(x, y, w, h) с толщиной линии d
	'''
	white = (255, 255, 255)

	line(screen, white, (x, y), (x + w//2, y + h//2), d)
	line(screen, white, (x + w//2, y + h//2), (x + w, y), d)




def draw_gull (screen, x, y, w, h):
    '''
    Рисует чайку внутри rect(x, y, w, h)
    '''
    white = (255, 255, 255)
    yellow = (255, 255, 0)
	
    draw_wings(screen, white, x, y, w, h)
    draw_tail(screen, white, x, y, w, h)

    draw_beak(screen, yellow, x, y, w, h)

    draw_claws(screen, yellow, x, y, w, h)
    draw_trotters(screen, white, x, y, w, h)

    draw_body(screen, white, x, y, w, h)

def draw_body(screen, color, x, y, w, h):
	'''
	Рисует туловище, шею и глаз чайки внутри rect(x, y, w, h)
	'''
	black = (0, 0, 0)
	
	ellipse(screen, color, (x + 5*w//25,  y + 7*h//19, 10*w//25, 6*h//19))
	ellipse(screen, color, (x + 13*w//25, y + 7*h//19, 6*w//25,  4*h//19))
	ellipse(screen, color, (x + 17*w//25, y + 6*h//19, 5*w//25,  3*h//19))
	ellipse(screen, black, (x + 20*w//25, y + 7*h//19, 1*w//25,  1*h//19))

def draw_wings(screen, color, x, y, w, h):
	'''
	Рисует крылья чайки внутри rect(x, y, w, h)
	'''
	black = (0, 0, 0)
	
	polygon(screen, color, [[x + 11*w//25, y + 10*h//19], [x + 10*w//25, y + 3*h//19], [x + 7*w//25, y + 2*h//19], [x + 3*w//25, y + 0*h//19], [x + 4*w//25, y + 3*h//19], [x + 7*w//25, y + 5*h//19], [x + 8*w//25, y + 10*h//19]])
	polygon(screen, black, [[x + 11*w//25, y + 10*h//19], [x + 10*w//25, y + 3*h//19], [x + 7*w//25, y + 2*h//19], [x + 3*w//25, y + 0*h//19], [x + 4*w//25, y + 3*h//19], [x + 7*w//25, y + 5*h//19], [x + 8*w//25, y + 10*h//19]], 1)
	
	polygon(screen, color, [[x + 10*w//25, y + 10*h//19], [x + 9*w//25, y + 4*h//19], [x + 2*w//25, y + 5*h//19], [x + 0*w//25, y + 3*h//19], [x + 2*w//25, y + 7*h//19], [x + 5*w//25, y + 7*h//19], [x + 7*w//25, y + 10*h//19]])
	polygon(screen, black, [[x + 10*w//25, y + 10*h//19], [x + 9*w//25, y + 4*h//19], [x + 2*w//25, y + 5*h//19], [x + 0*w//25, y + 3*h//19], [x + 2*w//25, y + 7*h//19], [x + 5*w//25, y + 7*h//19], [x + 7*w//25, y + 10*h//19]], 1)
	
def draw_tail(screen, color, x, y, w, h):
	'''
	Рисует хвост чайки внутри rect(x, y, w, h)
	'''

	polygon(screen, color, [[x + 7*w//25, y + 9*h//19], [x + 1*w//25, y + 8*h//19], [x + 0*w//25, y + 13*h//19], [x + 7*w//25, y + 11*h//19]])
	polygon(screen, color, [[x + 7*w//25, y + 9*h//19], [x + 1*w//25, y + 8*h//19], [x + 0*w//25, y + 13*h//19], [x + 7*w//25, y + 11*h//19]], 1)

def draw_beak(screen, color, x, y, w, h):
	'''
	Рисует клюв чайки внутри rect(x, y, w, h)
	'''
	black = (0, 0, 0)
	
	polygon(screen, color, [[x + 21*w//25, y + 8*h//19], [x + 24*w//25, y + 7*h//19], [x + 25*w//25, y + 8*h//19]])
	polygon(screen, black, [[x + 21*w//25, y + 8*h//19], [x + 24*w//25, y + 7*h//19], [x + 25*w//25, y + 8*h//19]], 1)
	
	polygon(screen, color, [[x + 20*w//25, y + 8*h//19], [x + 24*w//25, y + 9*h//19], [x + 25*w//25, y + 8*h//19]])
	polygon(screen, black, [[x + 20*w//25, y + 8*h//19], [x + 24*w//25, y + 9*h//19], [x + 25*w//25, y + 8*h//19]], 1)

def draw_trotters(screen, color, x, y, w, h):
	'''
	Рисует ноги чайки внутри rect(x, y, w, h)
	'''
	ellipse(screen, color, (x + 8*w//25,  y + 12*h//19, 3*w//25, 3*h//19))
	ellipse(screen, color, (x + 9*w//25,  y + 14*h//19, 2*w//25, 4*h//19))
	ellipse(screen, color, (x + 10*w//25, y + 17*h//19, 5*w//25, 1*h//19))
	
	ellipse(screen, color, (x + 10*w//25, y + 11*h//19, 3*w//25, 3*h//19))
	ellipse(screen, color, (x + 11*w//25, y + 13*h//19, 2*w//25, 4*h//19))
	ellipse(screen, color, (x + 12*w//25, y + 16*h//19, 5*w//25, 1*h//19))
	
	
    

def draw_claws(screen, color, x, y, w, h):
	'''
	Рисует когти чайки внутри rect(x, y, w, h)
	'''
	black = (0, 0, 0)
	
	polygon(screen, color, [[x + 14*w//25, y + 18*h//19], [x + 15*w//25, y + 17*h//19], [x + 15*w//25, y + 19*h//19]])
	polygon(screen, black, [[x + 14*w//25, y + 18*h//19], [x + 15*w//25, y + 17*h//19], [x + 15*w//25, y + 19*h//19]], 1)
	
	polygon(screen, color, [[x + 14*w//25, y + 18*h//19], [x + 15*w//25, y + 17*h//19], [x + 16*w//25, y + 19*h//19]])
	polygon(screen, black, [[x + 14*w//25, y + 18*h//19], [x + 15*w//25, y + 17*h//19], [x + 16*w//25, y + 19*h//19]], 1)
	
	polygon(screen, color, [[x + 14*w//25, y + 18*h//19], [x + 15*w//25, y + 17*h//19], [x + 16*w//25, y + 18*h//19]])
	polygon(screen, black, [[x + 14*w//25, y + 18*h//19], [x + 15*w//25, y + 17*h//19], [x + 16*w//25, y + 18*h//19]], 1)
	
	
	polygon(screen, color, [[x + 16*w//25, y + 17*h//19], [x + 17*w//25, y + 16*h//19], [x + 17*w//25, y + 18*h//19]])
	polygon(screen, black, [[x + 16*w//25, y + 17*h//19], [x + 17*w//25, y + 16*h//19], [x + 17*w//25, y + 18*h//19]], 1)
	
	polygon(screen, color, [[x + 16*w//25, y + 17*h//19], [x + 17*w//25, y + 16*h//19], [x + 18*w//25, y + 18*h//19]])
	polygon(screen, black, [[x + 16*w//25, y + 17*h//19], [x + 17*w//25, y + 16*h//19], [x + 18*w//25, y + 18*h//19]], 1)
	
	polygon(screen, color, [[x + 16*w//25, y + 17*h//19], [x + 17*w//25, y + 16*h//19], [x + 18*w//25, y + 17*h//19]])
	polygon(screen, black, [[x + 16*w//25, y + 17*h//19], [x + 17*w//25, y + 16*h//19], [x + 18*w//25, y + 17*h//19]], 1)



draw_background(screen)   

draw_bird(screen, 100, 240, 70, 50)
draw_bird(screen, 100, 50,  70, 50)
draw_bird(screen, 300, 140, 70, 50)

i = 0
while i < 10:
	draw_bird(screen, randint(50, window_width - 50), randint(50, window_height // 2 - 50), 40, 25, 1)
	i += 1

draw_fish(screen, 300, 600, 120, 45)
draw_fish(screen, 200, 500, -120, 45)
draw_fish(screen, 350, 400, 120, 45)

draw_gull(screen, 100, 400, 300, 200)
draw_gull(screen, 400, 300, -100, 75)
draw_gull(screen, 500, 500, -150, 100)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit() 