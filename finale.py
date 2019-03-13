import sys, os
import time
import pygame, pygbutton
import pygame, sys
from pygame.locals import *
import text_class
import pygame_textinput
import button_class
import show_canteen_class
import fn
import pandas as pd
from pandas import DataFrame
#import abhi
import re


W = 1280
H = 720
FPS = 60
FPSCLOCK = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 99, 71)
blue = (0,191,255)
grey = (200, 200, 200)

win = pygame.display.set_mode((0,0), RESIZABLE)
textinput = pygame_textinput.TextInput(font_size = 25)

Data = pd.read_csv("canteen.csv", encoding = "ISO-8859-1")
df = DataFrame(Data, columns = ["Canteen", "Pixel", "Stall", "Cuisine", "Halal","Veg","Food","Price","Rating","Distance"])

def official_show_canteen():

	hal = False
	veg = False
	cuisine = 0
	food_name = 0

	#Welcome screen
	win.fill((250,255,255))
	font1 = pygame.font.SysFont("calibri", 48)
	font2 = pygame.font.SysFont("calibri", 96)

	line1 = "Food & Beverage (F&B) Recommendation System for NTU"
	line2 = "By Abhinandan, Khoa, & Reena (CS Year 1, SCSE)"
	line3 = "Welcome!"
	line4 = "To start, please click on \"View Map of NTU\" below:"

	textLine1 = font1.render(line1, True, (0,0,128))
	textLine2 = font1.render(line2, True, (0,128,128))
	textLine3 = font2.render(line3, True, (0,0,0))
	textLine4 = font1.render(line4, True, (128,0,128))

	win.blit(textLine1, (((W-textLine1.get_width())/2),96))
	win.blit(textLine2, (((W-textLine2.get_width())/2),(96+48)))
	win.blit(textLine3, (((W-textLine3.get_width())/2),((H-textLine3.get_height())/2)))
	win.blit(textLine4, (((W-textLine4.get_width())/2),(512)))

	pygame.display.flip()

	# VIEW MAP & CLOSE BUTTON
	viewMapButton = pygbutton.PygButton((((W-240)/2), ((H-120)), 240, 60 ), 'View Map of NTU')
	closeButton = pygbutton.PygButton(((W-150), ((H-60)), 100, 30 ), 'Close')

	#(IGNORE) pygame.display.flip()

	viewMap = False
	while viewMap == False:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or ('click' in closeButton.handleEvent(event)):
	            pygame.quit()
	            sys.exit()
	        
	        if 'click' in viewMapButton.handleEvent(event):
	            viewMap = True

	        viewMapButton.draw(win)
	        closeButton.draw(win)
	        pygame.display.update()
	        FPSCLOCK.tick(FPS)

	#Map Screen
	locationEntered = False

	while locationEntered == False:

	    loadMapScreen()
	    updateLoc = False
	    userLocX, userLocY = get_user_location()
	    sort_distance(userLocX, userLocY)

	    font = pygame.font.SysFont("calibri", 20)
	    line1 = "To continue, click on one of the"
	    line2 = "three buttons given below."

	    textLine1 = font.render(line1, True, (0,0,128))
	    textLine2 = font.render(line2, True, (0,0,128))

	    win.blit(textLine1, (10,400))
	    win.blit(textLine2, (10,420))
	    
	    #locationEntered = True

	    # UPDATE LOCATION & CLOSE BUTTON
	    updateLocButton = pygbutton.PygButton((10, 460, 250, 40 ), 'Update Location')
	    setFoodPreferencesButton = pygbutton.PygButton((10, 510, 250, 40 ), 'Set Food Preferences')
	    closeButton = pygbutton.PygButton((10, (H-80), 250, 40 ), 'Close')

	    while updateLoc == False:
	       for event in pygame.event.get():
	           if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or ('click' in closeButton.handleEvent(event)):
	               closeButton.draw(win)
	               pygame.display.update()
	               FPSCLOCK.tick(FPS)
	               pygame.quit()
	               sys.exit()
	           
	           elif 'click' in updateLocButton.handleEvent(event):
	               updateLoc = True
	               #locationEntered = False
	               updateLocButton.draw(win)
	               pygame.display.update()
	               FPSCLOCK.tick(FPS)
	               #loadMapScreen()
	               break

	           elif 'click' in setFoodPreferencesButton.handleEvent(event):
	              updateLoc = False
	              locationEntered = True
	              setFoodPreferencesButton.draw(win)
	              pygame.display.update()
	              FPSCLOCK.tick(FPS)                
	              break
	           
	           updateLocButton.draw(win)
	           setFoodPreferencesButton.draw(win)
	           closeButton.draw(win)
	           pygame.display.update()
	           FPSCLOCK.tick(FPS)                

	scence = pygame.image.load('heeee.png')
	japan = pygame.image.load('japan.png')
	india = pygame.image.load('india.png')
	vietnam = pygame.image.load('vietnam.png')
	drink = pygame.image.load('drink.png')
	malay = pygame.image.load('malay.png')
	china = pygame.image.load('china.png')
	bakery = pygame.image.load('bakery.png')
	italy = pygame.image.load('italy.png')
	america = pygame.image.load('america.png')
	korea = pygame.image.load('korea.png')
	dessert = pygame.image.load('dessert.png')
	other = pygame.image.load('other.png') 

	ntu = pygame.image.load('ntu.jpg')
	house = pygame.image.load('house.png')

	japanese_c_1 = pygame.image.load('japanese_c.png')
	japanese_c_2 = pygame.image.load('japanese_c.png')
	japanese_c_3 = pygame.image.load('japanese_c.png')
	indian_c_1 = pygame.image.load('idian_c.png')
	indian_c_2 = pygame.image.load('idian_c.png')
	indian_c_3 = pygame.image.load('idian_c.png')
	vietnamese_c_1 = pygame.image.load('vietnamese_c.png')
	vietnamese_c_2 = pygame.image.load('vietnamese_c.png')
	vietnamese_c_3 = pygame.image.load('vietnamese_c.png')
	drink_c_1 = pygame.image.load('drink_c.png')
	drink_c_2= pygame.image.load('drink_c.png')
	drink_c_3 = pygame.image.load('drink_c.png')
	malaysian_c_1 = pygame.image.load('malaysian_c.png')
	malaysian_c_2 = pygame.image.load('malaysian_c.png')
	malaysian_c_3 = pygame.image.load('malaysian_c.png')
	chinese_c_1 = pygame.image.load('chinese_c.png')
	chinese_c_2 = pygame.image.load('chinese_c.png')
	chinese_c_3 = pygame.image.load('chinese_c.png')
	bakery_c_1 = pygame.image.load('bakery_c.png')
	bakery_c_2 = pygame.image.load('bakery_c.png')
	bakery_c_3 = pygame.image.load('bakery_c.png')
	western_c_1 = pygame.image.load('italian_c.png')
	western_c_2 = pygame.image.load('italian_c.png')
	western_c_3 = pygame.image.load('italian_c.png')
	american_c_1 = pygame.image.load('american_c.png')
	american_c_2 = pygame.image.load('american_c.png')
	american_c_3 = pygame.image.load('american_c.png')
	korean_c_1 = pygame.image.load('korean_c.png')
	korean_c_2 = pygame.image.load('korean_c.png')
	korean_c_3 = pygame.image.load('korean_c.png')
	dessert_c_1 = pygame.image.load('dessert_c.png')
	dessert_c_2 = pygame.image.load('dessert_c.png')
	dessert_c_3 = pygame.image.load('dessert_c.png')
	other_c_1 = pygame.image.load('other_c.png')
	other_c_2 = pygame.image.load('other_c.png')
	other_c_3 = pygame.image.load('other_c.png')
	text_c_1 = pygame.image.load('text_input_c.png')
	text_c_2 = pygame.image.load('text_input_c.png')
	text_c_3 = pygame.image.load('text_input_c.png')

	button1 = button_class.button(win,"Korean", (80, 290))
	button2 = button_class.button(win,"Indian", (205, 290))
	button3 = button_class.button(win,"Drink", (317, 290))
	button4 = button_class.button(win,"Dessert", (420, 290))
	button5 = button_class.button(win,"Vietnamese", (65, 390))
	button6 = button_class.button(win,"Malaysian", (190, 390))
	button7 = button_class.button(win,"Western", (312, 390))
	button8 = button_class.button(win,"American", (437, 390))
	button9 = button_class.button(win,"Bakery", (65, 460))
	button10 = button_class.button(win,"Japanese", (190, 460))
	button11 = button_class.button(win,"Chinese", (313, 460))
	button12 = button_class.button(win,"Others", (437, 460))
	button13 = button_class.button(win,"Search", (407, 135), background_color = orange, text_color = white, size = (80, 35.8))
	button14 = button_class.button(win,"Are you a Halal?", (120, 550), size = (150, 30), background_color = blue)
	button15 = button_class.button(win,"Are you a Vegeterian?", (330, 550), size = (180, 30), background_color = blue)
	#button16 = button_class.button(win,"Submit", (407, 620), None, background_color = orange, text_color = white)
	buttons_all = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15]
	#buttons_not_all = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button14, button15]
	click_1, click_2, click_3, click_4, click_5, click_6, click_7, click_8, click_9, click_10, click_11, click_12, click_13, click_14, click_15 = False, False, False,\
	False, False, False, False,False, False, False, False,False, False, False, False

	begin = True
	while begin == True:
		submit = pygbutton.PygButton((380, 620, 100, 40), 'Submit')
		win.fill(white)
		win.blit(scence, (0, 0))
		win.blit(korea, (19, 233))
		win.blit(india, (143, 240))
		win.blit(bakery, (5, 427))
		win.blit(vietnam, (5, 333))
		win.blit(malay, (129, 333))
		win.blit(italy, (252, 333))
		win.blit(america, (375, 333))
		win.blit(drink, (267, 230))
		win.blit(japan, (129, 418))
		win.blit(china, (253, 416))
		win.blit(other, (376, 417))
		win.blit(dessert,(371, 230))
		win.blit(ntu, (500, 0))
		events = pygame.event.get()
		for event in events:
			if 'down' in submit.handleEvent(event):
				begin = False
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for button in buttons_all:
					if button.rect.collidepoint(pos):
						if button == button1:
							cuisine_1 = korean_c_1
							cuisine_2 = korean_c_2
							cuisine_3 = korean_c_3
							cuisine = "korean"
							click_1 = True
						elif button == button2:
							cuisine_1 = indian_c_1
							cuisine_2 = indian_c_2
							cuisine_3 = indian_c_3
							cuisine = "indian"
							click_2 = True
						elif button == button3:
							cuisine_1 = drink_c_1
							cuisine_2 = drink_c_2
							cuisine_3 = drink_c_3
							cuisine = "drink"
							click_3 = True
						elif button == button4:
							cuisine_1 = dessert_c_1
							cuisine_2 = dessert_c_2
							cuisine_3 = dessert_c_3
							cuisine = "dessert"
							click_4 = True
						elif button == button5:
							cuisine_1 = vietnamese_c_1
							cuisine_2 = vietnamese_c_2
							cuisine_3 = vietnamese_c_3
							cuisine = "vietnamese"
							click_5 = True
						elif button == button6:
							cuisine_1 = malaysian_c_1
							cuisine_2 = malaysian_c_2
							cuisine_3 = malaysian_c_3
							cuisine = "malaysian"
							click_6 = True
						elif button == button7:
							cuisine_1 = western_c_1
							cuisine_2 = western_c_2
							cuisine_3 = western_c_3
							cuisine= "western"
							click_7 = True
						elif button == button8:
							cuisine_1 = american_c_1
							cuisine_2 = american_c_2
							cuisine_3 = american_c_3
							cuisine = "american"
							click_8 = True
						elif button == button9:
							cuisine_1 = bakery_c_1
							cuisine_2 = bakery_c_2
							cuisine_3 = bakery_c_3
							cuisine = "bakery"
							click_9 = True
						elif button == button10:
							cuisine_1 = japanese_c_1
							cuisine_2 = japanese_c_2
							cuisine_3 = japanese_c_3
							cuisine = "japanese"
							click_10 = True
						elif button == button11:
							cuisine_1 = chinese_c_1
							cuisine_2 = chinese_c_2
							cuisine_3 = chinese_c_3
							cuisine = "chinese"
							click_11 = True
						elif button == button12:
							cuisine_1 = other_c_1
							cuisine_2 = other_c_2
							cuisine_3 = other_c_3
							cuisine = "taiwanese"
							click_12 = True
						elif button == button13:
							cuisine_1 = text_c_1
							cuisine_2 = text_c_2
							cuisine_3 = text_c_3
							food_name = textinput.input_string
							click_13 = True
						elif button == button14:
							hal = True
							click_14 = True
						elif button == button15:
							veg = True
							click_15 = True

		click = [click_1, click_2, click_3, click_4, click_5, click_6, click_7, click_8, click_9, click_10, click_11, click_12, click_13, click_14, click_15]
		textinput.update(events)
		win.blit(textinput.get_surface(), (80, 126))
		submit.draw(win)
		for i in range(15):
			buttons_all[i].draw(click[i])
		pygame.display.update()
		pygame.time.wait(40)

	#global top_rating_dict, top_price_dict, top_dist_dict

	top_rating_dict, top_dist_dict, top_price_dict, top_rating_dict_1, top_dist_dict_1, top_price_dict_1 = {}, {}, {}, {}, {}, {}

	if cuisine != 0 and food_name == 0:
	    filter_cuisine = fn.filter_by_cuisine(cuisine,df)
	    filter_veg = fn.veg_(filter_cuisine, veg)
	    filter_halal = fn.halal_(filter_veg,hal)

	    sort_dist = fn.sort_by_location(userLocX,userLocY, filter_halal)
	    top_dist = fn.top_results(sort_dist)
	    top_dist_dict = fn.df_to_dict(top_dist)
	    
	    
	    sort_price = fn.sort_price(filter_halal)
	    top_price = fn.top_results(sort_price)
	    top_price_dict = fn.df_to_dict(top_price)

	    sort_rating = fn.sort_by_rating(filter_halal)
	    top_rating = fn.top_results(sort_rating)
	    top_rating_dict = fn.df_to_dict(top_rating)
	    
	if food_name != 0 and cuisine == 0:
		#underscore number 1 to mark the food insert
	    filter_name_1 = fn.search_by_name(food_name,df)
	    filter_veg_1 = fn.veg_(filter_name_1, veg)
	    filter_halal_1 = fn.halal_(filter_veg_1,hal)

	    sort_dist_1 = fn.sort_by_location(userLocX,userLocY, filter_halal_1)
	    top_dist_1 = fn.top_results(sort_dist_1)
	    top_dist_dict_1 = fn.df_to_dict(top_dist_1)
	    
	    
	    sort_price_1 = fn.sort_price(filter_halal_1)
	    top_price_1 = fn.top_results(sort_price_1)
	    top_price_dict_1 = fn.df_to_dict(top_price_1)


	    sort_rating_1 = fn.sort_by_rating(filter_halal_1)
	    top_rating_1 = fn.top_results(sort_rating_1)
	    top_rating_dict_1= fn.df_to_dict(top_rating_1)


	my_rank_dict = []
	my_distance_dict = []
	my_price_dict = []

	my_rank_dict_1 = []
	my_distance_dict_1 = []
	my_price_dict_1 = []

	#This is for the cuisine
	for i in top_rating_dict:
		my_rank_dict.append(top_rating_dict.get(i))
	for i in top_dist_dict:
		my_distance_dict.append(top_dist_dict.get(i))
	for i in top_price_dict:
		my_price_dict.append(top_price_dict.get(i))

	#This is for the food insert	
	for i in top_rating_dict_1:
		my_rank_dict_1.append(top_rating_dict_1.get(i))
	for i in top_dist_dict_1:
		my_distance_dict_1.append(top_dist_dict_1.get(i))
	for i in top_price_dict_1:
		my_price_dict_1.append(top_price_dict_1.get(i))

	most_suitable_canteen = pygbutton.PygButton((400, 20, 210, 40), 'Highest Rank Canteen')
	nearest_canteen = pygbutton.PygButton((780, 20, 200, 40), 'Nearest Canteen')
	cheapest_canteen = pygbutton.PygButton((1120, 20, 200, 40), 'Cheapest Canteen')

	my_rank_show = show_canteen_class.show_canteen_class_cuisine(my_rank_dict, cuisine_1, house)
	my_price_show = show_canteen_class.show_canteen_class_cuisine(my_price_dict, cuisine_3, house)
	my_distance_show = show_canteen_class.show_canteen_class_cuisine(my_distance_dict, cuisine_2, house)

	my_rank_show_1 = show_canteen_class.show_canteen_class_foodname(my_rank_dict_1, cuisine_1, house)
	my_price_show_1 = show_canteen_class.show_canteen_class_foodname(my_price_dict_1, cuisine_3, house)
	my_distance_show_1 = show_canteen_class.show_canteen_class_foodname(my_distance_dict_1, cuisine_2, house)
	
	first = True
	while first:
		win.fill(white)
		win.blit(cuisine_1, (0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if 'down' in most_suitable_canteen.handleEvent(event):
					most_suitable_canteen.draw(cuisine_1)
					first = False
		most_suitable_canteen.draw(cuisine_1)
		nearest_canteen.draw(cuisine_1)
		cheapest_canteen.draw(cuisine_1)
		pygame.display.flip()
		pygame.time.wait(40)


	rank_canteen = True
	while rank_canteen:
		win.fill(white)
		win.blit(cuisine_1, (0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if 'down' in nearest_canteen.handleEvent(event):
					nearest_canteen.draw(cuisine_1)
					rank_canteen = False
		if my_rank_dict != []:
			my_rank_show.draw()
		if my_rank_dict_1 != []:
			my_rank_show_1.draw()
		most_suitable_canteen.draw(cuisine_1)
		nearest_canteen.draw(cuisine_1)
		cheapest_canteen.draw(cuisine_1)
		pygame.display.flip()
		pygame.time.wait(40)	


	distance_canteen = True
	while distance_canteen:
		win.fill(white)
		win.blit(cuisine_2, (0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if 'down' in cheapest_canteen.handleEvent(event):
					cheapest_canteen.draw(win)
					distance_canteen = False
		if my_distance_dict != []:
			my_distance_show.draw()
		if my_distance_dict_1 != []:
			my_distance_show_1.draw()
		most_suitable_canteen.draw(cuisine_2)
		nearest_canteen.draw(cuisine_2)
		cheapest_canteen.draw(cuisine_2)
		pygame.display.flip()
		pygame.time.wait(40)


	price_canteen = True
	while price_canteen:
		win.fill(white)
		win.blit(cuisine_3, (0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
		if my_price_dict != []:
			my_price_show.draw()
		if my_price_dict_1 != []:
			my_price_show_1.draw()
		most_suitable_canteen.draw(cuisine_3)
		nearest_canteen.draw(cuisine_3)
		cheapest_canteen.draw(cuisine_3)
		pygame.display.flip()
		pygame.time.wait(40)

  
def loadMapScreen():

   # read image file and rescale it to the window size
   screenIm = pygame.image.load('Map1WithInfoTab5.png')
   screenIm = pygame.transform.scale(screenIm, (W , H))

   # add the image over the screen object
   win.blit(screenIm,(0, 0))   

   font = pygame.font.SysFont("calibri", 20)
   
   line1 = "The screen to the right shows"
   line2 = "the map of NTU."
   line3 = "Please click where you are on"
   line4 = "the map to enter your location."

   textLine1 = font.render(line1, True, (0,0,128))
   textLine2 = font.render(line2, True, (0,0,128))
   textLine3 = font.render(line3, True, (0,0,128))
   textLine4 = font.render(line4, True, (0,0,128))

   win.blit(textLine1, (10,60))
   win.blit(textLine2, (10,80))
   win.blit(textLine3, (10,120))
   win.blit(textLine4, (10,140)) 

   # update the contents of the entire display window
   pygame.display.flip()
   

def MouseClick():
   finish = False
   while finish == False:
   ## pygame.event.get() retrieves all events made by user
      for event in pygame.event.get():
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): #or ('click' in closeButton.handleEvent(event)):
            pygame.quit()
            sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            finish = True
         #closeButton.draw(screen)
         #pygame.display.update()
         #FPSCLOCK.tick(FPS)
         
   return (mouseX, mouseY)


def get_user_location():
  userLocX, userLocY = (0,0)
  while True:
    userLocX, userLocY = MouseClick()
    if userLocX > 260:
      break  
  font = pygame.font.SysFont("calibri", 20)
  userLocLine1 = "Your coordinates: "
  userLocLine2 = "X: " + str(userLocX) + ", Y: " + str(userLocY)
  textUserLocLine1 = font.render(userLocLine1, True, (0,0,128))
  textUserLocLine2 = font.render(userLocLine2, True, (0,128,128))
  win.blit(textUserLocLine1, (10,180))
  win.blit(textUserLocLine2, (11,200))
  pygame.display.flip()
  return (userLocX, userLocY)

   # update the contents of the entire display window to now display user coordinates


def distance_a_b(A_x, A_y, B_x, B_y):
   distanceAB = round((((B_y-A_y)**2)+((B_x-A_x)**2))**(0.5)*1.65)
   return distanceAB


def sort_distance(userLocX, userLocY):
   canteens_x = {'Food Court 1':831, 'Food Court 2':882, 'Food Court 9':1046, 'Food Court 11':1189, 'Food Court 13':834,
                'Food Court 14':932, 'Food Court 16':776, 'Ananda Kitchen':1201, 'Foodgle Food Court': 1127,
                'North Hill Food Court':1226, 'Pioneer Food Court':912, 'Quad Cafe':486, 'North Spine Plaza':583,
                'Koufu @ South Spine':511}

   canteens_y = {'Food Court 1':522, 'Food Court 2':435, 'Food Court 9':271, 'Food Court 11':210, 'Food Court 13':121,
                'Food Court 14':128, 'Food Court 16':181, 'Ananda Kitchen':289, 'Foodgle Food Court': 150,
                'North Hill Food Court':338, 'Pioneer Food Court':642, 'Quad Cafe':340, 'North Spine Plaza':279,
                'Koufu @ South Spine':554}

   canteens_distance = {}
 
   for key_x in canteens_x:
      canteens_distance[key_x] = distance_a_b(userLocX, userLocY, canteens_x[key_x], canteens_y[key_x])

   print(canteens_distance)

   canteenListByDistance = []
   canteenSortedDistanceList = []
   
   while len(canteens_distance) > 0:
      for key in canteens_distance:
         if canteens_distance[key] == min(canteens_distance.values()):
            canteenListByDistance.append(key)
            canteenSortedDistanceList.append(canteens_distance[key])
            del canteens_distance[key]
            break

   print(canteenListByDistance)
   print(canteenSortedDistanceList)

   font = pygame.font.SysFont("calibri", 20)

   CanteenDistLine1 = "Top 5 canteens by Distance:"
   textCanteenDistLine1 = font.render(CanteenDistLine1, True, (0,0,128))
   win.blit(textCanteenDistLine1, (10,240))
   
   for i in range(1,6):
      win.blit((font.render((str(i) + ". " + str(canteenListByDistance[i-1]) + " (" + str(canteenSortedDistanceList[i-1]) + "m)"), True, (50*(i-1), 0, 255-(50*i)))), (10, (260+20*i)))
   
   pygame.display.flip()   


def main():
  pygame.init()
  official_show_canteen()


#---------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()			

