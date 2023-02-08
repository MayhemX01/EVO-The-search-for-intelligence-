import pygame , sys, random, threading
from pygame.locals import *

pygame.init()

pygame.mixer.pre_init(44100,-16,2,512)
pygame.mixer.init()
pygame.mixer.music.load("audio/Music.wav")
pygame.mixer.music.play(-1)

fire_sound = pygame.mixer.Sound(file="audio/Fire.wav")
eating_sound = pygame.mixer.Sound(file="audio/Food.wav")
hit_sound = pygame.mixer.Sound(file="audio/Hit.wav")
evo_sound = pygame.mixer.Sound(file="audio/Powerup.wav")
shooting_sound = pygame.mixer.Sound(file="audio/Shooting.wav")
user_select_sound = pygame.mixer.Sound(file="audio/User_Select.wav")
zaped_sound = pygame.mixer.Sound(file="audio/Zaped.wav")

REZ = False
REZ2 = False

last_ticks = 0
count = 0

flags = FULLSCREEN | DOUBLEBUF | HWACCEL | SCALED

window_x = 1600
window_y = 900

window = pygame.display.set_mode((window_x, window_y),flags,vsync=1)

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

background = pygame.image.load("backgrounds/background.png").convert()
background = pygame.transform.scale(background,(window_x,window_y))
background_h = background.get_height()
background_w = background.get_width()
background_x_position = 0

regular_blob = pygame.image.load("enemy imgs/regular_blob_base.png").convert_alpha()
regular_blob = pygame.transform.scale(regular_blob, (window_x * .03, window_y * .03))
regular_blob_list = []
regular_blob_attack_count = 0

fire_blob = pygame.image.load("enemy imgs/fire_blob_base.png").convert_alpha()
fire_blob = pygame.transform.scale(fire_blob,(window_x * .045,window_y * .035))
fire_blob_list = []
fire_blob_attack_count = 0

electric_blob = pygame.image.load("enemy imgs/electric_blob_base.png").convert_alpha()
electric_blob = pygame.transform.scale(electric_blob,(window_x * .03,window_y * .03))
electric_blob_list = []

electric_shot = pygame.image.load("enemy imgs/shot.png").convert_alpha()
electric_shot = pygame.transform.scale(electric_shot,(window_x * .01,window_y * .01))
electric_shot_list = []
electric_shot_attack_count = 0

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

poison = pygame.image.load("food imgs/poison_move_1.png").convert_alpha()
poison = pygame.transform.scale(poison,(window_x * .02,window_y * .02))
poison_list = []

food = pygame.image.load("food imgs/food_move_1.png").convert_alpha()
food = pygame.transform.scale(food,(window_x * .02,window_y * .02))
food_list = []

player = pygame.image.load("player imgs/base.png").convert_alpha()
player = pygame.transform.scale(player, (window_x * .03, window_y * .03))


player_move_up = False
player_move_down = False
player_move_left = False
player_move_right = False

player_x = 0
player_y = 0

player_tail_evo = False
player_health_evo = False

player_rotate_degree = 0
not_stuned = 0

forward_key = False
back_key = False
up_key = False
down_key = False

# CLASSES

class Player(object):
    def __init__(self):
        self.img = player
        self.h = self.img.get_height()
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.w = self.img.get_width()
        self.x = 50
        self.y = window_y // 2 - self.h // 2
        self.rect = player.get_rect(center=(self.x, self.y))


    def draw_forward(self, window):
        self.rotate = pygame.transform.rotozoom(self.img, player_rotate_degree, 1)
        window.blit(self.rotate, (self.x, self.y))

    def draw_reverse(self,window):
        self.flip = pygame.transform.flip(self.img, flip_x=True, flip_y=False)
        self.rotate = pygame.transform.rotozoom(self.flip, player_rotate_degree, 1)
        window.blit(self.rotate , (self.x, self.y))

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

    def draw_regular_blob(self, regular_blob_list):
        for i in regular_blob_list:
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

    def draw_fire_blob(self, fire_blob_list):
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

    def draw_electric_blob(self,electric_blob_list):
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

    def draw_electric_shot(self,electric_shot_list):
        for i in electric_shot_list:
            window.blit(self.img, i)


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

    def draw_poison(self,poison_list):
        for i in poison_list:
            window.blit(self.img, i)

