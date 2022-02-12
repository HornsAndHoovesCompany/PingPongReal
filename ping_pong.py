from pygame import *
from random import randint
#100500 strings of code later...
clock = time.Clock()
FPS = 60
back = (50, 140, 42)
window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
game = True
finish = False
while game:
    for e in event.get():
        if e.type==QUIT:
            game = False
    window.fill((50, 140, 42))
    display.update()
    clock.tick(FPS)