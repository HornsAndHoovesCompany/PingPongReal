from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = None
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

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
