import pygame
from pygame.locals import *

flags = FULLSCREEN | SCALED

window_x = 1600
window_y = 900

clock = pygame.time.Clock()
Score_Font = pygame.font.SysFont('Times', 20)
GameOver_Font = pygame.font.SysFont('Times', 50)
Paused_Font = pygame.font.SysFont('Times', 50)
Hints_Font = pygame.font.SysFont('Times', 15)

gameactive = True
gameover = False
paused = False
gamestart = True
player_initilize = True
evo_menu = False

evolution_points = 0
life_points = 50
score_points = 0

count = 0

player_move_up = False
player_move_down = False
player_move_left = False
player_move_right = False

player_x = 0
player_y = 0

E = False

player_start_evo = True
player_eye_evo = False
player_tail_evo = False
player_fin_evo = False
player_tail_fin_evo = False
player_attack_evo = False
player_health_evo = False

player_rotate_degree = 0
not_stuned = 0
slow_count = 0

forward_key = False
back_key = False
up_key = False
down_key = False

window = pygame.display.set_mode((window_x, window_y),flags,vsync=1)