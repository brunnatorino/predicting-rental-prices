import requests
import json


api_key='your-api-key-here'
headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/businesses/search'

## creating global empty lists so we don't overwrite them but keep adding data to them
rating = []
zipcode = []
cities2 = []
prices = []

## offset can be explained as the page number and with limit can gather max 1000 business data from Yelp every day
offset = 1
## loop to iterate over 7 pages of 50 businesses each = 350 businesses in Amsterdam 
while offset <= 7:
    params={'term':'Restaurants', 'location': 'amsterdam', 'limit': 50, 'offset': offset}
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
            prices.append(price_data)
            
        except:
            ## some of the data gathered are not going to have the necessary information
            ## so we skip those 
            pass
    offset += 1
