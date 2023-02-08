import pygame

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