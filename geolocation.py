from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
import geopy.geocoders
from geopy.geocoders import Nominatim
import geopy
import geopandas
import pandas as pd
import time 


list_of_points = []

df['address'] = df['postcode']

df['address2'] = df['postcode'].str.replace('\s','')

locator = Nominatim(user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9')

df2 = pd.DataFrame(columns=['house_price', 'rental_agency',
                            'postcode','bedrooms','surface',
                            'address','address2'])
n = int(len(houses)) - 1

count = 1
while count <= n: 
    if count == 0:
        df_new = df[0:1]
    else:
        a = count
        n = count+1
        print(a)
        print(n)
        df_new = df[a:n]
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
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
            df_new = df_new.dropna(subset=['location'])
            list_of_points.append(a)
                
    df2 = pd.concat([df2, df_new], sort=False)
    time.sleep(1)
    count += 1