class Food(object):
    def __init__(self):
        self.img = food
        self.h = self.img.get_height()
        self.w = self.img.get_width()
    def create_food(self):
        self.x = random.randrange(window_x, window_x + 200)
        self.y = random.randrange(0 + 25, window_y - 50)
        self.rect = self.img.get_rect(center=(self.x, self.y))
        return self.rect

    def move_food(self,food_list):
        for i in food_list:
            i.centerx -= 3
        return food_list

    def draw_food(self,food_list):
        for i in food_list:
            window.blit(self.img, i)

# CLASS FUNCTIONS

run_Player = Player()
run_Regular_Blob = Regular_Blob()
run_Fire_Blob = Fire_Blob()
run_Electric_Blob = Electric_Blob()
run_Electric_Shot = Electric_Shot()
run_Poison = Poison()
run_Food = Food()

# WHILE LOOP TRIGGERS

def Spawn_Timers():

    global  count

    if not paused:

        count += 1

        if count % 220 == 0:
            ran = random.choice([1, 2, 3])
            grass_list.append(Grass(ran))

        for g in grass_list:
            g.x -= g.xv
            g.y += g.yv

        if count % 1000 == 0:
            ran = random.choice([1, 2, 3])
            bush_list.append(Bush(ran))

        for b in bush_list:
            b.x -= b.xv
            b.y += b.yv

        if count % 185 == 0:
            ran = random.choice([1, 2, 3, 4, 5])
            seaweed_list.append(Seaweed(ran))

        for s in seaweed_list:
            s.x -= s.xv
            s.y += s.yv

        if count % 200 == 0:
            ran = random.choice([1, 2, 3, 4, 5])
            seaweed_2_list.append(Seaweed(ran))

        for s in seaweed_2_list:
            s.x -= s.xv
            s.y += s.yv

        if count % 1225 == 0:
            ran = random.choice([1, 2, 3, 4, 5])
            rock_list.append(Rock(ran))

        for r in rock_list:
            r.x -= r.xv
            r.y += r.yv

        if count % 1150 == 0:
            ran = random.choice([1, 2, 3, 4, 5])
            rock_2_list.append(Rock2(ran))

        for r in rock_2_list:
            r.x -= r.xv
            r.y += r.yv

        if count % 500 == 0:
            regular_blob_list.append(run_Regular_Blob.create_regular_blob())
        if count % 1000 == 0:
            fire_blob_list.append(run_Fire_Blob.create_fire_blob())
        if count % 2500 == 0:
            electric_blob_list.append(run_Electric_Blob.create_electric_blob())
        if count % 3000 == 0:
            poison_list.append(run_Poison.create_poison())
        if count % 250 == 0:
            food_list.append(run_Food.create_food())

def Game_Counters():

    global life_points,player_health_evo,evolution_points,not_stuned,gameover,regular_blob_attack_count,fire_blob_attack_count,electric_shot_attack_count

    if player_health_evo:
        if life_points >= 100:
            life_points = 100

    if not player_health_evo:
        if life_points >= 50:
            life_points = 50

    if life_points <= 0:
        gameover = True

    if evolution_points >= 50:
        evolution_points = 50

    if not_stuned >= 0:
        not_stuned = not_stuned - 1

    if gameover:
        GameOver()

    if regular_blob_attack_count >= 0:
        regular_blob_attack_count -= 1

    if fire_blob_attack_count >= 0:
        fire_blob_attack_count -= 1

    if electric_shot_attack_count >= 0:
        electric_shot_attack_count -= 1

