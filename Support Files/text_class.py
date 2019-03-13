import pygame, sys
from pygame.locals import *
pygame.init()


black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 99, 71)
grey = (200, 200, 200)

class text_class:
	def __init__(self, text, location, text_color = white, text_color_change = grey, font = 'calibri', font_size = 25):
		self.text = text
		self.location = location
		self.text_color = text_color
		self.text_color_change = text_color_change
		self.font = pygame.font.SysFont(font, font_size)
		#self.call_back_ = action
		self.text_rect_center = [s//2 for s in self.location]
		#self.image = image

	def draw(self, image):
		pos = pygame.mouse.get_pos()
		self.text_surf, self.text_rect = text_objects(self.text, self.font, self.text_color, self.text_rect_center)
		if self.text_rect.collidepoint(pos):
			self.text_surf, self.text_rect = text_objects(self.text, self.font, self.text_color_change, self.text_rect_center)
		else:
			self.text_surf, self.text_rect = text_objects(self.text, self.font, self.text_color, self.text_rect_center)
		image.blit(self.text_surf, self.text_rect)


	def call_back(self):
		self.call_back_()



def text_objects(text, font, color, text_rect_center):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect(center = text_rect_center)

def mousebuttondown():
	pos = pygame.mouse.get_pos()
	if text.text_rect.collidepoint(pos):
		text.call_back()

