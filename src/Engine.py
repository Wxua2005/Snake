import pygame
from random import randint

class Gamestate:
    def __init__(self,screen):
        self.screen = screen
        self.length = 3
        self.size = 10 , 10
        self.factor_x = 1
        self.factor_y = 1
        self.bodyposition_x = 250
        self.bodyposition_y = 250
        self.stopper = None
        self.orientation = False              # 0 for horizontal and 1 for vertical
        self.speed = 1
        self.eaten_food = True
        self.food_pos_x = None
        self.food_pos_y = None 
        self.score = 0

    def food(self) -> None:
        
        '''
        Creates food particles at random places 
        on the screen within the range of width
        and height (400,400)

        if food is eaten then
        it chooses a new random (x,y)
        and blits the new food particle
        '''
        if self.eaten_food:
            self.food_pos_x = randint(0,400)
            self.food_pos_y = randint(0,400)
            self.eaten_food = False
        food = pygame.Rect(self.food_pos_x,self.food_pos_y,self.size[0],self.size[1])
        pygame.draw.rect(self.screen,'Blue',food)

    
    def body(self) -> object:

        '''
        Creates the snake body depending
        on bodyposition_x and bodyposition_y
        and scales according to factor
        '''

        body = pygame.Rect(self.bodyposition_x, self.bodyposition_y, self.size[0] * self.factor_x, self.size[1] * self.factor_y)
        return pygame.draw.rect(self.screen,'Green',body)
    
    def growth(self) -> None:
        '''
        Grows the snake by one square
        depending on the orientation
        '''
        if self.orientation:
            self.factor_y += 1
        elif not self.orientation:
            self.factor_x += 1  
        return None
    
    def moveleft(self) -> int:
        '''
        Decrements x position , i.e moving towards the left
        '''
        self.bodyposition_x = self.bodyposition_x - self.speed
        return self.bodyposition_x
    
    def moveright(self) -> int:
        '''
        Increments x position , i.e moving towards the right
        '''
        self.bodyposition_x = self.bodyposition_x + self.speed
        return self.bodyposition_x
    
    def moveup(self) -> int:
        '''
        Decrements y position , i.e moving upwards
        '''
        self.bodyposition_y = self.bodyposition_y - self.speed
        return self.bodyposition_y
    
    def movedown(self) -> int:
        '''
        Increments x position , i.e moving downwards
        '''
        self.bodyposition_y = self.bodyposition_y + self.speed
        return self.bodyposition_y
    
    def swapvertical(self) -> bool:
        '''
        Swaps the horizontal position of the snake to vertical
        '''
        self.factor_y = self.factor_x
        self.factor_x = 1
        self.orientation = not self.orientation
        return self.orientation
    
    def swaphorizontal(self) -> bool:
        '''
        Swaps the horizontal position of the snake to vertical
        '''
        self.factor_x = self.factor_y
        self.factor_y = 1
        self.orientation = not self.orientation
        return self.orientation
    
    def eating(self):
        body = pygame.Rect(self.bodyposition_x, self.bodyposition_y, self.size[0] * self.factor_x, self.size[1] * self.factor_y)
        food = pygame.Rect(self.food_pos_x,self.food_pos_y,self.size[0],self.size[1])
        if body.colliderect(food):
            self.score += 1
            self.growth()
            self.eaten_food = True
        else:
            pass