def Collision_check():

    global evolution_points,life_points,score_points,not_stuned,gameover,regular_blob_attack_count,fire_blob_attack_count,electric_shot_attack_count

    # Enemys

    for i, r in enumerate(regular_blob_list):
        if run_Player.x + 200 > r.x and run_Player.x < r.x and r.y < run_Player.y + 125 and r.y > run_Player.y:
            r.y -= 1
        if run_Player.x + 200 > r.x and run_Player.x < r.x and r.y > run_Player.y - 125 and r.y < run_Player.y:
            r.y += 1
        if r.x < -100:
            regular_blob_list.pop(i)
        if run_Player.rect.colliderect(r):
            if regular_blob_attack_count <= 0:
                pygame.mixer.Sound.play(hit_sound)
                regular_blob_attack_count = 30
                life_points = life_points - 5

    for i, f in enumerate(fire_blob_list):
        if run_Player.x + 125 > f.x and run_Player.x < f.x and f.y < run_Player.y + 75 and f.y > run_Player.y:
            f.y -= 2
        if run_Player.x + 125 > f.x and run_Player.x < f.x and f.y > run_Player.y - 75 and f.y < run_Player.y:
            f.y += 2
        if f.x < -100:
            fire_blob_list.pop(i)
        if run_Player.rect.colliderect(f):
            if fire_blob_attack_count <= 0:
                pygame.mixer.Sound.play(hit_sound)
                pygame.mixer.Sound.play(fire_sound)
                fire_blob_attack_count = 60
                life_points = life_points - 20

    for i, e in enumerate(electric_blob_list):
        x = e.x
        y = e.y
        if e.x < -100:
            electric_blob_list.pop(i)
        if e.x < run_Player.x + 1000 and e.x > run_Player.x:
            if electric_shot_attack_count <= 0:
                pygame.mixer.Sound.play(shooting_sound)
                electric_shot_list.append(run_Electric_Shot.create_electric_shot(x,y))
                electric_shot_attack_count = 120
        if run_Player.rect.colliderect(e):
            pygame.mixer.Sound.play(hit_sound)
            pygame.mixer.Sound.play(zaped_sound)
            electric_blob_list.pop(i)
            not_stuned = 180
            life_points -= 30

    for i, f in enumerate(food_list):
        if f.x < -100:
            food_list.pop(i)
        if run_Player.rect.colliderect(f):
            pygame.mixer.Sound.play(eating_sound)
            score_points = score_points + 100
            evolution_points = evolution_points + 1
            life_points = life_points + 5
            food_list.pop(i)

    for i, p in enumerate(poison_list):
        if p.x < -100:
            poison_list.pop(i)
        if run_Player.rect.colliderect(p):
            pygame.mixer.Sound.play(hit_sound)
            poison_list.pop(i)
            gameover = True

    for i, s in enumerate(electric_shot_list):
        if s.y > window_y - 30:
            electric_shot_list.pop(i)
        if run_Player.rect.colliderect(s):
            pygame.mixer.Sound.play(hit_sound)
            pygame.mixer.Sound.play(zaped_sound)
            life_points -= 10
            not_stuned = 180
            electric_shot_list.pop(i)

    # Background decor

    for i, g in enumerate(grass_list):
        if g.x < -100:
            grass_list.pop(i)

    for i, s in enumerate(seaweed_list):
        if s.x < -100:
            seaweed_list.pop(i)

    for i, s in enumerate(seaweed_2_list):
        if s.x < -100:
            seaweed_2_list.pop(i)

    for i, b in enumerate(bush_list):
        if b.x < -100:
            bush_list.pop(i)

    for i, r in enumerate(rock_list):
        if r.x < -100:
            rock_list.pop(i)

    for i, r in enumerate(rock_2_list):
        if r.x < -100:
            rock_2_list.pop(i)

    # Player

    if run_Player.x <= 0:
        run_Player.x = 0

    if run_Player.x + 50>= window_x:
        run_Player.x = window_x - 50

    if run_Player.y <= 0:
        run_Player.y = 0

    if run_Player.y + 30 >= window_y:
        run_Player.y = window_y - 30

