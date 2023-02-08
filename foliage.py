import pygame, random

window_x = 1600
window_y = 900

grass = pygame.image.load("folliage imgs/grass.png").convert_alpha()
grass1 = pygame.image.load("folliage imgs/grass 1.png").convert_alpha()
grass2 = pygame.image.load("folliage imgs/grass 2.png").convert_alpha()
grass_list = []

bush = pygame.image.load("folliage imgs/bush.png").convert_alpha()
bush1 = pygame.image.load("folliage imgs/bush 1.png").convert_alpha()
bush2 = pygame.image.load("folliage imgs/bush 2.png").convert_alpha()
bush_list = []

seaweed = pygame.image.load("folliage imgs/seaweed.png").convert_alpha()
seaweed1 = pygame.image.load("folliage imgs/seaweed 1.png").convert_alpha()
seaweed2 = pygame.image.load("folliage imgs/seaweed 2.png").convert_alpha()
seaweed3 = pygame.image.load("folliage imgs/seaweed 3.png").convert_alpha()
seaweed4 = pygame.image.load("folliage imgs/seaweed 4.png").convert_alpha()
seaweed_list = []
seaweed_2_list = []

rock = pygame.image.load("folliage imgs/rock.png").convert_alpha()
rock1 = pygame.image.load("folliage imgs/rock 1.png").convert_alpha()
rock2 = pygame.image.load("folliage imgs/rock 2.png").convert_alpha()
rock3 = pygame.image.load("folliage imgs/rock 3.png").convert_alpha()
rock4 = pygame.image.load("folliage imgs/rock 4.png").convert_alpha()
rock_list = []
rock_2_list = []

class Grass(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = grass
        elif self.rank == 2:
            self.image = grass1
        else:
            self.image = grass2
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(window_y - self.h, window_y - self.h + 70)
        self.xv = 1
        self.yv = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

class Bush(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = bush
        elif self.rank == 2:
            self.image = bush1
        else:
            self.image = bush2
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(window_y - self.h, window_y - self.h + 10)
        self.xv = 1
        self.yv = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

class Seaweed(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = seaweed
        elif self.rank == 2:
            self.image = seaweed1
        elif self.rank == 4:
            self.image = seaweed2
        elif self.rank == 4:
            self.image = seaweed3
        else:
            self.image = seaweed4
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(window_y - self.h, window_y - self.h + 50)
        self.xv = 1
        self.yv = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

class Rock(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = rock
        elif self.rank == 2:
            self.image = rock1
        elif self.rank == 4:
            self.image = rock2
        elif self.rank == 4:
            self.image = rock3
        else:
            self.image = rock4
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(window_y - self.h, window_y - self.h + 20)
        self.xv = 1
        self.yv = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

class Rock2(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = rock
        elif self.rank == 2:
            self.image = rock1
        elif self.rank == 4:
            self.image = rock2
        elif self.rank == 4:
            self.image = rock3
        else:
            self.image = rock4
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(window_y - self.h, window_y - self.h + 20)
        self.xv = 1
        self.yv = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))