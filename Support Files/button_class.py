import pygame, sys
import pygame_textinput
import pandas as pd
from pygame.locals import *
import show_canteen
pygame.init()

#Color
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 99, 71)
grey = (200, 200, 200)



#Create a button class
class button():
    def __init__(button, text, location, action, background_color = black, text_color = white, size = (90, 30), font = 'comicsansms', font_size = 17):
        button.text = text
        button.background_color = background_color
        button.text_color = text_color
        button.color = background_color
        button.size = size
        button.font = pygame.font.SysFont(font, font_size)
        button.text_surf = button.font.render(button.text, 1, button.text_color)
        button.text_rect = button.text_surf.get_rect(center=[s//2 for s in button.size])
        button.surface = pygame.surface.Surface(size)
        button.rect = button.surface.get_rect(center = location)
        button.call_back_ = action
        
    def draw(button, win):
        button.background_color = button.color
        pos = pygame.mouse.get_pos()
        if button.rect.collidepoint(pos):
            button.background_color = grey
        button.surface.fill(button.background_color)
        button.surface.blit(button.text_surf, button.text_rect)
        win.blit(button.surface, button.rect)
        
        
    def call_back(button):
        button.call_back_()
    

#intial_list = [(65, 0),(90,50), (140, 55), (105, 90), (120, 140), (65, 115), (20, 140), (35, 90), (0, 55), (50, 50)]
#my_star = star.star(intial_list, 3.5)