def GameEvents():

    global player_move_up,player_move_down,player_move_left,player_move_right,player_x,player_y,player_rotate_degree,forward_key,back_key,up_key,down_key,paused,gameover,life_points,score_points,evolution_points,REZ,REZ2,gamestart,player_initilize,evo_menu,player_tail_evo,player_health_evo

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                if game_menu:
                    if not player_speed_evo:
                        if evolution_points >= 25:
                            pygame.mixer.Sound.play(evo_sound)
                            evolution_points -= 25
                            player_speed_evo = True

            if event.key == pygame.K_2:
                if game_menu:
                    if not player_health_evo:
                        if evolution_points >= 25:
                            pygame.mixer.Sound.play(evo_sound)
                            evolution_points -= 25
                            player_health_evo = True

            if event.key == pygame.K_i:
                if gamestart:
                    pygame.mixer.Sound.play(user_select_sound)
                    gamestart = False
                    player_initilize = True
                    paused = False
                    player_initilize = False

            if event.key == pygame.K_m:
                if paused:
                    pygame.mixer.Sound.play(user_select_sound)
                    game_menu = True

            if event.key == pygame.K_p:
                if not gameover:
                    pygame.mixer.Sound.play(user_select_sound)
                    paused = True

            if event.key == pygame.K_u:
                if not gameover:
                    pygame.mixer.Sound.play(user_select_sound)
                    paused = False
                    game_menu = False

            if event.key == pygame.K_TAB:
                if gameover:
                    pygame.mixer.Sound.play(user_select_sound)
                    gameover = False
                    life_points = 100
                    score_points = 0
                    evolution_points = 0
                    paused = False
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_w: # up
                up_key = True
                player_move_up = True
                if forward_key:
                    player_rotate_degree += 25
                if back_key:
                    player_rotate_degree -= 25

            if event.key == pygame.K_s: # down
                down_key = True
                player_move_down = True
                if forward_key:
                    player_rotate_degree -= 25
                if back_key:
                    player_rotate_degree += 25

            if event.key == pygame.K_a: # back
                back_key = True
                player_move_left = True
                if up_key:
                    player_rotate_degree -= 25
                if down_key:
                    player_rotate_degree += 25

            if event.key == pygame.K_d: # forward
                forward_key = True
                player_move_right = True
                if up_key:
                    player_rotate_degree += 25
                if down_key:
                    player_rotate_degree -= 25

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: # up
                up_key = False
                player_move_up = False
                if forward_key:
                    player_rotate_degree -= 25
                if back_key:
                    player_rotate_degree += 25

            if event.key == pygame.K_s: # down
                down_key = False
                player_move_down = False
                if forward_key:
                    player_rotate_degree += 25
                if back_key:
                    player_rotate_degree -= 25

            if event.key == pygame.K_a: # back
                back_key = False
                player_move_left = False
                if up_key:
                    player_rotate_degree += 25
                if down_key:
                    player_rotate_degree -= 25

            if event.key == pygame.K_d: # forward
                forward_key = False
                player_move_right = False
                if up_key:
                    player_rotate_degree -= 25
                if down_key:
                    player_rotate_degree += 25



    if not paused:
        if not_stuned <= 0:
            if player_speed_evo:
                if player_move_up:
                    run_Player.y -= 2
                if player_move_down:
                    run_Player.y += 2
                if player_move_left:
                    run_Player.x -= 3
                if player_move_right:
                    run_Player.x += 2
        if not_stuned <= 0:
            if not player_speed_evo:
                if player_move_up:
                    run_Player.y -= 1
                if player_move_down:
                    run_Player.y += 1
                if player_move_left:
                    run_Player.x -= 2
                if player_move_right:
                    run_Player.x += 1

