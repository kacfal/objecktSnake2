from items import Fruit
from settings import *
import pygame as pg
from snake import Snake, SnakePart


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.small_font = pg.font.SysFont("comicsansms", 25)
        self.med_font = pg.font.SysFont("comicsansms", 50)
        self.large_font = pg.font.SysFont("comicsansms", 80)

    def score(self, snakaae, hight):
        text = self.small_font.render("Score: " + str(snakaae.snake_length), True, BLACK)
        self.screen.blit(text, [hight, 0])

    def new(self, png):
        """Initialize all variables and do all setup for a new game"""
        self.all_sprites = pg.sprite.Group()
        self.fruit = Fruit(self, 120, 0, png)
        self.fruit2 = Fruit(self, 40, 40, png)
        self.fruit3 = Fruit(self, 40, 120, png)
        self.snake = Snake(self, 10, 10, GREEN)
        self.snake2 = Snake(self, 4, 4, RED)

    @staticmethod
    def quit():
        pg.quit()
        quit()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            # self.events1()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def pause(self):

        paused = True

        self.message_to_screen("Paused", BLACK, -100, size="large")
        self.message_to_screen("Press C to continue or Q to quit", BLACK, 25)

        pg.display.update()

        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        paused = False
                    elif event.key == pg.K_q:
                        self.quit()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.snake.key('LEFT')
                if event.key == pg.K_RIGHT:
                    self.snake.key('RIGHT')
                if event.key == pg.K_UP:
                    self.snake.key('UP')
                if event.key == pg.K_DOWN:
                    self.snake.key('DOWN')
                if event.key == pg.K_p:
                    self.pause()
                if event.key == pg.K_q:
                    self.quit()
                if event.key == pg.K_a:
                    print('a')
                    self.snake2.key('LEFT')
                if event.key == pg.K_d:
                    self.snake2.key('RIGHT')
                if event.key == pg.K_w:
                    self.snake2.key('UP')
                if event.key == pg.K_s:
                    self.snake2.key('DOWN')

    # def events1(self):
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             self.quit()
    #         if event.type == pg.KEYDOWN:
    #             if event.key == pg.K_a:
    #                 print('a')
    #                 self.snake2.key('LEFT')
    #             if event.key == pg.K_d:
    #                 self.snake2.key('RIGHT')
    #             if event.key == pg.K_w:
    #                 self.snake2.key('UP')
    #             if event.key == pg.K_s:
    #                 self.snake2.key('DOWN')

    def draw(self):
        self.screen.fill(WHITE)
        self.snake.draw_body(self.screen)
        self.snake2.draw_body(self.screen)
        self.all_sprites.draw(self.screen)
        self.score(self.snake2, DISPLAY_HEIGHT)
        self.score(self.snake, 0)
        pg.time.delay(150)
        pg.display.update()

    def text_objects(self, text, color, size):
        if size == "small":
            text_surface = self.small_font.render(text, True, color)
        elif size == "medium":
            text_surface = self.med_font.render(text, True, color)
        elif size == "large":
            text_surface = self.large_font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_to_screen(self, msg, color, y_displace=0, x_displace=0, size="small"):
        text_surf, text_rect = self.text_objects(msg, color, size)
        text_rect.center = (DISPLAY_WIDTH / 2) + x_displace, (DISPLAY_HEIGHT / 2) + y_displace
        self.screen.blit(text_surf, text_rect)

    def show_star_screen(self):
        intro = True

        while intro:
            self.screen.fill(WHITE)
            self.message_to_screen("Welcome to Snake", GREEN, -100, size="large")
            self.message_to_screen("Press C to play, ESC to pause or Q to quit", BLACK, 180, size='small')
            self.message_to_screen("The objective of the game is to eat red apples", BLACK, -30, size='small')
            self.message_to_screen("The more apples you eat, the longer you get", BLACK, 10)
            self.message_to_screen("if you run into yourself, or the edges, you die!", BLACK, 50)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.quit()
                if event.key == pg.K_c:
                    self.run()



g = Game()
g.new("apple.png")
g.show_star_screen()
while True:
    g.new("apple.png")
    g.run()