import pygame

pygame.init()
pygame.mixer.music.load('ex21.mp3.mpeg')
pygame.mixer.music.play()
pygame.event.wait()