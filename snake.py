from settings import *
import pygame as pg


class SnakePart():
    def __init__(self, game, xs, ys, color):
        self.game = game
        self.xs = xs
        self.ys = ys
        self.color = color
        self.image = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(color)
        self.draw()
        self.move()

    def move(self):
        if self.xs < 0:
            self.xs = DISPLAY_WIDTH
        elif self.xs > DISPLAY_WIDTH:
            self.xs = 0
        if self.ys < 0:
            self.ys = DISPLAY_HEIGHT
        elif self.ys > DISPLAY_HEIGHT:
            self.ys = 0

    def draw(self):
        self.game.screen.blit(self.image, (self.xs, self.ys))


class Snake():
    def __init__(self, game, lead_x, lead_y, color, head):
        self.body = []
        self.snake_length = 10
        self.game = game
        self.direction = 'RIGHT'
        self.color = color
        self.x_change = BLOCK_SIZE
        self.y_change = 0
        self.lead_x = lead_x*BLOCK_SIZE
        self.lead_y = lead_y*BLOCK_SIZE
        self.image = pg.image.load(head)
        self.head = pg.transform.rotate(self.image, 270)

    def key(self, direction):
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
            self.head = pg.transform.rotate(self.image, 90)
            self.x_change = -BLOCK_SIZE
            self.y_change = 0

        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
            self.head = pg.transform.rotate(self.image, 270)
            self.x_change = BLOCK_SIZE
            self.y_change = 0

        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
            self.head = pg.transform.rotate(self.image, 0)
            self.y_change = -BLOCK_SIZE
            self.x_change = 0

        if direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
            self.head = pg.transform.rotate(self.image, 180)
            self.y_change = BLOCK_SIZE
            self.x_change = 0

    def add_part(self, screen, list):
        if self.direction == "right":
            self.head = pg.transform.rotate(self.image, 270)

        elif self.direction == "left":
            self.head = pg.transform.rotate(self.image, 90)

        elif self.direction == "up":
            self.head = self.image

        elif self.direction == "down":
            self.head = pg.transform.rotate(self.image, 180)

        screen.blit(self.head, (list[-1][0], list[-1][1]))
        for XnY in list[:-1]:  # [positionX, positionY, sizeX, sizeY]
            SnakePart(self.game, XnY[0], XnY[1], self.color)

    def draw_body(self, screen):

        if len(self.body) > self.snake_length:
            del self.body[0]

        snakeHead = []
        if self.lead_x < 0:
            self.lead_x = DISPLAY_WIDTH
        elif self.lead_x > DISPLAY_WIDTH-BLOCK_SIZE:
            self.lead_x = 0
        if self.lead_y < 0:
            self.lead_y = DISPLAY_HEIGHT
        elif self.lead_y > DISPLAY_HEIGHT-BLOCK_SIZE:
            self.lead_y = 0
        snakeHead.append(self.lead_x)
        snakeHead.append(self.lead_y)
        self.body.append(snakeHead)
        self.add_part(screen, self.body)
        self.lead_x += self.x_change
        self.lead_y += self.y_change
        self.collide(snakeHead)

    def eat(self):
        self.snake_length += 1

    def collide(self, snakeHead):
        for eachSegment in self.body[:-1]:
            if eachSegment == snakeHead:

                self.game.playing = False



