import pygame

window_x = 1600
window_y = 900

background = pygame.image.load("backgrounds/background.png").convert()
background = pygame.transform.scale(background,(window_x,window_y))
background_h = background.get_height()
background_w = background.get_width()
background_x_position = 0

gamestart_img = pygame.image.load("menus/gamestart.png").convert_alpha()
gamestart_img_H = gamestart_img.get_height()
gamestart_img_W = gamestart_img.get_width()

gamestart_menu_img = pygame.image.load("menus/gamestart_menu.png").convert_alpha()
gamestart_menu_img_H = gamestart_menu_img.get_height()
gamestart_menu_img_W = gamestart_menu_img.get_width()

paused_img = pygame.image.load("menus/paused.png").convert_alpha()
paused_img_H = paused_img.get_height()
paused_img_W = paused_img.get_width()

paused_menu_img = pygame.image.load("menus/pause_menu.png").convert_alpha()
paused_menu_img_H = paused_menu_img.get_height()
paused_menu_img_W = paused_menu_img.get_width()

evo_img = pygame.image.load("menus/evo.png").convert_alpha()
evo_img_H = evo_img.get_height()
evo_img_W = evo_img.get_width()

evo_menu_img = pygame.image.load("menus/evo_menu.png").convert_alpha()
evo_menu_img_H = evo_menu_img.get_height()
evo_menu_img_W = evo_menu_img.get_width()

gameover_img = pygame.image.load("menus/gameover.png").convert_alpha()
gameover_img_H = gameover_img.get_height()
gameover_img_W = gameover_img.get_width()

gameover_menu_img = pygame.image.load("menus/gameover_menu.png").convert_alpha()
gameover_menu_img_H = gameover_menu_img.get_height()
gameover_menu_img_W = gameover_menu_img.get_width()