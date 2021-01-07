from random import randrange as rnd, choice
import tkinter as tk
import math
import time
'''
перемещаться - W/S (нужна включенная ангилйская раскладка
стрелять - ЛКМ/ПКМ
'''

# Константы окна
screen_width = 800
screen_height = 600


# параметры игры
Score = 0

# константы снарядов
ball_lifetime = 60
ball_radius = 10
ball_x = 40
ball_y = 450

bomb_radius = 50
bomb_lifetime = 200

# константы пушки
gun_x = 20
gun_y = 450

# инициализация игры
root = tk.Tk()
fr = tk.Frame(root)
root.geometry(str(screen_width) + 'x' + str(screen_height))
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

# снаряд
class ball():
    def __init__(self, x = ball_x, y = ball_y):
        """
        Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        r - радиус шарика
        vx - скорость шарика по оси x
        xy - скорость шарика по оси y
        color - цвет шарика
        id - полотно на котором размещается шарик
        live - время жизни шарика
        """
        self.x = x
        self.y = y
        self.r = ball_radius
		
        self.vx = 0
        self.vy = 0
		
        self.color = choice(['blue', 'green', 'red', 'brown'])
		
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill = self.color
        )
        self.lifetime = ball_lifetime

    def set_coords(self):
        """Метод устанавливает координаты холста с мячом"""
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        """
        Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.lifetime < 0:
            balls.pop(balls.index(self))
            canv.delete(self.id)
        else:
            if self.y > screen_height or self.y < 0:
                self.vy = -self.vy
            if self.x > screen_width or self.x < 0:
                self.vx = -self.vx
            self.vy += 1
            self.lifetime -= 1
            self.x += self.vx
            self.y += self.vy
            self.set_coords()

    def hittest(self, ob):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (ob.x - self.x) ** 2 + (ob.y - self.y) ** 2 <= (self.r + ob.r) ** 2:
            return True
        else:
            return False

#снаряд тип 2
class ball_antigravity (ball):
	def move(self):
		#
		#Переместить мяч по прошествии единицы времени.
		#Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
		#self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
		#и стен по краям окна (размер окна 800х600).
		#"""
		if self.lifetime < 0:
			balls.pop(balls.index(self))
			canv.delete(self.id)
		else:
			if self.y > screen_height or self.y < 0:
				self.vy = -self.vy
			if self.x > screen_width or self.x < 0:
				self.vx = -self.vx
			self.lifetime -= 1
			self.x += self.vx
			self.y += self.vy
			self.set_coords()

# вражеский снаряд
class bomb (ball):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = ball_radius
		
        self.vx = -10
        self.vy = 0
		
        self.color = 'black'
		
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill = self.color
        )
        self.lifetime = 200
		
    def move(self, obj):
        if self.lifetime < 0:
            bombs.pop(bombs.index(self))
            canv.delete(self.id)
        else:
            self.lifetime -= 1
            self.x += self.vx
            self.y += self.vy
            self.set_coords()

# пушка
class gun():
	def __init__(self):
        #
        #f2_power - сила, с которой стреляет пушка
        #f2_on - 1 если пушка готова стрелять, 0 - если нет
        #an - угол пушки
        #id - полтно с пушкой
        #
		self.f2_power = 10
		self.f2_on = 0
		self.an = 1
		self.x = 20
		self.y = 450
		self.r = 10
		self.access_to_fire = True
		self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)

	def fire2_start(self, event):
        #Меняет переменную, обозначающую заряженность пушки, на 1"""
		if self.access_to_fire:
			self.f2_on = 1

	def fire2_end_L(self, event):
        #
        #Выстрел мячом.
        #Происходит при отпускании кнопки мыши.
        #Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        #:param event:
        #y - координата курсора по оси y
        #x - координата кусора по оси x
        #bullets - количесто затраченных пуль
        #:return: none
        #"""
		if self.access_to_fire:
			global balls, bullet
			bullet += 1
			new_ball = ball(self.x, self.y)
			self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
			new_ball.vx = self.f2_power * math.cos(self.an)
			new_ball.vy = self.f2_power * math.sin(self.an)
			balls += [new_ball]
			self.f2_on = 0
			self.f2_power = 10
		
	def fire2_end_R(self, event):
        #
        #Выстрел мячом.
        #Происходит при отпускании кнопки мыши.
        #Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        #:param event:
        #y - координата курсора по оси y
        #x - координата кусора по оси x
        #bullets - количесто затраченных пуль
        #:return: none
        #"""
		if self.access_to_fire:
			global balls, bullet
			bullet += 1
			new_ball = ball_antigravity(self.x, self.y)
			self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
			new_ball.vx = self.f2_power * math.cos(self.an)
			new_ball.vy = self.f2_power * math.sin(self.an)
			balls += [new_ball]
			self.f2_on = 0
			self.f2_power = 10

	def targetting(self, event=0):
        #"""Меняет направление пушки"""

		if event:
			self.an = math.atan((event.y - self.y) / (event.x - self.x))
		canv.coords(self.id, self.x, self.y,
					self.x + max(self.f2_power, 20) * math.cos(self.an),
					self.y + max(self.f2_power, 20) * math.sin(self.an)
					)
		if t1.live == 1:
			t1.move()
		if t2.live == 1:
			t2.move()

	def power_up(self):
        #"""увеличивает силу выстрела пушки и закрашивает ее"""
		if self.f2_on:
			if self.f2_power < 40:
				self.f2_power += 0.4
			canv.itemconfig(self.id, fill='orange')
		else:
			canv.itemconfig(self.id, fill='black')
			
	def motion(self, event):
		if (event.char == 'w' or event.char == 'W') and self.y > 50:
			self.y -= 10
		if (event.char == 's' or event.char == 'S') and self.y < 550:
			self.y += 10
			
	def reset(self):
		self.access_to_fire = True
    
	

