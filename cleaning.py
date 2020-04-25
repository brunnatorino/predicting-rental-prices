## DATA FORMATTING 
## initializing lists and variables
count = 0
house_price = []
rental_agency = []
location = []
city = []
bedrooms = []
surface = []
## how long we are running the while loop for 
n = int(len(houses)) - 1

while count <= n:
    # running the loop through each html bin we scraped
    num = houses[int(count)]
    
    # getting the price: make sure to test this code a few times by itself to understand exactly which parameters will work 
    price = num.find_all('span',{"class":"listing-search-item__price"})[0].text
    house_price.append(price)
    df_price = pd.DataFrame({'house_price':house_price})
    df_price['house_price'] = df_price['house_price'].str.replace("\D","")
    df_price['house_price'] = df_price['house_price'].str.replace("per month","")
    
    # if you have a variable that is not present on all ads the ads, you can use try and except to avoid stopping the loop
    try:
        agency = num.find_all('a', href=True)[2].text
    except IndexError:
        agency = 'none'
    rental_agency.append(agency)
    df_agency = pd.DataFrame({'rental_agency':rental_agency})
    
   #getting the postcode: make sure to test this code a few times by itself to understand exactly which parameters will work 
    postcode = num.find('div',{"class":"listing-search-item__location"}).text
    location.append(street)
    df_postcode = pd.DataFrame({'postcode':location})
    df_postcode['postcode'] = df_postcode['postcode'].str.replace("\nApartment\n ","")
    df_postcode['postcode'] = df_postcode['postcode'].str.replace("\n","")
    df_postcode['postcode'] = df_postcode['postcode'].str.replace("\s","")
    df_postcode['postcode'] = df_postcode['postcode'].str.replace("               ","")
    df_postcode['postcode'] = df_postcode['postcode'].str.replace("new","")
    df_postcode['postcode'] = df_postcode['postcode'].str[0:6]
    
    #getting the number of bedrooms: make sure to test this code a few times by itself to understand exactly which parameters will work 
    bedrooms_num = num.find_all('dd',{"class":"illustrated-features__description"})[1].text
    bedrooms.append(bedrooms_num)
    df_bedrooms = pd.DataFrame({'bedrooms':bedrooms})
    df_bedrooms['bedrooms'] = df_bedrooms['bedrooms'].str.replace("\D","")
    
    #getting the sq meter size: make sure to test this code a few times by itself to understand exactly which parameters will work 
    size = num.find_all('dd',{"class":"illustrated-features__description"})[0].text
    surface.append(size)
    df_surface = pd.DataFrame({'surface':surface})
    df_surface['surface'] = df_surface['surface'].str.replace("\D","")
    
    print(count)
    
    count += 1

# concat all the different dataframes created, culminating in dfa (completed dataframe)
result = pd.concat([df_price, df_agency], axis=1, sort=False)
result2 = pd.concat([result, df_postcode], axis=1, sort=False)
result3 = pd.concat([result2, df_bedrooms], axis=1, sort=False)
dfa = pd.concat([result3, df_surface], axis=1, sort=False)
