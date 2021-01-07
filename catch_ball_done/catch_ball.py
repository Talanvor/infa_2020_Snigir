import pygame as pg
from pygame.draw import *
from random import randint
import numpy as np
import numpy.random

# Инициализация pygame
pg.init()

print('Введите ваш ник')
USERNAME = input()
USERNAME = USERNAME.split()[0]

# Константы окна
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Параметры игры
FPS = 30
Score = 0
Flag_Finish = False
TimeLeft = 30 * FPS

# Инициализация игрового окна
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

# Константы цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Константы шаров
balls_amount = 6
balls_max_speed = 2
balls_lifetime = 100
balls_radiusRange = (30, 70)

# Параметры шаров
list_of_balls_coor_x = np.empty((balls_amount))
list_of_balls_coor_y = np.empty((balls_amount))
list_of_balls_radius = np.empty((balls_amount))
list_of_balls_color = np.empty((3*balls_amount)).reshape(balls_amount, 3)
list_of_balls_speed_x = np.empty((balls_amount))
list_of_balls_speed_y = np.empty((balls_amount))
list_of_balls_ingameTime = np.empty((balls_amount))

# Функция создания i-го шарика
def ball_new(i):
    list_of_balls_coor_x[i] = randint(int(SCREEN_WIDTH * 0.2), int(SCREEN_WIDTH * 0.8))
    list_of_balls_coor_y[i] = randint(int(SCREEN_HEIGHT * 0.2), int(SCREEN_HEIGHT * 0.8))
    list_of_balls_speed_x[i] = randint(-balls_max_speed, balls_max_speed)
    list_of_balls_speed_y[i] = randint(-balls_max_speed, balls_max_speed)
    list_of_balls_radius[i] = randint(balls_radiusRange[0], balls_radiusRange[1])
    list_of_balls_color[i] = COLORS[randint(0, 5)]
    list_of_balls_ingameTime[i] = randint(0, balls_lifetime)
	
# Функция игрового шага i-го шарика
def ball_step(i):
	# прорисовка
	circle(screen, list_of_balls_color[i], (list_of_balls_coor_x[i], list_of_balls_coor_y[i]), list_of_balls_radius[i])
	
	# увеличение прожитого времени
	list_of_balls_ingameTime[i] += 1

	# условие смерти
	if list_of_balls_ingameTime[i] >= balls_lifetime:
		ball_new(i)
		
	# движение
	list_of_balls_coor_x[i] += list_of_balls_speed_x[i]
	list_of_balls_coor_y[i] += list_of_balls_speed_y[i]

    # Взаимодействие с краями
	if list_of_balls_coor_x[i] > SCREEN_WIDTH * 0.9:
		list_of_balls_speed_x[i] = -list_of_balls_speed_x[i]
	if list_of_balls_coor_x[i] < SCREEN_WIDTH * 0.1:
		list_of_balls_speed_x[i] = -list_of_balls_speed_x[i]
	if list_of_balls_coor_y[i] > SCREEN_HEIGHT * 0.9:
		list_of_balls_speed_y[i] = -list_of_balls_speed_y[i]
	if list_of_balls_coor_y[i] < SCREEN_HEIGHT * 0.1:
		list_of_balls_speed_y[i] = -list_of_balls_speed_y[i]

# Константы мишеней
marks_amount = 4
marks_max_speed = 9
marks_max_accel = 2
marks_lifetime = 90
marks_radiusRange = (40, 60)

# Параметры мишеней
list_of_marks_coor_x = np.empty((marks_amount))
list_of_marks_coor_y = np.empty((marks_amount))
list_of_marks_radius = np.empty((marks_amount))
list_of_marks_speed_x = np.empty((marks_amount))
list_of_marks_speed_y = np.empty((marks_amount))
list_of_marks_accel_x = np.empty((marks_amount))
list_of_marks_accel_y = np.empty((marks_amount))
list_of_marks_ingameTime = np.empty((marks_amount))

# Функция создания i-ой мишени
def mark_new(i):
	list_of_marks_coor_x[i] = randint(int(SCREEN_WIDTH * 0.2), int(SCREEN_WIDTH * 0.8))
	list_of_marks_coor_y[i] = randint(int(SCREEN_HEIGHT * 0.2), int(SCREEN_HEIGHT * 0.8))
	list_of_marks_speed_x[i] = randint(-marks_max_speed, marks_max_speed)
	list_of_marks_speed_y[i] = randint(-marks_max_speed, marks_max_speed)
	list_of_marks_accel_x[i] = randint(-marks_max_accel, marks_max_accel)
	list_of_marks_accel_y[i] = randint(-marks_max_accel, marks_max_accel)
	list_of_marks_radius[i] = randint(marks_radiusRange[0], marks_radiusRange[1])
	list_of_marks_ingameTime[i] = randint(0, marks_lifetime)
	
