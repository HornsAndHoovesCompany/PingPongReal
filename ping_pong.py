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
        if keys_pressed[K_LEFT] and player.rect.x > 5:
            player.rect.x-=self.speed
        if keys_pressed[K_RIGHT] and player.rect.x < 595:
            player.rect.x+=self.speed
        '''if keys_pressed[K_UP] and player.rect.y > 5:
            player.rect.y-=self.speed
        if keys_pressed[K_DOWN] and player.rect.y < 395:
            player.rect.y+=self.speed'''
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
player = Player('kolobok.png', 300, 400, 170, 100, 12)
rocket1 = Player('ракетка.png', 25, 250, 170, 100, 12)
rocket2 = Player('ракетка.png', 500, 250, 170, 100, 12)
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
    player.reset()
    player.update()
    rocket1.reset()
    rocket1.update()
    rocket2.reset()
    rocket2.update()
    display.update()
    
    clock.tick(FPS)
