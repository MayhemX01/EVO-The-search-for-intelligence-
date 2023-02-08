import pygame

window_x = 1600
window_y = 900

player_shot = pygame.image.load("misc imgs/p shot.png").convert_alpha()
player_shot = pygame.transform.scale(player_shot,(window_x * .005,window_y * .01))
player_shot_list_F = []
player_shot_list_B = []
player_shot_attack_count = 0

player_base = pygame.image.load("player imgs/base.png").convert_alpha()
player_base = pygame.transform.scale(player_base, (window_x * .03, window_y * .03))

player_sight = pygame.image.load("player imgs/eye.png").convert_alpha()
player_sight = pygame.transform.scale(player_sight, (window_x * .03, window_y * .03))

player_fin = pygame.image.load("player imgs/eye+fin.png").convert_alpha()
player_fin = pygame.transform.scale(player_fin, (window_x * .03, window_y * .03))

player_tail = pygame.image.load("player imgs/eye+tail.png").convert_alpha()
player_tail = pygame.transform.scale(player_tail, (window_x * .03, window_y * .03))

player_fin_tail = pygame.image.load("player imgs/eye+tail+fin.png").convert_alpha()
player_fin_tail = pygame.transform.scale(player_fin_tail, (window_x * .03, window_y * .03))

player_attack = pygame.image.load("player imgs/eye+tail+fin+attack.png").convert_alpha()
player_attack = pygame.transform.scale(player_attack, (window_x * .03, window_y * .03))

class Player(object):
    def __init__(self):
        self.base = player_base
        self.eye = player_sight
        self.tail = player_tail
        self.fin = player_fin
        self.tail_fin = player_fin_tail
        self.attack = player_attack
        self.h = self.base.get_height()
        self.w = self.base.get_width()
        self.h = self.base.get_height()
        self.w = self.base.get_width()
        self.x = 50
        self.y = window_y // 2 - self.h // 2
        self.rect = self.base.get_rect(center=(self.x, self.y))

    def draw_forward_base(self,player_rotate_degree, window):
        self.rotate = pygame.transform.rotozoom(self.base, player_rotate_degree, 1)
        window.blit(self.rotate, (self.x, self.y))

    def draw_reverse_base(self,player_rotate_degree,window):
        self.flip = pygame.transform.flip(self.base, flip_x=True, flip_y=False)
        self.rotate = pygame.transform.rotozoom(self.flip, player_rotate_degree, 1)
        window.blit(self.rotate , (self.x, self.y))



    def draw_forward_eye(self,player_rotate_degree, window):
        self.rotate = pygame.transform.rotozoom(self.eye, player_rotate_degree, 1)
        window.blit(self.rotate, (self.x, self.y))

    def draw_reverse_eye(self,player_rotate_degree,window):
        self.flip = pygame.transform.flip(self.eye, flip_x=True, flip_y=False)
        self.rotate = pygame.transform.rotozoom(self.flip, player_rotate_degree, 1)
        window.blit(self.rotate , (self.x, self.y))



    def draw_forward_tail(self,player_rotate_degree, window):
        self.rotate = pygame.transform.rotozoom(self.tail, player_rotate_degree, 1)
        window.blit(self.rotate, (self.x, self.y))

    def draw_reverse_tail(self,player_rotate_degree,window):
        self.flip = pygame.transform.flip(self.tail, flip_x=True, flip_y=False)
        self.rotate = pygame.transform.rotozoom(self.flip, player_rotate_degree, 1)
        window.blit(self.rotate , (self.x, self.y))



    def draw_forward_fin(self,player_rotate_degree, window):
        self.rotate = pygame.transform.rotozoom(self.fin, player_rotate_degree, 1)
        window.blit(self.rotate, (self.x, self.y))

    def draw_reverse_fin(self,player_rotate_degree,window):
        self.flip = pygame.transform.flip(self.fin, flip_x=True, flip_y=False)
        self.rotate = pygame.transform.rotozoom(self.flip, player_rotate_degree, 1)
        window.blit(self.rotate , (self.x, self.y))



    def draw_forward_tail_fin(self,player_rotate_degree, window):
        self.rotate = pygame.transform.rotozoom(self.tail_fin, player_rotate_degree, 1)
        window.blit(self.rotate, (self.x, self.y))

    def draw_reverse_tail_fin(self,player_rotate_degree,window):
        self.flip = pygame.transform.flip(self.tail_fin, flip_x=True, flip_y=False)
        self.rotate = pygame.transform.rotozoom(self.flip, player_rotate_degree, 1)
        window.blit(self.rotate , (self.x, self.y))



    def draw_forward_attack(self,player_rotate_degree, window):
        self.rotate = pygame.transform.rotozoom(self.attack, player_rotate_degree, 1)
        window.blit(self.rotate, (self.x, self.y))

    def draw_reverse_attack(self,player_rotate_degree,window):
        self.flip = pygame.transform.flip(self.attack, flip_x=True, flip_y=False)
        self.rotate = pygame.transform.rotozoom(self.flip, player_rotate_degree, 1)
        window.blit(self.rotate , (self.x, self.y))

class Player_Shot(object):
    def __init__(self):
        self.img = player_shot
        self.rotate = pygame.transform.rotozoom(self.img, 270, 1)

    def create_player_shot(self,x,y):
        self.x = x
        self.y = y
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect

    def move_player_shot_forward(self,player_shot_list_F):
        for e in player_shot_list_F:
            e.centerx += 2
        return player_shot_list_F

    def move_player_shot_backward(self,player_shot_list_B):
        for e in player_shot_list_B:
            e.centerx -= 3
        return player_shot_list_B

    def draw_player_shot(self,player_shot_list_F, window):
        for i in player_shot_list_F:
            window.blit(self.rotate, i)

    def draw_player_shot(self,player_shot_list_B, window):
        for i in player_shot_list_B:
            window.blit(self.rotate, i)