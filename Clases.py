import pygame
from os import path

class Base(object):
    def __init__(self, image_name):
        self.img = pygame.image.load(path.join('Sprites', image_name))
        self.x = 400
        self.y = 760
        self.speed = 10
        self.hitbox = (self.x +40, self.y + 5, 100, 10)
        self.drawhitbox = False
    
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        #Draw the hitbox
        if self.drawhitbox:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.img.get_width(), self.img.get_height()), True)

class Ball(object):
    def __init__(self, image_name):
        self.img = pygame.image.load(path.join('Sprites', image_name))
        self.x = 450
        self.y = 745
        self.xspeed = 0
        self.yspeed = 0
        self.drawhitbox = False

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        if self.drawhitbox:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.img.get_width(), self.img.get_height()), True)

class Brick(object):
    def __init__(self, image_name):
        self.img = pygame.image.load(path.join('Sprites', image_name)) 
        self.x = 200
        self.y = 100
        self.drawhitbox = False
    
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        if self.drawhitbox:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.img.get_width(), self.img.get_height()), True)

if __name__ == '__main__':
    Screen = pygame.display.set_mode((800, 800))
    Base1 = Base('purple_base.png')
    Base1.drawhitbox = True
    Ball1 = Ball('ball1.png')
    Ball1.y -= 50
    Ball1.drawhitbox = True
    Brick1 = Brick('red_brick.png')
    Brick1.drawhitbox = True
    while True:
        Base1.draw(Screen)
        Ball1.draw(Screen)
        Brick1.draw(Screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False

        pygame.display.update()