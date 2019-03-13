import pygame, sys
from pygame.locals import *
import text_class
import star


pygame.init()


black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 99, 71)
grey = (200, 200, 200)

class show_canteen:
	def __init__(self, list_canteen_sorted, image, house):
		self.list_canteen_sorted = list_canteen_sorted
		self.number_canteen = len(self.list_canteen_sorted)
		self.image = image
		self.canteen_1 = []
		self.canteen_2 = []
		self.canteen_3 = []
		self.canteen_4 = []
		self.canteen_5 = []
		self.house = house
		self.house_1 = self.house.get_rect(center = (376, 200))
		self.house_2 = self.house.get_rect(center = (376, 300))
		self.house_3 = self.house.get_rect(center = (376, 400))
		self.house_4 = self.house.get_rect(center = (376, 500))
		self.house_5 = self.house.get_rect(center = (376, 600))


	def draw(self):
		canteen_1_list = [(1155, 195),(1160, 205), (1170, 206), (1163, 213), (1166, 223), (1155, 218), (1146, 223), (1149, 213), (1142, 206), (1152, 205)]
		canteen_2_list = [(1155, 295),(1160, 305), (1170, 306), (1163, 313), (1166, 323), (1155, 318), (1146, 323), (1149, 313), (1142, 306), (1152, 305)]
		canteen_3_list = [(1155, 395),(1160, 405), (1170, 406), (1163, 413), (1166, 423), (1155, 418), (1146, 423), (1149, 413), (1142, 406), (1152, 405)]
		canteen_4_list = [(1155, 495),(1160, 505), (1170, 506), (1163, 513), (1166, 523), (1155, 518), (1146, 523), (1149, 513), (1142, 506), (1152, 505)]
		canteen_5_list = [(1155, 595),(1160, 605), (1170, 606), (1163, 613), (1166, 623), (1155, 618), (1146, 623), (1149, 613), (1142, 606), (1152, 605)]
		for i in range(self.number_canteen):
			if i == 0:
				self.canteen_1.append(self.list_canteen_sorted[0])
			elif i == 1:
				self.canteen_2.append(self.list_canteen_sorted[1])
			elif i == 2:
				self.canteen_3.append(self.list_canteen_sorted[2])
			elif i == 3:
				self.canteen_4.append(self.list_canteen_sorted[3])
			elif i == 4:
				self.canteen_5.append(self.list_canteen_sorted[4])
		if self.canteen_1 != []:
			self.image.blit(self.house, (340, 170))
			self.message_display(self.canteen_1[0]['canteen'], (550, 213))
			self.message_display(self.canteen_1[0]['distance'], (800, 213))
			self.message_display(self.canteen_1[0]['price'], (1035, 213))
			star.star(canteen_1_list, self.canteen_1[0]['rate']).show_rate(self.image)
		if self.canteen_2 != []:
			self.image.blit(self.house, (340, 270))
			self.message_display(self.canteen_2[0]['canteen'], (550, 313))
			self.message_display(self.canteen_2[0]['distance'], (800, 313))
			self.message_display(self.canteen_2[0]['price'], (1035, 313))
			star.star(canteen_2_list, self.canteen_2[0]['rate']).show_rate(self.image)
		if self.canteen_3 != []:
			self.image.blit(self.house, (340, 370))
			self.message_display(self.canteen_3[0]['canteen'], (550, 413))
			self.message_display(self.canteen_3[0]['distance'], (800, 413))
			self.message_display(self.canteen_3[0]['price'], (1035, 413))
			star.star(canteen_3_list, self.canteen_3[0]['rate']).show_rate(self.image)
		if self.canteen_4 != []:
			self.image.blit(house, (340, 470))
			self.message_display(self.canteen_4[0]['canteen'], (550, 513))
			self.message_display(self.canteen_4[0]['distance'], (800, 513))
			self.message_display(self.canteen_4[0]['price'], (1035, 513))
			star.star(canteen_4_list, self.canteen_4[0]['rate']).show_rate(self.image)
		if self.canteen_5 != []:
			self.image.blit(self.house, (340, 570))
			self.message_display(self.canteen_5[0]['canteen'], (550, 613))
			self.message_display(self.canteen_5[0]['distance'], (800, 613))
			self.message_display(self.canteen_5[0]['price'], (1035, 613))
			star.star(canteen_5_list, self.canteen_5[0]['rate']).show_rate(self.image)		
		pos = pygame.mouse.get_pos()
		if self.house_1.collidepoint(pos):
			pygame.draw.polygon(self.image, black, [(340, 228), (410, 228)], 1)
		elif self.house_2.collidepoint(pos):
			pygame.draw.polygon(self.image, black, [(340, 328), (410, 328)], 1)
		elif self.house_3.collidepoint(pos):
			pygame.draw.polygon(self.image, black, [(340, 428), (410, 428)], 1)
		elif self.house_4.collidepoint(pos):
			pygame.draw.polygon(self.image, black, [(340, 528), (410, 528)], 1)
		elif self.house_5.collidepoint(pos):
			pygame.draw.polygon(self.image, black, [(340, 628), (410, 628)], 1)

	def message_display(self, text, text_center):
		largeText = pygame.font.SysFont('comicsansms',30) 
		TextSurf, TextRect = text_objects(text, largeText, black)
		TextRect.center = text_center
		self.image.blit(TextSurf, TextRect)

				
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def mousebuttondown():
	pos = pygame.mouse.get_pos()
	if my_show.house_1.collidepoint(pos):
		print(my_show.canteen_1[0])
	elif my_show.house_2.collidepoint(pos):
		print(my_show.canteen_2[0])
	elif my_show.house_3.collidepoint(pos):
		print(my_show.canteen_3[0])
	elif my_show.house_4.collidepoint(pos):
		print(my_show.canteen_4[0])
	elif my_show.house_5.collidepoint(pos):
		print(my_show.canteen_5[0])
		
house = pygame.image.load('house.png')
my_dict = [{"canteen": "North Spine Plaza", "distance": "250m", "price": "4.0", "rate": 3.7}, \
{"canteen": "Hall 12", "distance": "700m", "price": "4.5", "rate": 3.2}, \
{"canteen": "Koufu", "distance": "1003m", "price": "3.7", "rate": 4.5}]

def my_function():
	print("yay")

win = pygame.display.set_mode((0,0), RESIZABLE)
korea = pygame.image.load('korean_c.png')
most_suitable_canteen = text_class.text_class("Most suitable Canteen", (1070, 100), my_function, korea)
nearest_canteen = text_class.text_class("Nearest Canteen", (1770, 100), my_function, korea)
cheapest_canteen = text_class.text_class("Cheapest Canteen", (2450, 100), my_function, korea)
house = pygame.image.load('house.png')
my_show = show_canteen(my_dict, korea, house)


# while True:
# 	win.fill(white)
# 	win.blit(korea, (0,0))
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()
# 		elif event.type == pygame.MOUSEBUTTONDOWN:
# 			mousebuttondown()
# 	my_show.draw()
# 	most_suitable_canteen.draw()
# 	nearest_canteen.draw()
# 	cheapest_canteen.draw()
# 	pygame.display.flip()
# 	pygame.time.wait(40)

  





