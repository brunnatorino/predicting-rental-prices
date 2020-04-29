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
## create a new dataframe with the lists as the columns
yelp1 = pd.DataFrame({'rating':rating,'zipcode':zipcode,'prices':prices})
## get the length of the zipcode
yelp1['zip_len'] = yelp1.zipcode.str.len()
## NL postcodes have more than 4 digits, so make sure we only keep those
yelp1 = yelp1[yelp1['zip_len'] > 4]
## I like to copy data frames when I make radical changes to data that took a while to be generated
## to ensure I can go back to the original data if I need
yelp = yelp1.copy()

## elimate whitespaces
yelp['postcode2'] = yelp['zipcode'].str.replace('\s','')
## only get 4 first digits of the postcode
yelp['postcode2']= yelp.postcode2.str[0:4]

## prices in yelp are represented by $, $$, $$$ or $$$$ so the length of the string can tell us how 
## expensive a restaurant is
yelp['price_len'] = yelp.prices.str.len()

## group by and get means by postcode area
yelp_prices = yelp.groupby(['postcode2']).price_len.mean()
yelp_rate = yelp.groupby(['postcode2']).rating.mean()

## create two dataframes and transform them into dictionaries 
yelp_prices = pd.DataFrame(data=yelp_prices)
yelp_rate = pd.DataFrame(data=yelp_rate)
dict1 = yelp_prices.to_dict()['price_len']
dict2 = yelp_rate.to_dict()['rating']

## delete the non-digit characters of the postcodes and copy dataframe to amsmodel1
df2.postcode2 = df2.postcode.str.replace("\D","") 
amsmodel1 = df2.copy()

## map the yelp price means and ratings means into our rental data frame
amsmodel1['yelp_prices'] = amsmodel1['postcode2'].map(dict1)
amsmodel1['yelp_ratings'] = amsmodel1['postcode2'].map(dict2)

## make sure all the integer columns are in fact integer types
amsmodel1['house_price'] = pd.to_numeric(amsmodel1['house_price'])
amsmodel1['bedrooms'] = pd.to_numeric(amsmodel1['bedrooms'])
amsmodel1['surface'] = pd.to_numeric(amsmodel1['surface'])
## drop any empty rows 
amsmodel1 = amsmodel1.dropna()
## how many columns do we have?
len(amsmodel1.columns)
