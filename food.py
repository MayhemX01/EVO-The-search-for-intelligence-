import pygame, random

window_x = 1600
window_y = 900

food = pygame.image.load("food imgs/food.png").convert_alpha()
food_list = []

moving_food = pygame.image.load("food imgs/moving food.png").convert_alpha()
moving_food_list = []

class Food(object):
    def __init__(self):
        self.img = food
        self.h = self.img.get_height()
        self.w = self.img.get_width()
    def create_food(self):
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(50, window_y - 50)
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect

    def move_food(self,food_list):
        for i in food_list:
            i.centerx -= 3
        return food_list

    def draw_food(self,food_list,window):
        for i in food_list:
            window.blit(self.img, i)

class Moving_Food(object):
    def __init__(self):
        self.img = moving_food
        self.h = self.img.get_height()
        self.w = self.img.get_width()
    def create_moving_food(self):
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(100, window_y - 100)
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect

    def move_moving_food(self,moving_food_list):
        for i in moving_food_list:
            i.centerx -= 3
        return moving_food_list

    def draw_moving_food(self,moving_food_list,window):
        for i in moving_food_list:
            window.blit(self.img, i)