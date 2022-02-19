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

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 370:
            self.rect.y+=self.speed
    def update_new(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y < 370:
            self.rect.y+=self.speed
speed_x = 3
speed_y = 5

ball = Player('kolobok.png', 300, 250, 130, 80, 12)
rocket1 = Player('ракетка.png', 15, 190, 140, 140, 12)
rocket2 = Player('ракетка.png', 500, 190, 140, 140, 12)
clock = time.Clock()
FPS = 60
back = (50, 140, 42)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
game = True
finish = False
while game:
    for e in event.get():
        if e.type==QUIT:
            game = False
    if finish!=True:
        window.fill((50, 140, 42))
        ball.reset()
        rocket1.reset()
        rocket1.update_new()
        rocket2.reset()
        rocket2.update()

        ball.rect.y+=speed_y
        ball.rect.x+=speed_x

        if ball.rect.y > win_height-130 or ball.rect.y==0:
            speed_y*=-1
            
        display.update()
        
    clock.tick(FPS)
