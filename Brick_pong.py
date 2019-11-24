import pygame
from pygame.locals import QUIT, K_LEFT, K_RIGHT
from os import path
from Clases import *
pygame.init()

HEIGH = 800
WIDTH = 800

#Main window
Screen = pygame.display.set_mode((WIDTH, HEIGH))
pygame.display.set_caption('Brick Pong')
clock = pygame.time.Clock()

#Load the images
bg = pygame.image.load(path.join('Sprites','bg.jpg')) # The background
base = Base('purple_base.png') # The base
ball = Ball('ball1.png')


#Load the music and the efects
music = pygame.mixer.music.load(path.join('Sounds', 'music.mp3'))
pygame.mixer.music.play(-1)
hitSound = pygame.mixer.Sound(path.join('Sounds', 'hit.wav'))
brick_sound = pygame.mixer.Sound(path.join('Sounds', 'bullet.wav'))

#Create the bricks!
bricks = []
for i in range(5):
    bricks.append([])
    for j in range(5):
        bricks[i].append(Brick('red_brick.png'))
        bricks[i][j].x += bricks[i][j].img.get_width() * i + 20 * i
        bricks[i][j].y += bricks[i][j].img.get_height() * j + 20 * j


def redrawGameWindow():
    """ This function draws 
        everything on the screen
    """
    # Draw Backgorund
    Screen.blit(bg, (-400, -100))
    # Draw base
    base.draw(Screen)

    #Draw bricks
    for list_of_bricks in bricks:
        for brick in list_of_bricks:
            brick.draw(Screen)

    #draw balls
    ball.draw(Screen)

    pygame.display.update()

# Start game loop
start= True
while start:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
    keys = pygame.key.get_pressed()
    # Get what user is typing
    if keys[pygame.K_LEFT] and base.x >= 10:
        base.x -= base.speed
        ball.x -= base.speed
    if keys[pygame.K_RIGHT] and base.x <= 730:
        base.x += base.speed
        ball.x += base.speed
    if keys[pygame.K_SPACE] :
        ball.xspeed = 5
        ball.yspeed = -5
        start = 0
    redrawGameWindow()

gaming = True
while gaming:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False

    # Ball movement
    ball.x += ball.xspeed
    ball.y += ball.yspeed

    # Check if the ball collides with the walls
    if ball.x + ball.img.get_width() >= WIDTH or ball.x <= 0 :
        hitSound.play()
        ball.xspeed *= -1
    if ball.y + ball.img.get_height()/2 <= 0:
        hitSound.play()
        ball.yspeed *= -1
    # Check if the ball colliedes with the base
    if ball.y >= 400:
        if ball.y >= base.y - base.img.get_height() and ball.y <= base.y - base.img.get_height()/2 and ball.x >= base.x and ball.x <= base.x + base.img.get_width():
            hitSound.play()
            ball.yspeed *= -1
            porcentaje = (ball.x - base.x) / base.img.get_width()
            if porcentaje >= 50:
                ball.xspeed = 10 * porcentaje
            else:
                ball.xspeed = -10 * porcentaje
        elif ball.y >= base.y and ball.y <= base.y + base.img.get_height() and ball.x >= base.x and ball.x <= base.x + base.img.get_width():
            hitSound.play()
            ball.xspeed *= -1
            ball.yspeed *= -1
    else:
        for brick_list in bricks:
            for brick in brick_list:
                # if the ball hist down
                if ball.y >= brick.y and ball.y <= brick.y + brick.img.get_height() and ball.x >= brick.x and ball.x <= brick.x + brick.img.get_width():
                    brick_sound.play()
                    brick_list.remove(brick)
                    ball.yspeed *= -1
                # If the ball hist the sides
                elif ball.y >= brick.y and ball.y <= brick.y + brick.img.get_height() and ball.x >= brick.x and ball.x <= brick.x + brick.img.get_width():
                    brick_sound.play()
                    brick_list.remove(brick)
                    ball.xspeed *= -1
    #if the ball drops down you lose
    if ball.y >= HEIGH:
        print('Perdiste')
        ball.y -= 20
        ball.yspeed = 0
        ball.xspeed = 0
                
    # Get what user is typing
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and base.x >= 10:
        base.x -= base.speed
    if keys[pygame.K_RIGHT] and base.x <= 730:
        base.x += base.speed

    redrawGameWindow()
pygame.quit()