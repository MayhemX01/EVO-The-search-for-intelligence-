import pygame, random

window_x = 1600
window_y = 900

regular_blob = pygame.image.load("enemy imgs/regular blob base.png").convert_alpha()
regular_blob = pygame.transform.scale(regular_blob, (window_x * .03, window_y * .03))
regular_blob_list = []
regular_blob_attack_count = 0

jumping_blob = pygame.image.load("enemy imgs/jumping blob.png").convert_alpha()
jumping_blob_list = []
jumping_blob_attack_count = 0

fire_blob = pygame.image.load("enemy imgs/fire blob base.png").convert_alpha()
fire_blob = pygame.transform.scale(fire_blob,(window_x * .045,window_y * .035))
fire_blob_list = []
fire_blob_attack_count = 0

electric_blob = pygame.image.load("enemy imgs/electric blob base.png").convert_alpha()
electric_blob = pygame.transform.scale(electric_blob,(window_x * .03,window_y * .03))
electric_blob_list = []

electric_shot = pygame.image.load("misc imgs/e shot.png").convert_alpha()
electric_shot = pygame.transform.scale(electric_shot,(window_x * .01,window_y * .01))
electric_shot_list = []
electric_shot_attack_count = 0

poison = pygame.image.load("misc imgs/poison.png").convert_alpha()
poison = pygame.transform.scale(poison,(window_x * .02,window_y * .02))
poison_list = []

barrier = pygame.image.load("misc imgs/barrier.png").convert_alpha()
barrier1 = pygame.image.load("misc imgs/barrier 1.png").convert_alpha()
barrier2 = pygame.image.load("misc imgs/barrier 2.png").convert_alpha()
barrier_list = []

class Regular_Blob(object):
    def __init__(self):
        self.img = regular_blob

    def create_regular_blob(self):
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(95, window_y - 50)
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect


    def move_regular_blob(self, regular_blob_list):
        for i in regular_blob_list:
            i.centerx -= 2
        return regular_blob_list

    def draw_regular_blob(self, regular_blob_list, window):
        for i in regular_blob_list:
            window.blit(self.img, i)

class Jumping_Blob(object):
    def __init__(self):
        self.img = jumping_blob

    def create_jumping_blob(self):
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(window_y - 50, window_y - 10)
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect


    def move_jumping_blob(self, jumping_blob_list):
        for i in jumping_blob_list:
            i.centerx -= 2
        return jumping_blob_list

    def draw_jumping_blob(self, jumping_blob_list, window):
        for i in jumping_blob_list:
            window.blit(self.img, i)

class Fire_Blob(object):
    def __init__(self):
        self.img = fire_blob

    def create_fire_blob(self):
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(95, window_y - 50)
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect


    def move_fire_blob(self, fire_blob_list):
        for i in fire_blob_list:
            i.centerx -= 2
        return fire_blob_list

    def attack_fire_blob(self, fire_blob_list):
        for i in fire_blob_list:
            self.count = 120
            i.centerx -= 2
        return fire_blob_list

    def draw_fire_blob(self, fire_blob_list, window):
        for i in fire_blob_list:
            window.blit(self.img, i)

class Electric_Blob(object):
    def __init__(self):
        self.img = electric_blob

    def create_electric_blob(self):
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(0 + 15, 80 )
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect

    def move_electric_blob(self,electric_blob_list):
        for i in electric_blob_list:
            i.centerx -= 2
        return electric_blob_list

    def draw_electric_blob(self,electric_blob_list, window):
        for i in electric_blob_list:
            window.blit(self.img, i)

class Electric_Shot(object):
    def __init__(self):
        self.img = electric_shot

    def create_electric_shot(self,x,y):
        self.x = x
        self.y = y
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect

    def move_electric_shot(self,electric_shot_list):
        for e in electric_shot_list:
            e.centery += 3
        return electric_shot_list

    def draw_electric_shot(self,electric_shot_list, window):
        for i in electric_shot_list:
            window.blit(self.img, i)

class Poison(object):
    def __init__(self):
        self.img = poison

    def create_poison(self):
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(0 + 25, window_y - 50)
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect


    def move_poison(self,poison_list):
        for i in poison_list:
            i.centerx -= 4
        return poison_list

    def draw_poison(self,poison_list, window):
        for i in poison_list:
            window.blit(self.img, i)

class Barrier(object):
    def __init__(self):
        self.barrier = barrier
        self.barrier1 = barrier1
        self.barrier2 = barrier2
        self.rnd_img = [self.barrier, self.barrier1, self.barrier2]

    def create_barrier(self):
        self.img = random.choice(self.rnd_img)
        self.h = self.img.get_height()
        self.w = self.img.get_width()
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(300, window_y - 200)
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect


    def move_barrier(self, barrier_list):
        for i in barrier_list:
            i.centerx -= 1
        return barrier_list

    def draw_barrier(self, barrier_list, window):
        for i in barrier_list:
            window.blit(self.img, i)

