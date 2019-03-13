min_price = 3
max_price = 7

#-----------store in fn file--------------------
def search_by_price(df,min_price,max_price):
    filter_max = df.loc[df.Price <= max_price]
    filter_min = filter_max.loc[filter_max.Price >= min_price]
    return filter_min
#--------------------------------------------------------
if min_price != 0 and max_price != 0 and food_name == 0 and cuisine == 0:
    filter_price = search_by_price(df,min_price,max_price)
    filter_veg = fn.veg_(filter_price,veg)
    filter_halal = fn.halal_(filter_veg, hal)

    sort_dist = fn.sort_by_location(200,200, filter_halal)
    top_dist = fn.top_results(sort_dist)
    top_dist_dict = fn.df_to_dict(top_dist)
    
    
    sort_price = fn.sort_price(filter_halal)
    top_price = fn.top_results(sort_price)
    top_price_dict = fn.df_to_dict(top_price)


    sort_rating = fn.sort_by_rating(filter_halal)
    top_rating = fn.top_results(sort_rating)
    top_rating_dict = fn.df_to_dict(top_rating)

print(top_dist_dict)
print(top_price_dict)
print(top_rating_dict)
    

