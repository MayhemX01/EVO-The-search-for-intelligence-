import pygame, sys, threading

pygame.init()

from settings import *

from audio import *

from menus import  *

from player import  *

from enemys import *

from food import  *

from foliage import  *

run_Player = Player()
run_Regular_Blob = Regular_Blob()
run_Jumping_Blob = Jumping_Blob()
run_Fire_Blob = Fire_Blob()
run_Electric_Blob = Electric_Blob()
run_Electric_Shot = Electric_Shot()
run_Poison = Poison()
run_Barrier = Barrier()
run_Food = Food()
run_Moving_food = Moving_Food()
run_Player_Shot = Player_Shot()

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
            jumping_blob_list.append(run_Jumping_Blob.create_jumping_blob())
        if count % 750 == 0:
            fire_blob_list.append(run_Fire_Blob.create_fire_blob())
        if count % 2000 == 0:
            electric_blob_list.append(run_Electric_Blob.create_electric_blob())
        if count % 3000 == 0:
            poison_list.append(run_Poison.create_poison())
        if count % 2500 == 0:
            barrier_list.append(run_Barrier.create_barrier())
        if count % 250 == 0:
            food_list.append(run_Food.create_food())
        if count % 650 == 0:
            moving_food_list.append(run_Moving_food.create_moving_food())

def Game_Counters():

    global life_points,player_health_evo,evolution_points,not_stuned,gameover,regular_blob_attack_count,jumping_blob_attack_count,fire_blob_attack_count,electric_shot_attack_count,player_shot_attack_count,slow_count

    if player_shot_attack_count >= 0:
        player_shot_attack_count -= 1

    if player_health_evo:
        if life_points >= 75:
            life_points = 75

    if not player_health_evo:
        if life_points >= 50:
            life_points = 50

    if life_points <= 0:
        gameover = True

    if evolution_points >= 500:
        evolution_points = 500

    if not_stuned >= 0:
        not_stuned -= 1

    if slow_count >= 0:
        slow_count -= 1

    if gameover:
        GameOver()

    if regular_blob_attack_count >= 0:
        regular_blob_attack_count -= 1

    if jumping_blob_attack_count >= 0:
        jumping_blob_attack_count -= 1

    if fire_blob_attack_count >= 0:
        fire_blob_attack_count -= 1

    if electric_shot_attack_count >= 0:
        electric_shot_attack_count -= 1

