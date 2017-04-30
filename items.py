from settings import *
import pygame as pg
import random as rd


class Fruit(pg.sprite.Sprite):
    def __init__(self, game, x, y, png):
        self.game = game
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.png = png
        self.x = round(x)
        self.y = round(y)
        self.image = pg.image.load(png)
        self.rect = self.image.get_rect()

    def collide(self, snaake):
        print(snaake.lead_x, " ", snaake.lead_y, end=" ")
        print(self.x, " ", self.y)
        if (snaake.lead_x, snaake.lead_y) == (self.x, self.y):
            snaake.eat()
            self.random()

    def random(self):
        self.groups.remove(self)
        x = round(rd.randrange(0, DISPLAY_WIDTH-BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE
        y = round(rd.randrange(0, DISPLAY_HEIGHT-BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE
        Fruit(self.game, x, y, self.png)
        # print(x, y)

    # def draw(self, screen):
    #     #print(self.x," ",self.y)
    #     self.random()
    #     screen.blit(self.image, (self.x, self.y))





    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.collide(self.game.snake2)
        self.collide(self.game.snake)
