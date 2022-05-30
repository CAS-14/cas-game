import random
import pygame
 
# Global Variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
 
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, imageDefault, imageMove = None):
        super().__init__()
        self.imageDefault = pygame.image.load(imageDefault)
        self.imageMove = pygame.image.load(imageMove) if imageMove else self.imageDefault

        #print(self.imageDefault + self.imageMove)

        self.image = self.imageDefault
        self.rect = self.image.get_rect()
 
    def move(self, x, y, goofy = False):
        self.image = self.imageMove

        self.rect.x += x if x > 0 and self.rect.right < WIDTH else -1 if goofy else 0
        self.rect.x += x if x < 0 and self.rect.left > 0 else -1 if goofy else 0
        self.rect.y -= y if y > 0 and self.rect.top > 0 else -1 if goofy else 0
        self.rect.y -= y if y < 0 and self.rect.bottom < HEIGHT else -1 if goofy else 0

        self.image = self.imageDefault
 
 
pygame.init()
 
 
RED = (255, 0, 0)
 
 
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
 
 
all_sprites_list = pygame.sprite.Group()
 
jimmy = Sprite("jimmy1.png", "jimmy2.png")
jimmy.rect.x = 300
jimmy.rect.y = 200
 
all_sprites_list.add(jimmy)
 
exit = True
clock = pygame.time.Clock()

doGoofy = True
 
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        #jimmy.moveLeft(10)
        jimmy.move(-10, 0, doGoofy)
    if keys[pygame.K_RIGHT]:
        #jimmy.moveRight(10)
        jimmy.move(10, 0, doGoofy)
    if keys[pygame.K_DOWN]:
        #jimmy.moveDown(10)
        jimmy.move(0, -10, doGoofy)
    if keys[pygame.K_UP]:
        #jimmy.moveUp(10)
        jimmy.move(0, 10, doGoofy)
 
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()