def Collision_check():

    global evolution_points,life_points,score_points,not_stuned,gameover,regular_blob_attack_count,jumping_blob_attack_count,fire_blob_attack_count,electric_shot_attack_count,slow_count

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
                life_points -= 5



                # WORKING HERE ON PLAYER SHOOTING MECANICS



        for t, f in enumerate(player_shot_list_F):
            if f.x > r.x:
                if run_Player_Shot.rect.colliderect(r):
                    player_shot_list_F.pop(t)
                    regular_blob_list.pop(i)







    for i, j in enumerate(jumping_blob_list):
        if j.x < -100:
            jumping_blob_list.pop(i)

        if run_Player.x + 300 >= j.x and run_Player.x <= j.x:
            if run_Player.y + 200 >= j.y and run_Player.y <= j.y:
                j.x -= 2
                j.y -= 2

        if run_Player.rect.colliderect(j):
            if jumping_blob_attack_count <= 0:
                pygame.mixer.Sound.play(hit_sound)
                life_points -= 30
                jumping_blob_attack_count = 120

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
                life_points -= 20

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

    # Misc

    for i, p in enumerate(poison_list):
        if p.x < -100:
            poison_list.pop(i)
        if run_Player.rect.colliderect(p):
            pygame.mixer.Sound.play(hit_sound)
            poison_list.pop(i)
            gameover = True

    for i, b in enumerate(barrier_list):
        if b.x < -350:
            barrier_list.pop(i)
        if run_Player.rect.colliderect(b):
            slow_count = 2

    # Food

    for i, f in enumerate(food_list):
        if f.x < -100:
            food_list.pop(i)
        if run_Player.rect.colliderect(f):
            pygame.mixer.Sound.play(eating_sound)
            score_points = score_points + 50
            evolution_points = evolution_points + 1
            life_points = life_points + 2
            food_list.pop(i)

    for i, m in enumerate(moving_food_list):
        if m.x < -100:
            moving_food_list.pop(i)
        if run_Player.x + 200 > m.x and run_Player.x - 50 < m.x and m.y < run_Player.y + 125 and m.y > run_Player.y:
            m.y += 1
        if run_Player.x + 200 > m.x and run_Player.x - 50 < m.x and m.y > run_Player.y - 125 and m.y < run_Player.y:
            m.y -= 1
        if run_Player.rect.colliderect(m):
            pygame.mixer.Sound.play(eating_sound)
            score_points = score_points + 300
            evolution_points = evolution_points + 5
            life_points = life_points + 5
            moving_food_list.pop(i)

    # Shots

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

    global E,player_move_up,player_move_down,player_move_left,player_move_right,player_x,player_y,player_rotate_degree,forward_key,back_key,up_key,down_key,paused,gameover,life_points,score_points,evolution_points,REZ,REZ2,gamestart,player_initilize,evo_menu,player_eye_evo,player_tail_evo,player_fin_evo,player_attack_evo,player_health_evo,slow_count,player_shot_attack_count,player_start_evo,player_tail_fin_evo

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if evo_menu:
                if event.key == pygame.K_e:
                    E = True
                if E:
                    if event.key == pygame.K_1:
                        if not player_eye_evo or player_tail_evo or player_fin_evo or player_attack_evo or player_attack_evo or player_tail_fin_evo:
                            if evolution_points >= 10:
                                pygame.mixer.Sound.play(evo_sound)
                                evolution_points -= 10
                                player_eye_evo = True
                                player_start_evo = False

                    if event.key == pygame.K_2:
                        if player_eye_evo or player_fin_evo:
                            if not player_tail_evo or player_attack_evo or player_health_evo or player_tail_fin_evo:
                                if evolution_points >= 25:
                                    pygame.mixer.Sound.play(evo_sound)
                                    evolution_points -= 25
                                    player_eye_evo = False
                                    if player_fin_evo:
                                        player_tail_fin_evo = True
                                        player_fin_evo = False
                                    else:
                                        player_tail_evo = True

                    if event.key == pygame.K_3:
                        if player_eye_evo or player_tail_evo:
                            if not player_fin_evo or player_attack_evo or player_health_evo or player_tail_fin_evo:
                                if evolution_points >= 25:
                                    pygame.mixer.Sound.play(evo_sound)
                                    evolution_points -= 25
                                    player_eye_evo = False
                                    if player_tail_evo:
                                        player_tail_fin_evo = True
                                        player_tail_evo = False
                                    else:
                                        player_fin_evo = True

                    if event.key == pygame.K_4:
                        if player_tail_fin_evo or player_health_evo:
                            if not player_attack_evo:
                                if evolution_points >= 50:
                                    pygame.mixer.Sound.play(evo_sound)
                                    evolution_points -= 50
                                    player_attack_evo = True
                                    player_tail_fin_evo = False

                    if event.key == pygame.K_5:
                        if player_tail_fin_evo or player_attack_evo:
                            if not player_health_evo:
                                if evolution_points >= 50:
                                    pygame.mixer.Sound.play(evo_sound)
                                    evolution_points -= 50
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
                    evo_menu = True

            if event.key == pygame.K_p:
                if not gameover:
                    pygame.mixer.Sound.play(user_select_sound)
                    paused = True

            if event.key == pygame.K_u:
                if not gameover:
                    pygame.mixer.Sound.play(user_select_sound)
                    paused = False
                    evo_menu = False

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

            if event.key == pygame.K_SPACE:

                if player_attack_evo:

                    if back_key:
                        x = run_Player.x - 2
                        y = run_Player.y + 14
                        if player_shot_attack_count <= 0:
                            pygame.mixer.Sound.play(shooting_sound)
                            player_shot_list_B.append(run_Player_Shot.create_player_shot(x, y))
                            player_shot_attack_count = 60
                    else:
                        x = run_Player.x + 50
                        y = run_Player.y + 14
                        if player_shot_attack_count <= 0:
                            pygame.mixer.Sound.play(shooting_sound)
                            player_shot_list_F.append(run_Player_Shot.create_player_shot(x, y))
                            player_shot_attack_count = 60

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_e:
                E = False

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
        if slow_count > 0:
            if not_stuned <= 0:
                if player_fin_evo:
                    if player_move_up:
                        run_Player.y -= .5
                    if player_move_down:
                        run_Player.y += .5
                if player_tail_evo:
                    if player_move_left:
                        run_Player.x -= 1
                    if player_move_right:
                        run_Player.x += .5
            if not_stuned <= 0:
                if not player_fin_evo:
                    if player_move_up:
                        run_Player.y -= .25
                    if player_move_down:
                        run_Player.y += .25
                if not player_tail_evo:
                    if player_move_left:
                        run_Player.x -= .5
                    if player_move_right:
                        run_Player.x += .25

        else:
            if not_stuned <= 0:
                if player_fin_evo:
                    if player_move_up:
                        run_Player.y -= 1.2
                    if player_move_down:
                        run_Player.y += 1.2
                if player_tail_evo:
                    if player_move_left:
                        run_Player.x -= 2.4
                    if player_move_right:
                        run_Player.x += 1.2
            if not_stuned <= 0:
                if not player_fin_evo:
                    if player_move_up:
                        run_Player.y -= .85
                    if player_move_down:
                        run_Player.y += .85
                if not player_tail_evo:
                    if player_move_left:
                        run_Player.x -= 1.7
                    if player_move_right:
                        run_Player.x += .85

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
            pygame.draw.rect(window, (0, 0, 0), [10, window_y - 31, 152, 17])

        if not player_health_evo:
            pygame.draw.rect(window, (0, 0, 0), [10, window_y - 31, 102, 17])

        pygame.draw.rect(window, (250, 11, 4), [11, window_y - 30, life_points * 2, 15])

        Score_Text2 = Score_Font.render('Score: ' + str(score_points), True, (255, 255, 255))
        window.blit(Score_Text2, (5, 5))

    if paused:

        window.fill("Black")

        window.blit(paused_img, (window_x // 2 - paused_img_W // 2, 50))

        window.blit(paused_menu_img, (window_x // 2 - paused_menu_img_W // 2, 450))

        Score_Text = Score_Font.render('Score: ' + str(score_points), True, (255, 255, 255))
        window.blit(Score_Text, (10, 35))

        Evo_Point_text = Score_Font.render('Evo Points: ' + str(evolution_points), True, (255, 255, 255))
        window.blit(Evo_Point_text, (10, 10))





        if evo_menu:

            window.fill("Black")

            window.blit(evo_img, (window_x // 2 - evo_img_W // 2, 50))

            window.blit(evo_menu_img, (window_x // 2 - evo_menu_img_W // 2, evo_menu_img_H - 200))

            Evo_Point_text1 = Score_Font.render('Evo Points: ' + str(evolution_points), True, (255, 255, 255))
            window.blit(Evo_Point_text1, (10, 10))

    if gameover:

        window.fill("Black")

        window.blit(gameover_img, (window_x // 2 - gameover_img_W // 2, 50))

        window.blit(gameover_menu_img, (window_x // 2 - gameover_menu_img_W // 2, gameover_menu_img_H + 200))

        Score_text = Score_Font.render('Final Score: ' + str(score_points), True, (255, 255, 255))
        window.blit(Score_text, (10, 10))

    if gamestart:

        window.fill("Black")

        paused = True

        window.blit(gamestart_img, (window_x//2 - gamestart_img_W//2, 50))

        window.blit(gamestart_menu_img, (window_x // 2 - gamestart_menu_img_W // 2, window_x//2 - gamestart_menu_img_H - 50))

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

    global food_list,poison_list,regular_blob_list,jumping_blob_list,fire_blob_list,electric_blob_list,electric_shot_list,player_shot_list_F,player_shot_list_B,barrier_list,moving_food_list

    if not paused:

        barrier_list = run_Barrier.move_barrier(barrier_list)
        run_Barrier.draw_barrier(barrier_list, window)

        if player_eye_evo:

            if back_key:
                run_Player.draw_reverse_eye(player_rotate_degree, window)
            else:
                run_Player.draw_forward_eye(player_rotate_degree, window)

        if player_tail_evo:

            if back_key:
                run_Player.draw_reverse_tail(player_rotate_degree, window)
            else:
                run_Player.draw_forward_tail(player_rotate_degree, window)

        if player_fin_evo:

            if back_key:
                run_Player.draw_reverse_fin(player_rotate_degree, window)
            else:
                run_Player.draw_forward_fin(player_rotate_degree, window)

        if player_tail_fin_evo:

            if back_key:
                run_Player.draw_reverse_tail_fin(player_rotate_degree, window)
            else:
                run_Player.draw_forward_tail_fin(player_rotate_degree, window)

        if player_attack_evo:

            if back_key:
                run_Player.draw_reverse_attack(player_rotate_degree, window)
            else:
                run_Player.draw_forward_attack(player_rotate_degree, window)

        if player_start_evo:

            if back_key:
                run_Player.draw_reverse_base(player_rotate_degree,window)
            else:
                run_Player.draw_forward_base(player_rotate_degree,window)

        player_shot_list_F = run_Player_Shot.move_player_shot_forward(player_shot_list_F)
        run_Player_Shot.draw_player_shot(player_shot_list_F, window)

        player_shot_list_B = run_Player_Shot.move_player_shot_backward(player_shot_list_B)
        run_Player_Shot.draw_player_shot(player_shot_list_B, window)

        # Enemys

        regular_blob_list = run_Regular_Blob.move_regular_blob(regular_blob_list)
        run_Regular_Blob.draw_regular_blob(regular_blob_list, window)

        jumping_blob_list = run_Jumping_Blob.move_jumping_blob(jumping_blob_list)
        run_Jumping_Blob.draw_jumping_blob(jumping_blob_list, window)

        fire_blob_list = run_Fire_Blob.move_fire_blob(fire_blob_list)
        run_Fire_Blob.draw_fire_blob(fire_blob_list, window)

        electric_blob_list = run_Electric_Blob.move_electric_blob(electric_blob_list)
        run_Electric_Blob.draw_electric_blob(electric_blob_list, window)

        electric_shot_list = run_Electric_Shot.move_electric_shot(electric_shot_list)
        run_Electric_Shot.draw_electric_shot(electric_shot_list, window)

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
        run_Poison.draw_poison(poison_list, window)

        food_list = run_Food.move_food(food_list)
        run_Food.draw_food(food_list, window)

        moving_food_list = run_Moving_food.move_moving_food(moving_food_list)
        run_Moving_food.draw_moving_food(moving_food_list, window)

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

    for i, j in enumerate(jumping_blob_list):
        jumping_blob_list.pop(i)

    for i, f in enumerate(food_list):
        food_list.pop(i)

    for i, m in enumerate(moving_food_list):
        moving_food_list.pop(i)

    for i, p in enumerate(poison_list):
        poison_list.pop(i)

    for i, b in enumerate(barrier_list):
        barrier_list.pop(i)

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
    t4 = threading.Thread(target=MovingBackground_Menus())
    t4.start()
    t5 = threading.Thread(target=reDrawGameWindow())
    t5.start()

    clock.tick(60)

    pygame.display.flip()

# Made by Mayhem X01