import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import ExcelWriter
from pandas import ExcelFile
import re

Data = pd.read_csv("canteen.csv", encoding = "ISO-8859-1")
df = DataFrame(Data, columns = ["Canteen", "Pixel", "Stall", "Cuisine", "Halal","Veg","Food","Price","Rating","Distance"])

def sort_price(df):
    sorted_price = df.sort_values("Price")
    return(sorted_price)
    
'''sort_price = sort_price(df)
print(sort_price)'''

def distance_a_b(A_x, A_y, B_x, B_y):
    distanceAB = round((((B_y-A_y)**2)+((B_x-A_x)**2))**(0.5)*1.65)
    return distanceAB

def sort_by_location(userLocX, userLocY, df):
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

    
    c1 = list(df[df["Canteen"] == "Food Court 1"].index)
    c2 = list(df[df["Canteen"] == "Food Court 2"].index)
    c3 = list(df[df["Canteen"] == "Food Court 9"].index)
    c4 = list(df[df["Canteen"] == "Food Court 11"].index)
    c5 = list(df[df["Canteen"] == "Food Court 13"].index)
    c6 = list(df[df["Canteen"] == "Food Court 14"].index)
    c7 = list(df[df["Canteen"] == "Food Court 16"].index)
    c8 = list(df[df["Canteen"] == "Ananda Kitchen"].index)
    c9 = list(df[df["Canteen"] == "Foodgle Food Court"].index)
    c10 = list(df[df["Canteen"] == "North Hill Food Court"].index)
    c11 = list(df[df["Canteen"] == "Pioneer Food Court"].index)
    c12 = list(df[df["Canteen"] == "Quad Cafe"].index)
    c13 = list(df[df["Canteen"] == "North Spine Plaza"].index)
    c14 = list(df[df["Canteen"] == "Koufu @ South Spine"].index)

    df.loc[c1, "Distance"] = canteens_distance["Food Court 1"]
    df.loc[c2, "Distance"] = canteens_distance["Food Court 2"]
    df.loc[c3, "Distance"] = canteens_distance["Food Court 9"]
    df.loc[c4, "Distance"] = canteens_distance["Food Court 11"]
    df.loc[c5, "Distance"] = canteens_distance["Food Court 13"]
    df.loc[c6, "Distance"] = canteens_distance["Food Court 14"]
    df.loc[c7, "Distance"] = canteens_distance["Food Court 16"]
    df.loc[c8, "Distance"] = canteens_distance["Ananda Kitchen"]
    df.loc[c9, "Distance"] = canteens_distance["Foodgle Food Court"]
    df.loc[c10, "Distance"] = canteens_distance["North Hill Food Court"]
    df.loc[c11, "Distance"] = canteens_distance["Pioneer Food Court"]
    df.loc[c12, "Distance"] = canteens_distance["Quad Cafe"]
    df.loc[c13, "Distance"] = canteens_distance["North Spine Plaza"]
    df.loc[c14, "Distance"] = canteens_distance["Koufu @ South Spine"]


    sorted_by_distance = df.sort_values("Distance", ascending = True)
    sorted_by_distance = sorted_by_distance.drop_duplicates(subset = ["Canteen"], keep = "first", inplace = False)
    return sorted_by_distance
                            
'''x = sort_by_location(200,200, df)
print(x)'''
   
   

    #sort from highest rank to lowest rank
def sort_by_rating(df):
    sorted_rating = df.sort_values("Rating", ascending = False)
    new_sorted = sorted_rating.drop_duplicates(subset = ["Canteen"], keep = "first", inplace = False)                                             
    return new_sorted


''''sort_by_rank = sort_by_rating(df)
print(sort_by_rank)'''


def filter_by_cuisine(user_input,df):
    x = df.Cuisine.str.contains(user_input, flags = re.IGNORECASE)
    return df[x]

'''cuisine = filter_by_cuisine("chinese",df)
print(cuisine)'''

def search_by_name(userInput,df):
    x = df.Food.str.contains(userInput, flags = re.IGNORECASE)
    best_match = df[x]        
    return best_match

'''bestmatch = search_by_name("chicken",df)
print(bestmatch.Food)'''
    
def veg_(df, vegOrNot):
    if vegOrNot:                    #veg options
        return df.loc[df.Veg == "Y"]
    elif not vegOrNot:                 #non veg options
        return df.loc[df.Veg == "N"]

'''veg = veg(df, True)
print(veg)'''


def halal_(df, halalOrNot):
    if halalOrNot:                  #halal options
        return df.loc[df.Halal == "Y"]
    elif not halalOrNot:               #non-halal options
        return df.loc[df.Halal == "N"]

'''halal = halal(df,True)
print(halal)'''

def top_results(df):
    no_of_rows = df.Food.count()
    df = df.reset_index(drop = True)
    print(no_of_rows)
    if df.Food.count()  <= 5:
        return df
    elif df.Food.count() > 5:
        sliced_df = df.head(n=5)
        return sliced_df

'''x = top_results(df)
print(x)'''

def df_to_dict(df):
    dict_set = df.T.to_dict()#.values()
    return dict_set