def MovingBackground_Menus():

    global background_x_position,paused,score_points,evolution_points,gamestart,gameover

    if not paused:

        background_x_position -= 1
        if background_x_position == -window_x:
            background_x_position = 0

        window.blit(background, (background_x_position, 0))
        window.blit(background,(background_x_position + window_x, 0))

        pygame.draw.rect(window, (0, 0, 0), [10, window_y - 51, 102, 17])
        pygame.draw.rect(window, (6, 251, 64), [11, window_y - 50, evolution_points * 2, 15])

        if player_health_evo:
            pygame.draw.rect(window, (0, 0, 0), [10, window_y - 31, 202, 17])

        if not player_health_evo:
            pygame.draw.rect(window, (0, 0, 0), [10, window_y - 31, 102, 17])

        pygame.draw.rect(window, (250, 11, 4), [11, window_y - 30, life_points * 2, 15])

        Score_Text2 = Score_Font.render('Score: ' + str(score_points), True, (255, 255, 255))
        window.blit(Score_Text2, (5, 5))



    if paused:

        window.fill("Black")

        Evo_Text = Score_Font.render('Press (M) To Enter', True, (255, 255, 255))
        window.blit(Evo_Text, (window_x // 2 - 75, window_y // 2 + 195))

        Evo_Text2 = Score_Font.render('The Evolution Menu', True, (255, 255, 255))
        window.blit(Evo_Text2, (window_x // 2 - 75, window_y // 2 + 220))

        Paused_Text = Paused_Font.render('PAUSED', True, (255, 255, 255))
        window.blit(Paused_Text, (window_x // 2 - 75, window_y // 2))

        Score_Text = Score_Font.render('Score: ' + str(score_points), True, (255, 255, 255))
        window.blit(Score_Text, (window_x // 2 - 75, window_y // 2 + 105))

        Evo_Point_text = Score_Font.render('Evo Points: ' + str(evolution_points), True, (255, 255, 255))
        window.blit(Evo_Point_text, (window_x // 2 - 75, window_y // 2 + 135))

        Hint_Text = Hints_Font.render('Press (U) to Unpause The Game', True, (255, 255, 255))
        window.blit(Hint_Text, (window_x // 2 - 75, window_y // 2 + 300))

        Hint_Text2 = Hints_Font.render('Press ESC To Exit The Game', True, (255, 255, 255))
        window.blit(Hint_Text2, (window_x // 2 - 75, window_y // 2 + 325))



        if evo_menu:

            window.fill("Black")

            Evo_Menu_Text = Paused_Font.render('Evolution', True, (255, 255, 255))
            window.blit(Evo_Menu_Text, (window_x // 2 - 100, window_y // 2))

            Cost_Text = Score_Font.render('Cost 25 Evo Points ', True, (255, 255, 255))
            window.blit(Cost_Text, (window_x // 2 - 75, window_y // 2 + 70))

            Speed_Evo_Text = Score_Font.render('Press 1 For Speed Evolution ', True, (255, 255, 255))
            window.blit(Speed_Evo_Text, (window_x // 2 - 120, window_y // 2 + 120))

            Life_Evo_Text = Score_Font.render('Press 2 For Health Evolution', True, (255, 255, 255))
            window.blit(Life_Evo_Text, (window_x // 2 - 120, window_y // 2 + 150))

            Evo_Point_text1 = Score_Font.render('Evo Points: ' + str(evolution_points), True, (255, 255, 255))
            window.blit(Evo_Point_text1, (window_x // 2 - 60, window_y // 2 + 200))

            Hint_Text2 = Hints_Font.render('Press (U) To Continue Playing', True, (255, 255, 255))
            window.blit(Hint_Text2, (window_x // 2 - 100, window_y // 2 + 250))



    if gameover:

        window.fill("Black")

        GameOverText = GameOver_Font.render('GAME OVER', True, (255, 255, 255))
        window.blit(GameOverText, (window_x // 2 - 125, window_y / 2))

        Score_text = Score_Font.render('Final Score: ' + str(score_points), True, (255, 255, 255))
        window.blit(Score_text, (window_x // 2 - 115, window_y // 2 + 85))

        Hint_Text2 = Hints_Font.render('Press ESC To Exit The Game', True, (255, 255, 255))
        window.blit(Hint_Text2, (window_x // 2 - 115, window_y // 2 + 155))

        Hint_Text3 = Hints_Font.render('Press TAB To Restart', True, (255, 255, 255))
        window.blit(Hint_Text3, (window_x // 2 - 115, window_y // 2 + 135))

    if gamestart:

        window.fill("Black")

        paused = True

        Game_Start_Text = Paused_Font.render('GAME START', True, (255, 255, 255))
        window.blit(Game_Start_Text, (window_x // 2 - 160, window_y / 2))

        Initizlize_Game = Score_Font.render('Please (I) When Ready To Play', True, (255, 255, 255))
        window.blit(Initizlize_Game, (window_x // 2 - 135, window_y // 2 + 100))

        P_Input_Text1 = Hints_Font.render('Press ESC To Exit Game', True, (255, 255, 255))
        window.blit(P_Input_Text1, (10, 5))

        P_Input_Text2 = Hints_Font.render('Press (P) For Menu Screen', True, (255, 255, 255))
        window.blit(P_Input_Text2, (10, 30))

        P_Input_Text3 = Hints_Font.render('Press (W) To Move Up', True, (255, 255, 255))
        window.blit(P_Input_Text3, (10, 55))

        P_Input_Text4 = Hints_Font.render('Press (S) To Move Down ', True, (255, 255, 255))
        window.blit(P_Input_Text4, (10, 80))

        P_Input_Text5 = Hints_Font.render('Press (D) To Move Forward', True, (255, 255, 255))
        window.blit(P_Input_Text5, (10, 105))

        P_Input_Text6 = Hints_Font.render('Press (A) To Move Backward', True, (255, 255, 255))
        window.blit(P_Input_Text6, (10, 130))

def reDrawGameWindow():

    global food_list,poison_list,regular_blob_list,fire_blob_list,electric_blob_list,electric_shot_list,forward_key

    if not paused:

        if back_key:
            run_Player.draw_reverse(window)
        else:
            run_Player.draw_forward(window)

        # Enemys

        regular_blob_list = run_Regular_Blob.move_regular_blob(regular_blob_list)
        run_Regular_Blob.draw_regular_blob(regular_blob_list)

        fire_blob_list = run_Fire_Blob.move_fire_blob(fire_blob_list)
        run_Fire_Blob.draw_fire_blob(fire_blob_list)

        electric_blob_list = run_Electric_Blob.move_electric_blob(electric_blob_list)
        run_Electric_Blob.draw_electric_blob(electric_blob_list)

        electric_shot_list = run_Electric_Shot.move_electric_shot(electric_shot_list)
        run_Electric_Shot.draw_electric_shot(electric_shot_list)

        # Foliage

        for r in rock_list:
            r.draw(window)

        for r in rock_2_list:
            r.draw(window)

        for g in grass_list:
            g.draw(window)

        for b in bush_list:
            b.draw(window)

        for s in seaweed_list:
            s.draw(window)

        for s in seaweed_2_list:
            s.draw(window)

        # Non Moving

        poison_list = run_Poison.move_poison(poison_list)
        run_Poison.draw_poison(poison_list)

        food_list = run_Food.move_food(food_list)
        run_Food.draw_food(food_list)

def GameOver():

    global gameover,score_points,paused

    # Background decor

    for i, g in enumerate(grass_list):
        grass_list.pop(i)

    for i, s in enumerate(seaweed_list):
        seaweed_list.pop(i)

    for i, s in enumerate(seaweed_2_list):
        seaweed_2_list.pop(i)

    for i, b in enumerate(bush_list):
        bush_list.pop(i)

    for i, r in enumerate(rock_list):
        rock_list.pop(i)

    for i, r in enumerate(rock_2_list):
        rock_2_list.pop(i)

    # Enemys

    for i, r in enumerate(regular_blob_list):
        regular_blob_list.pop(i)

    for i, f in enumerate(fire_blob_list):
        fire_blob_list.pop(i)

    for i, e in enumerate(electric_blob_list):
        electric_blob_list.pop(i)

    for i, f in enumerate(food_list):
        food_list.pop(i)

    for i, p in enumerate(poison_list):
        poison_list.pop(i)

    for i, s in enumerate(electric_shot_list):
        electric_shot_list.pop(i)

    for i, f in enumerate(food_list):
        food_list.pop(i)

    run_Player.x = 50
    run_Player.y = window_y // 2 - run_Player.h // 2

    paused = True

while gameactive:

    run_Player.rect.y = run_Player.y
    run_Player.rect.x = run_Player.x

    t0 = threading.Thread(target=Spawn_Timers())
    t0.start()
    t1 = threading.Thread(target=Game_Counters())
    t1.start()
    t2 = threading.Thread(target=Collision_check())
    t2.start()
    t3 = threading.Thread(target=GameEvents())
    t3.start()
    MovingBackground_Menus()
    reDrawGameWindow()
    clock.tick(60)

    pygame.display.flip()

# Made by Mayhem X01