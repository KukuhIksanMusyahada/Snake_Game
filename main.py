import pygame
import time
import random

from pygame.locals import *

SIZE = 40
class Snake:
    def __init__(self,parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x,self.y = [SIZE]*length,[SIZE]*length
        self.direction='down'

    def draw(self):
        self.parent_screen.fill((100,100,5))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
    
    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def increase_length(self):
        self.length +=1
        self.x.append(-1)
        self.y.append(-1)
 
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction =='down':
            self.y[0] += SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        self.draw()

class Food:
    def __init__(self,parent_screen):
        self.food = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x,self.y = SIZE *3,SIZE *3

    def draw(self):
        self.parent_screen.blit(self.food,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24) * SIZE
        self.y = random.randint(1,19) * SIZE

class Game:
    def __init__(self):
        pygame.init()
        # initialize the screen
        self.surface = pygame.display.set_mode((1000,800))
        self.surface.fill((100,100,5))
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.food = Food(self.surface)
        self.food.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
            return False

    def play(self):
        self.snake.walk()
        self.food.draw()
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.food.x,self.food.y):
            self.snake.increase_length()
            self.food.move()

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f'The score is {self.snake.length}',True, (225,225,225))
        self.surface.blit(score,(800,10))
            

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
            self.play()
            time.sleep(0.2)


    




if __name__=='__main__':
    # intialize pygame
    game = Game()
    game.run()

    
    
    
    
    

