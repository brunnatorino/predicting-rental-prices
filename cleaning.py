## DATA FORMATTING 

count = 0
house_price = []
rental_agency = []
location = []
city = []
bedrooms = []
surface = []

n = int(len(houses)) - 1

while count <= n:
    
    num = houses[int(count)]
    
    price = num.find_all('span',{"class":"listing-search-item__price"})[0].text
    house_price.append(price)
    df1 = pd.DataFrame({'house_price':house_price})
    df1['house_price'] = df1['house_price'].str.replace("\D","")
    df1['house_price'] = df1['house_price'].str.replace("per month","")
    
    try:
        agency = num.find_all('a', href=True)[2].text
    except IndexError:
        agency = 'none'
    rental_agency.append(agency)
    df2 = pd.DataFrame({'rental_agency':rental_agency})
    
    street = num.find('div',{"class":"listing-search-item__location"}).text
    location.append(street)
    df3 = pd.DataFrame({'street':location})
    df3['street'] = df3['street'].str.replace("\nApartment\n ","")
    df3['street'] = df3['street'].str.replace("\n","")
    df3['street'] = df3['street'].str.replace("               ","")
    
    bedrooms_num = num.find_all('dd',{"class":"illustrated-features__description"})[1].text
    bedrooms.append(bedrooms_num)
    df4 = pd.DataFrame({'bedrooms':bedrooms})
    df4['bedrooms'] = df4['bedrooms'].str.replace("\D","")
    
    size = num.find_all('dd',{"class":"illustrated-features__description"})[0].text
    surface.append(size)
    df5 = pd.DataFrame({'surface':surface})
    df5['surface'] = df5['surface'].str.replace("\D","")
    
    print(count)
    
    count += 1
    
result = pd.concat([df1, df2], axis=1, sort=False)
result2 = pd.concat([result, df3], axis=1, sort=False)
result3 = pd.concat([result2, df4], axis=1, sort=False)
dfa = pd.concat([result3, df5], axis=1, sort=False)
