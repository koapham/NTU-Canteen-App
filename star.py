import pygame, sys
from pygame.locals import *
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 99, 71)
grey = (200, 200, 200)

class star:
	def __init__(self, vertice_list, rate): #Vertice_list is the list of vertice of the first star
		self.vertice_list = vertice_list
		self.rate = rate

	def show_rate(self, image):
		if 2 < self.rate <= 2.33:
			pygame.draw.polygon(image, orange, self.no_star(1), 0)
			pygame.draw.polygon(image, orange, self.no_star(2), 0)
			pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(3), "color"), 0)
			pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(3), "blank"), 1)
			pygame.draw.polygon(image, orange, self.no_star(4), 1)
			pygame.draw.polygon(image, orange, self.no_star(5), 1)
		elif 2.33 < self.rate <= 2.66:
			pygame.draw.polygon(image, orange, self.no_star(1), 0)
			pygame.draw.polygon(image, orange, self.no_star(2), 0)
			pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(3), "color"), 0)
			pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(3), "blank"), 1)
			pygame.draw.polygon(image, orange, self.no_star(4), 1)
			pygame.draw.polygon(image, orange, self.no_star(5), 1)
		elif 2.66 < self.rate <= 3:
			pygame.draw.polygon(image, orange, self.no_star(1), 0)
			pygame.draw.polygon(image, orange, self.no_star(2), 0)
			pygame.draw.polygon(image, orange, self.no_star(3), 0)
			pygame.draw.polygon(image, orange, self.no_star(4), 1)
			pygame.draw.polygon(image, orange, self.no_star(5), 1)
		elif 3 < self.rate <= 3.33:
			pygame.draw.polygon(image, orange, self.no_star(1), 0)
			pygame.draw.polygon(image, orange, self.no_star(2), 0)
			pygame.draw.polygon(image, orange, self.no_star(3), 0)
			pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(4), "color"), 0)
			pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(4), "blank"), 1)
			pygame.draw.polygon(image, orange, self.no_star(5), 1)
		elif 3.33 < self.rate <= 3.66:
			pygame.draw.polygon(image, orange, self.no_star(1), 0)
			pygame.draw.polygon(image, orange, self.no_star(2), 0)
			pygame.draw.polygon(image, orange, self.no_star(3), 0)
			pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(4), "color"), 0)
			pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(4), "blank"), 1)
			pygame.draw.polygon(image, orange, self.no_star(5), 1)
		elif 3.66 < self.rate <= 4:
			pygame.draw.polygon(image, orange, self.no_star(1), 0)
			pygame.draw.polygon(image, orange, self.no_star(2), 0)
			pygame.draw.polygon(image, orange, self.no_star(3), 0)
			pygame.draw.polygon(image, orange, self.no_star(4), 0)
			pygame.draw.polygon(image, orange, self.no_star(5), 1)
		elif 4 < self.rate <= 4.33:
			pygame.draw.polygon(image, orange, self.no_star(1), 0)
			pygame.draw.polygon(image, orange, self.no_star(2), 0)
			pygame.draw.polygon(image, orange, self.no_star(3), 0)
			pygame.draw.polygon(image, orange, self.no_star(4), 0)
			pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(5), "color"), 0)
			pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(5), "blank"), 1)
		elif 4.33 < self.rate <= 4.66:
			pygame.draw.polygon(image, orange, self.no_star(1), 0)
			pygame.draw.polygon(image, orange, self.no_star(2), 0)
			pygame.draw.polygon(image, orange, self.no_star(3), 0)
			pygame.draw.polygon(image, orange, self.no_star(4), 0)
			pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(5), "color"), 0)
			pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(5), "blank"), 1)
		elif 4.66 < self.rate <= 5:
			pygame.draw.polygon(image, orange, self.no_star(1), 0)
			pygame.draw.polygon(image, orange, self.no_star(2), 0)
			pygame.draw.polygon(image, orange, self.no_star(3), 0)
			pygame.draw.polygon(image, orange, self.no_star(4), 0)
			pygame.draw.polygon(image, orange, self.no_star(5), 0)
			

	def no_star(self, num_star):
		new_list = []
		if num_star == 1:
			new_list = self.vertice_list
		elif num_star == 2:
			for i in range(10):
				x = self.vertice_list[i][0] + 40
				new_list.append((x, self.vertice_list[i][1]))
		elif num_star == 3:
			for i in range(10):
				x = self.vertice_list[i][0] + 80
				new_list.append((x, self.vertice_list[i][1]))
		elif num_star == 4:
			for i in range(10):
				x = self.vertice_list[i][0] + 120
				new_list.append((x, self.vertice_list[i][1]))
		elif num_star == 5:
			for i in range(10):
				x = self.vertice_list[i][0] + 160
				new_list.append((x, self.vertice_list[i][1]))
		return new_list

	def special_star(self, first_or_second, list_vertice, blank):
		if first_or_second == "first":
			if blank == "color":
				new_list = [list_vertice[7], list_vertice[8], list_vertice[9]]
			elif blank == "blank":
				new_list = [list_vertice[0], list_vertice[1], list_vertice[2], list_vertice[3], list_vertice[4], list_vertice[5], \
				list_vertice[6], list_vertice[7], list_vertice[9]]
		elif first_or_second == "second":
			if blank == "color":
				new_list = [list_vertice[0], list_vertice[1], list_vertice[5], list_vertice[6], list_vertice[7], list_vertice[8], \
				list_vertice[9]]
			elif blank == 'blank':
				new_list = [list_vertice[1], list_vertice[2], list_vertice[3], list_vertice[4], list_vertice[5]]
		return new_list

intial_list = [(13, 0),(18,10), (28, 11), (21, 18), (24, 28), (13, 23), (4, 28), (7, 18), (0, 11), (10, 10)]
win = pygame.display.set_mode((0,0), RESIZABLE)
#while True:
	#win.fill(white)
	#for event in pygame.event.get():
		#if event.type == pygame.QUIT:
			#pygame.quit()
			#sys.exit()
	#star(intial_list, 3.5).show_rate(win)
	#pygame.display.flip()
	#pygame.time.wait(40)




