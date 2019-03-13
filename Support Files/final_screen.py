import pygame
from pygame.locals import *
from google_images_download import google_images_download
import pandas as pd
from pandas import DataFrame
import text_class

Data = pd.read_csv("canteen.csv", encoding = "ISO-8859-1")
df = DataFrame(Data, columns = ["Canteen","Food", "Stall", "Cuisine", "Halal","Veg","Price","Rating","Distance","Address","Phone","Opening"])

pygame.init()
display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 99, 71)
grey = (200, 200, 200)
win = pygame.display.set_mode((0,0),RESIZABLE)

pygame.display.update

#downloads image from google
def food_image(food_name):
        food_image = google_images_download.googleimagesdownload()
        arguments = {"keywords": food_name, "limit":1, #"usage_rights": "labeled-for-reuse",
                     "print_size" : True, "size":"icon", "format": "png", "image_directory": "<output_directory><image_directory><images>"}
        food_image_path = food_image.download(arguments)



user_input = "Ananda Kitchen"


#get corresponding info
def get_info(user_input):
    if type(user_input) == str:    #if user chooses cuisine
        info_df = df.loc[df.Canteen == user_input].head(1)
        return user_input, info_df.Distance, info_df.Address, info_df.Phone, info_df.Rating, info_df.Opening

    elif type(user_input) == list:      #if user chooses by name
        info_df = df.loc[df.Food == user_input[0]]
        info_df = info_df.loc[df.Distance == user_input[1]]
        info_df = info_df.loc[df.Price == user_input[2]]
        info_df = info_df.loc[df.Rating == user_input[3]]
        return user_input[0], info_df.Canteen, info_df.Distance , info_df.Price, info_df.Rating , info_df.Address, info_df.Phone, info_df.Opening

start = True   
while start:
    win.fill(white)
    get_info(user_input)

    font1 = pygame.font.SysFont("calibri", 20)
    font2 = pygame.font.SysFont("calibri", 50)
    
    if  type(user_input) == str:       
        canteen_name, distance, address, phone, rating,opening = get_info(user_input)
        canteen_name_ = text_class.text_class(user_input,((win.get_width()/2), 1700) )
        address_ = text_class.text_class("Address: " + str(address),((win.get_width()/2), 800) )
        distance_ = text_class.text_class("Distance: "+ str(distance),((win.get_width()/2),900) )  
        opening_ = text_class.text_class("Opening: " + str(opening),((win.get_width()/2),700) )
        ##rating = star.star

        canteen_name_.draw(win)
        address_.draw(win)
        distance_.draw(win)
        opening_.draw(win)
        
        download_image = food_image(canteen_name)
        print(download_image)
        thumbnail = pygame.image.load(download_image)
        print(thumbnail)
        win.blit(image,(500, 1000))

        
        #------------------------------------------------------------------------------

        '''print(type(canteen_name))
        textLine1 = font2.render(canteen_name, True, (0,0,0))
        textLine2 = font1.render(address.decode('utf-8', 'ignore'), True, (0,128,128))
        textLine3 = font1.render(.decode('utf-8', 'ignore'), True, (0,128,2))
        textLine4 = font1.render(unicode.decode('utf-8', 'ignore'), True, (128,0,128))

        W = 1280
        win.blit(textLine1, (((W-textLine1.get_width())/2),96))
        win.blit(textLine2, (((W-textLine2.get_width())/2),(96+48)))
        win.blit(textLine3, (((W-textLine3.get_width())/2),((H-textLine3.get_height())/2)))
        win.blit(textLine4, (((W-textLine4.get_width())/2),(512)))'''

        #---------------------------------------------------------------------------------

    elif type(user_input) == list:
        
        food_name, canteen_name, price, rating, address, phone, opening
        food_name_ = text_class.text_class(food_name,(300, 1000))
        canteen_name_ = text_class.text_class(canteen_name, (win.get_width/2,900))
        address_ = text_class.text_class("Address: " + str(address), (win.get_width/2, 800
        price_ = text_class.text_class("Price: " + str(price),(win.get_width/2,800) )
        distance_ = text_class.text_class("Distance from your location: " + str(distance),(win.get_width/2,900) ) 
        opening_ = text_class.text_class("Opening hours:" + str(opening),(win.get_width/2,700) )
        ##rating = star.star()

        
        food_name_.draw(win)
        canteen_name_.draw(win)
        price_.draw(win)
        address_.draw(win)
        distance_.draw(win)
        opening_.draw(win)
                                    
        
        thumbnail = pygame.image.load(food_image(food_name_))
        win.blit(image,(500, 1000))
        
    #Get_directions = pygbutton.PygButton()
                                             
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(pos):
                    button.call_back()
                    start = False
