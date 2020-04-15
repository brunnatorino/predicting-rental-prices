rom geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
import geopy.geocoders
from geopy.geocoders import Nominatim
import geopy
import geopandas
import pandas as pd
import time 

df['postcode'] = df['street'].str[0:16]

list_of_points = []

df['address'] = df['street'] +',Amsterdam' + ',The Netherlands,' + df['postcode']

df['postcode2'] = df['postcode'].str.replace('\s','')

df['address2'] = df['street'] + ',' + 'Amsterdam' + ',The Netherlands,' + df['postcode2']

df['address3'] = df['street'] + ',' + 'Amsterdam' + ',Netherlands,' + df['postcode']

df['address4'] = df['street'] + ',' + 'Amsterdam' + ',The Netherlands'


locator = Nominatim(user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9')

df2 = pd.DataFrame(columns=['house_price', 'type','rental_agency','street','city','bedrooms',
                            'surface','furnished', 'move_in_date','inclusive','price_per_sq_meter',
                           'furnished_encoded','inclusive_encoded','postcode',
                            'address','postcode2'])

count = 0
while count <= 149: 
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
                
    df2 = pd.concat([df2, df_new], sort=False)
    time.sleep(1)
    count += 1
