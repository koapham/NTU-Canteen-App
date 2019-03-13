import pygame, sys
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
blue = (0,10,255)
win = pygame.display.set_mode((0,0),RESIZABLE)

pygame.display.update

#downloads image from google
def food_image(food_name):
        food_image = google_images_download.googleimagesdownload()
        arguments = {"keywords": food_name, "limit":1, #"usage_rights": "labeled-for-reuse",
                     "print_size" : True, "size":"icon", "format": "png"}
        food_image_path = food_image.download(arguments)



user_input = ["Sweet Corn Veg Soup", 0, 3,3.5]


#get corresponding info
def get_info(user_input):
    if type(user_input) == str:
        info_df = df.loc[df.Canteen == user_input].head(1)
        canteen = user_input
        distance = str(info_df.loc[0,"Distance"])
        address = str(info_df.loc[0,"Address"])
        phone = str(info_df.loc[0,"Phone"])
        rating = str(info_df.loc[0,"Rating"])
        opening = str(info_df.loc[0, "Opening"])
        
        return canteen, distance, address, phone, rating, opening

    elif type(user_input) == list:
        info_df = df.loc[df.Food == user_input[0]]
        info_df = info_df.loc[df.Distance == user_input[1]]
        info_df = info_df.loc[df.Price == user_input[2]]
        info_df = info_df.loc[df.Rating == user_input[3]].head(1)
        
        food = user_input[0]
        canteen = info_df.loc[0,"Canteen"]
        price = str(format(info_df.loc[0,"Price"], ".2f"))
        distance = str(info_df.loc[0,"Distance"])
        address = str(info_df.loc[0,"Address"])
        phone = str(info_df.loc[0,"Phone"])
        rating = str(info_df.loc[0,"Rating"])
        opening = str(info_df.loc[0, "Opening"])
        
        
        return food, canteen, price, distance, address, phone, rating, opening
    

start = True   
while start:
    win.fill(white)
    get_info(user_input)

    font1 = pygame.font.SysFont("calibri", 20)
    font2 = pygame.font.SysFont("calibri", 50)
    
    if  type(user_input) == str:       
        canteen, distance, address, phone, rating, opening = get_info(user_input)
        canteen_s = font2.render(canteen, True, orange)
        address_t = font1.render("Address:", True, black)
        address_s = font1.render(address, True, blue)
        distance_t = font1.render("Distance from your location: ",True, black)
        distance_s = font1.render(distance + "m", True, blue)
        phone_t = font1.render("Tel no. ", True, black)
        phone_s = font1.render(phone, True, blue)
        opening_t = font1.render("Opening Hours: ", True, black)
        opening_s = font1.render(opening, True, blue)
        ##rating = star.star

        win.blit(canteen_s,(200,100))
        win.blit(address_t, (700,280))
        win.blit(address_s,(700,300))
        win.blit(distance_t, (700,360))
        win.blit(distance_s,(950,360))
        win.blit(phone_t,(700,420))
        win.blit(phone_s,(770,420))
        win.blit(opening_t,(700,460))
        win.blit(opening_s,(700,480))
        
        
        download_image = food_image(canteen_name)
        print(download_image)
        thumbnail = pygame.image.load(download_image)
        print(thumbnail)
        win.blit(image,(500, 1000))

        
    elif type(user_input) == list:

        food, canteen, price, distance, address, phone, rating, opening = get_info(user_input)
        food_s = font2.render(food, True, orange)
        canteen_t = font1.render("Canteen: ", True, black)
        canteen_s = font1.render(canteen, True, blue)
        price_t = font1.render("Price: ",True, black)
        price_s = font1.render("$" + price,True, blue)
        address_t = font1.render("Address:", True, black)
        address_s = font1.render(address, True, blue)
        distance_t = font1.render("Distance from your location: ",True, black)
        distance_s = font1.render(distance + "m", True, blue)
        phone_t = font1.render("Tel no. ", True, black)
        phone_s = font1.render(phone, True, blue)
        opening_t = font1.render("Opening Hours: ", True, black)
        opening_s = font1.render(opening, True, blue)
        ##rating = star.star()

        
        win.blit(food_s, (130,100))
        win.blit(canteen_t,(700,200))
        win.blit(canteen_s,(700,220))
        win.blit(price_t,(700,280))
        win.blit(price_s,(750,280))
        win.blit(address_t,(700,320))
        win.blit(address_s,(700,340))
        win.blit(distance_t,(700,390))
        win.blit(distance_s,(950,390))
        win.blit(phone_t, (700,440))
        win.blit(phone_s, (770, 440))
        win.blit(opening_t,(700,480))
        win.blit(opening_s,(700,500))
                                    
        
        '''thumbnail = pygame.image.load(food_image(food_name_))
        win.blit(image,(500, 1000))'''
        
    #Get_directions = pygbutton.PygButton()
                                             
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

