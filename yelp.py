import requests
import json


api_key='secret'
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'

offset = 1
while count <= 901:
    params={'term':'Restaurants', 'location': 'amsterdam', 'limit': 1, 'offset': offset}
    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)
    n = 0
    while n <= 50:
        try:
            price_data = parsed["businesses"][n]['price']
            ratings_data = parsed["businesses"][n]['rating']
            zipcode_data = parsed["businesses"][n]["location"]["zip_code"]
            rating.append(ratings_data)
            zipcode.append(zipcode_data)
            cities2.append(cities_data)
            prices.append(price_data)
        except KeyError:
            pass
        n += 1
    offset += 50


yelp1 = pd.DataFrame({'name':name, 'rating':rating, 'address':address,'zipcode':zipcode, 'city':city, 'prices':prices,'coordinates':coordinates})