# мишень
class target():
    def __init__(self):
        """
        points - количсество уничтоженных шариков
        id - полотно с целью
        id_points - полотно со счетом
        live - 1 если цель жива 0 - если нет
        """
        self.points = rnd(5, 10)
        self.id = canv.create_oval(0, 0, 0, 0)
        #self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.live = 1

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(500, 700)
        y = self.y = rnd(300, 500)
        r = self.r = rnd(2, 50)
        vx = self.vx = rnd(-10, 10)
        vy = self.vy = rnd(-10, 10)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        global Score
        Score += self.points
        #canv.itemconfig(self.id_points, text=self.points)

    def move(self):
        if self.x >= 700:
            self.vx = -self.vx
        if self.x <= 100:
            self.vx = -self.vx
        if self.y >= 500:
            self.vy = -self.vy
        if self.y <= 100:
            self.vy = -self.vy

        self.x += self.vx
        self.y += self.vy
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)
		
    def fire(self):
        global bombs
        new_bomb = bomb(self.x, self.y)
        bombs += [new_bomb]


class targethard (target):
    def move(self):
        if self.x >= 700:
            self.vx = -self.vx
        if self.x <= 100:
            self.vx = -self.vx
        if self.y >= 500:
            self.vy = -self.vy
        if self.y <= 100:
            self.vy = -self.vy

        self.x += self.vx
        self.y += self.vy
		
        if self.x < 650 and self.x > 150 and self.y < 450 and self.y > 150 and rnd(0, 100) > 90:
            self.vx = rnd(-10, 10)
            self.vy = rnd(-10, 10)
		
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

t1 = target()
t2 = targethard()

screen1 = canv.create_text(400, 300, text='', font='28')  # создает полотно с количеством потраченных снарядов
deadscreen = canv.create_text(400, 400, text='', font='28')  # создает полотно с уведомлением о смерти
idscore = canv.create_text(30, 30, text = str(Score), font='28') # создает полотно со счетом

g1 = gun()
bullet = 0
balls = []
bombs = []


def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet, Score
    flag_continue = True
	
    t1.new_target()
    t2.new_target()
    g1.reset()
	
    bullet = 0

    canv.bind('<Button-1>', g1.fire2_start)  # Нажатие ПКМ или ЛКМ вызывает функцию g1.fire2_start
    canv.bind('<Button-3>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end_L)  # Отпускание ЛКМ
    canv.bind('<ButtonRelease-3>', g1.fire2_end_R)  # Отпускание ПКМ
    canv.bind('<Motion>', g1.targetting)  # Движение курсора
	
    canv.focus_set()
    canv.bind('<Key>', g1.motion)  # Движение пушки

    t1.live = 1
    t2.live = 1

    while (t1.live or t2.live or balls or bombs):				
        for b in balls:
            b.move()
            
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if t2.live == 0 and t1.live == 0:
                g1.access_to_fire = False
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        if t1.live == 1:
            t1.move()
            if rnd(0, 1000) < 10:
                t1.fire()
        if t2.live == 1:
            t2.move()
            if rnd(0, 1000) < 10:
                t2.fire()
        g1.targetting()
        canv.update()
        time.sleep(0.03)
        g1.power_up()
        canv.itemconfig(idscore, text = Score)
        for b in bombs:
            b.move(g1)
            if b.hittest(g1):
                g1.access_to_fire = False
                canv.itemconfig(deadscreen, text = 'Вы умерли')
                t1.live = 0
                t2.live = 0
                t1.hit()
                t2.hit()
                Score = 0

    for b in bombs:
        canv.delete(b.id)
        bombs.pop(bombs.index(b))

    for b in balls:
        canv.delete(b.id)
        balls.pop(balls.index(b))
		
    canv.itemconfig(screen1, text='')
    canv.itemconfig(deadscreen, text = '')
    root.after(750, new_game)

new_game()
root.mainloop()