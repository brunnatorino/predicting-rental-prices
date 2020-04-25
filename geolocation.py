## importing nominatin and other tools
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
import geopy.geocoders
from geopy.geocoders import Nominatim
import geopy
import geopandas
import pandas as pd
import time 

## initialize a list
list_of_points = []

## an address on nominatim can be hard to find at first, so add a few options by varying the use of commas,
## the use of state names, and all the variations for a country's name (The Netherlands, Netherlands, Holland...)
df['address'] = df['postcode']

df['postcode2'] = df['postcode'].str.replace('\s','')

df['address2'] = df['postcode2']

## start the locator with a header 
locator = Nominatim(user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9')

## create a dataframe with all the columns you already have (including the additional address columns)
df2 = pd.DataFrame(columns=['house_price', 'rental_agency',
                            'postcode','bedrooms','surface',
                            'address','postcode2'])

## this while loop basically tries every address that you specified until one is successful in geting the lat/lon
count = 0
while count <= 500: 
    if count == 0:
        df_new = df[0:1]
    else:
        a = count
        n = count+1
        print(a)
        print(n)
        df_new = df[a:n]
    geocode = RateLimiter(locator.geocode, min_delay_seconds=2.5)
    try:
        df_new['location'] = df_new['address'].apply(geocode)
        df_new['point'] = df_new['location'].apply(lambda loc: tuple(loc.point) if loc else None)
        df_new[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df_new['point'].tolist(), index=df_new.index)
    except ValueError:
        try:
            df_new['location'] = df_new['address2'].apply(geocode)
            print('trying second address')
            df_new['point'] = df_new['location'].apply(lambda loc: tuple(loc.point) if loc else None)
            df_new[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df_new['point'].tolist(), index=df_new.index)
        except ValueError:
          ## I didn't need an address 3 or 4 for this example, but I will leave it here in case you need it
            try:
                df_new['location'] = df_new['address3'].apply(geocode)
                print('trying third address')
                df_new['point'] = df_new['location'].apply(lambda loc: tuple(loc.point) if loc else None)
                df_new[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df_new['point'].tolist(), index=df_new.index)
            except ValueError:
                try:
                    df_new['location'] = df_new['address4'].apply(geocode)
                    print('trying fourth address')
                    df_new['point'] = df_new['location'].apply(lambda loc: tuple(loc.point) if loc else None)
                    df_new[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df_new['point'].tolist(), index=df_new.index)
                except ValueError:
                    df_new = df_new.dropna(subset=['location'])
                    list_of_points.append(a)
    # concat everything         
    df2 = pd.concat([df2, df_new], sort=False)
    # give nominatim some time to not overwhelm their website with requests
    time.sleep(1)
    count += 1
