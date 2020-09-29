import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

def draw_background ():
    '''
    Рисует фон
    '''
    rect(screen, (36, 117, 102), (0, 350, 700, 350))
    rect(screen, (246, 161, 75), (0, 280, 500, 70))
    rect(screen, (213, 133, 138), (0, 190, 500, 90))
    rect(screen, (208, 137, 191), (0, 120, 500, 70))
    rect(screen, (169, 118, 219), (0, 80, 500, 40))
    rect(screen, (55, 12, 141), (0, 0, 500, 80))
    
def draw_fish (screen, x, y, w, h):
    '''
    Рисует рыбу
    x, y - координаты рыбы
    w, h - размеры изображения
    '''
    MainColor = (46, 97, 192)
    SecondColor = (236, 83, 83)
    
    BodyRect = (x, y, 2*w//3, h)
    Tail = [[x - w//3, y], [x - w//3, y + h], [x, y + h//2]]
    
    FinU  = [[x + w//3, y + h//4], [x + w//2, y + h//4], [x + w//3, y - h//2]]
    FinDR = [[x + w//2, y + h//2], [x + w//2, y + h], [x + w//2 + w//12, y + h]]
    FinDL = [[x + w//6, y + h//2], [x + w//6, y + h], [x + w//6 - w//12, y + h]]
    
    polygon(screen, SecondColor, FinU)
    polygon(screen, SecondColor, FinDR)
    polygon(screen, SecondColor, FinDL)
    
    ellipse(screen, MainColor, BodyRect)
    polygon(screen, MainColor, Tail)
    
    ellipse(screen, (0, 0, 0), (365, 660, 15, 15))

def draw_bird ():
    '''
    Рисует птичку в небе
    '''
    x = 100
    y = 240
    line(screen, (255, 255, 255), (x, y), (x-50, y-30), 4)
    line(screen, (255, 255, 255), (x, y), (x+50, y-40), 4)
    
    x = 100
    y = 50
    line(screen, (255, 255, 255), (x, y), (x-50, y-30), 4)
    line(screen, (255, 255, 255), (x, y), (x+50, y-40), 4)
    
    x = 300
    y = 140
    line(screen, (255, 255, 255), (x, y), (x-50, y-30), 4)
    line(screen, (255, 255, 255), (x, y), (x+50, y-40), 4)
    
def draw_gull (screen, x, y, w, h):
    '''
    Рисует чайку
    '''
    draw_wings()
    draw_tail()
    
    draw_beak()
    
    draw_claws()
    draw_trotters()

    draw_body(screen, x, y, w, h)

def draw_body(screen, x, y, w, h):
    '''
    Рисует туловище и шею чайки
    '''
    White = (255, 255, 255)
    Black = (0, 0, 0)
    ellipse(screen, White, (x, y, w // 3, h // 5))
    ellipse(screen, White, (x + w // 4, y, w // 6, h // 9))
    ellipse(screen, White, (x + 3*w // 8, y - h // 30, w // 8, h // 12))
    ellipse(screen, Black, (x + 9*w // 20, y - h // 40, 8, 5))

def draw_wings():
    '''
    Рисует крылья чайки
    '''
    polygon(screen, (255, 255, 255), [[245, 510], [235, 430], [185, 410], [120, 360],
                                  [140, 410], [200, 460], [190, 510]])
    polygon(screen, (0, 0, 0), [[245, 510], [235, 430], [185, 410], [120, 360],
                                      [140, 410], [200, 460], [190, 510]], 1)
    polygon(screen, (255, 255, 255), [[225, 510], [215, 450], [125, 440], [90, 420], [135, 475],
                                      [175, 480], [195, 510]])
    polygon(screen, (0, 0, 0), [[225, 510], [215, 450], [125, 440], [90, 420], [135, 475],
                                      [175, 480], [195, 510]], 1)

def draw_tail():
    '''
    Рисует хвост чайки
    '''
    polygon(screen, (255, 255, 255), [[200, 535], [110, 480], [100, 545]])
    polygon(screen, (0, 0, 0), [[200, 535], [110, 480], [100, 545]], 1)

def draw_beak():
    '''
    Рисует клюв чайки
    '''
    polygon(screen, (255, 222, 0), [[380, 496], [415, 490], [425, 500], [380, 500]])
    polygon(screen, (0, 0, 0), [[380, 496], [415, 490], [425, 500], [380, 500]], 1)
    polygon(screen, (255, 222, 0), [[380, 496], [400, 498], [415, 498], [425, 500],
                                    [415, 510], [380, 506]])
    polygon(screen, (0, 0, 0), [[380, 496], [400, 498], [415, 498], [425, 500],
                                    [415, 510], [380, 506]], 1)
    
def draw_trotters():
    '''
    Рисует ноги чайки
    '''
    serf1 = pygame.Surface((500, 700), pygame.SRCALPHA)
    #serf.fill((0, 0, 0))
    pygame.draw.ellipse(serf1, (255, 255, 255), (10, 360, 30, 60))
    serf1 = pygame.transform.rotate(serf1, 30)
    screen.blit(serf1, (0, 0))
    
    serf1 = pygame.Surface((500, 700), pygame.SRCALPHA)
    #serf.fill((0, 0, 0))
    pygame.draw.ellipse(serf1, (255, 255, 255), (30, 370, 30, 50))
    serf1 = pygame.transform.rotate(serf1, 30)
    screen.blit(serf1, (0, 0))
    
    serf1 = pygame.Surface((700, 700), pygame.SRCALPHA)
    #serf.fill((0, 0, 0))
    pygame.draw.ellipse(serf1, (255, 255, 255), (140, 200, 20, 75))
    serf1 = pygame.transform.rotate(serf1, 70)
    screen.blit(serf1, (0, 0))
    
    serf1 = pygame.Surface((700, 700), pygame.SRCALPHA)
    #serf.fill((0, 0, 0))
    pygame.draw.ellipse(serf1, (255, 255, 255), (120, 180, 20, 75))
    serf1 = pygame.transform.rotate(serf1, 70)
    screen.blit(serf1, (0, 0))

def draw_claws():
    '''
    Рисует когти чайки
    '''
    polygon(screen, (255, 222, 0), [[300, 605], [340, 603], [340, 605], [300, 607], [338, 615],
                                [308, 617], [336, 621], [307, 620], [305, 650], [303, 640],
                                [306, 605]])
    polygon(screen, (0, 0, 0), [[300, 605], [340, 603], [340, 605], [300, 607], [338, 615],
                                    [308, 617], [336, 621], [307, 620], [305, 650], [303, 640],
                                [306, 605]], 1)
    
    
    polygon(screen, (255, 222, 0), [[283, 620], [273, 627],[270, 647], [271, 658], [278, 629],
                    [285, 627], [309, 639], [307, 634], [290, 627],
                    [316, 631], [283, 620], [310, 610],[280, 615]])
    polygon(screen, (0, 0, 0), [[283, 620], [273, 627],[270, 647], [271, 658], [278, 629],
                    [285, 627], [309, 639], [307, 634], [290, 627],
                    [316, 631], [283, 620], [310, 610],[280, 615]], 1)

draw_background()   
draw_bird()
draw_fish(screen, 306, 645, 120, 45)
draw_gull(screen, 160, 500, 450, 350)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()