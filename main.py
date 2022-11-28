import pygame
import time

from pygame.locals import *

class Snake:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x,self.y = 100,100
        self.direction='down'

    def draw(self):
        self.parent_screen.fill((100,100,5))
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()
    
    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'
 
    def walk(self):
        if self.direction == 'up':
            self.y -=10
        if self.direction =='down':
            self.y +=10
        if self.direction == 'right':
            self.x +=10
        if self.direction == 'left':
            self.x -=10
        self.draw()

        

class Game:
    def __init__(self):
        pygame.init()
        # initialize the screen
        self.surface = pygame.display.set_mode((500,500))
        self.surface.fill((100,100,5))
        self.snake = Snake(self.surface)
        self.snake.draw()
    def run(self):
        running= True
        while running:
            for event in pygame.event.get():
                if event.type== KEYDOWN:
                    if event.key == K_ESCAPE:
                        running=False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()  
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
            self.snake.walk()
            time.sleep(0.2)


    




if __name__=='__main__':
    # intialize pygame
    game = Game()
    game.run()

    
    
    
    
    