# Функция игрового шага i-ой мишени
def mark_step(i):
	# прорисовка
	circle(screen, WHITE, (list_of_marks_coor_x[i], list_of_marks_coor_y[i]), list_of_marks_radius[i])
	circle(screen, RED,   (list_of_marks_coor_x[i], list_of_marks_coor_y[i]), list_of_marks_radius[i]/2)
	circle(screen, WHITE, (list_of_marks_coor_x[i], list_of_marks_coor_y[i]), list_of_marks_radius[i]/3)
	circle(screen, RED,   (list_of_marks_coor_x[i], list_of_marks_coor_y[i]), list_of_marks_radius[i]/10)
	
	# увеличение прожитого времени
	list_of_marks_ingameTime[i] += 1
	list_of_marks_radius[i] -= 1

	# условие смерти
	if list_of_marks_ingameTime[i] >= marks_lifetime:
		mark_new(i)
	if list_of_marks_radius[i] <= 5:
		mark_new(i)
		
	# движение
	list_of_marks_coor_x[i] += list_of_marks_speed_x[i]
	list_of_marks_coor_y[i] += list_of_marks_speed_y[i]
	
	list_of_marks_speed_x[i] += list_of_marks_accel_x[i]
	list_of_marks_speed_y[i] += list_of_marks_accel_y[i]
	
	list_of_marks_accel_x[i] = randint(-marks_max_accel, marks_max_accel)
	list_of_marks_accel_y[i] = randint(-marks_max_accel, marks_max_accel)

    # Взаимодействие с краями
	if list_of_marks_coor_x[i] > SCREEN_WIDTH * 0.9:
		list_of_marks_speed_x[i] = -list_of_marks_speed_x[i]
	if list_of_marks_coor_x[i] < SCREEN_WIDTH * 0.1:
		list_of_marks_speed_x[i] = -list_of_marks_speed_x[i]
	if list_of_marks_coor_y[i] > SCREEN_HEIGHT * 0.9:
		list_of_marks_speed_y[i] = -list_of_marks_speed_y[i]
	if list_of_marks_coor_y[i] < SCREEN_HEIGHT * 0.1:
		list_of_marks_speed_y[i] = -list_of_marks_speed_y[i]

# Заполняем данные шариков
for i in range(balls_amount):
    ball_new(i)
	
# Заполняем данные мишеней
for i in range(marks_amount):
    mark_new(i)

# Функция вывода текста на экран
def text(txt, x, y):
    f1 = pg.font.SysFont('arial', 45)
    text = f1.render(txt, 1, RED)
    screen.blit(text, (x, y))

# Основной цикл pygame
while not Flag_Finish:
	clock.tick(FPS)
	
	TimeLeft -= 1
	
	for event in pg.event.get():
        # Проверка выхода из программы
		if event.type == pg.QUIT:
			Flag_Finish = True

        # Проверка попадания по шарику
		if event.type == pg.MOUSEBUTTONDOWN:
			mouse_x = event.pos[0]
			mouse_y = event.pos[1]
			for i in range(balls_amount):
				if (mouse_x - list_of_balls_coor_x[i]) ** 2 + (mouse_y - list_of_balls_coor_y[i]) ** 2 <= list_of_balls_radius[i] ** 2:
					ball_new(i)
					Score += 1
			for i in range(marks_amount):
				if (mouse_x - list_of_marks_coor_x[i]) ** 2 + (mouse_y - list_of_marks_coor_y[i]) ** 2 <= list_of_marks_radius[i] ** 2:
					mark_new(i)
					Score += 5

    # Движение шариков и мишеней
	for i in range(balls_amount):
		ball_step(i)
	for i in range(marks_amount):
		mark_step(i)

	# Проверка оставшегося времени
	if TimeLeft <= 0:
		Flag_Finish = True
	
	# Вывод текста
	text("Score: " + str(Score), 60, 20)
	text("Time left: " + str(TimeLeft // FPS), SCREEN_WIDTH * 0.9 - 250, 20)
	pg.display.update()
	screen.fill(BLACK)

# таблица лидеров
# Создание файла при необходимости и его считывание
try:
	lb = open("leaderboard.txt", "r")
	lblines = lb.readlines()
	lb.close()
except FileNotFoundError:
	lb = open("leaderboard.txt", "w")
	lb.write("Goodboy 300\n")
	lb.close()
	lb = open("leaderboard.txt", "r")
	lblines = lb.readlines()
	lb.close()

# Поиск игрока и запись его в таблицу
lb = open("leaderboard.txt", "w")
Flag_userFound = False
for lbline in lblines:
	if lbline != "":
		lbline_username = lbline.split()[0]
		lbline_score = lbline.split()[1]
		if lbline_username == USERNAME:
			Flag_userFound = True
			if Score > int(lbline_score):
				lbline = USERNAME + " " + str(Score) + "\n"
		lb.write(lbline)
if Flag_userFound == False:
	lb.write(USERNAME + " " + str(Score) + "\n")
lb.close()

# завершение pygame
print(Score)
pg.quit()