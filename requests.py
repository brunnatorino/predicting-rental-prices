# import all the relevant packages 
import pandas as pd
import itertools 
from bs4 import BeautifulSoup
import requests
from requests import get
import time
from random import seed
from random import random
from random import randint

# specify the url format
url = 'https://www.pararius.com/apartments/amsterdam/page-'
# initialize a list called houses 
houses = []
# initialize variable count at 1
count = 1

# first while loop that will run 100 times (adjust this to how many pages you want to scrape)
while count <= 100:
    # initialize variable new_count at 0
    new_count = 0
    # if loop that specifies the first page separately (many websites have a first page url format different than other pages)
    if count == 1:
        first_page = 'https://www.pararius.com/apartments/amsterdam/page-1'
        # request the response
        response = get(first_page)
        # parse through the html 
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # in the html of the page, find all the bins with <li> and class:
        house_data = html_soup.find_all('li', class_="search-list__item search-list__item--listing")
        # I like to print where the program is on the screen so we can follow its progress and where any errors happened
        print(first_page)
        
        # if the response was not empty (if something was actually scraped)
        if house_data != []:
            # add to the list houses
            houses.extend(house_data)
            # random wait times
            value = random()
            scaled_value = 1 + (value * (9 - 5))
            print(scaled_value)
            time.sleep(scaled_value)
    # pages other than the first
    elif count != 1:
        # collect four and wait random times 
        while new_count < 4:
            count2 = new_count + count
            new_url = url + str(count2)
            print(new_url)

            response = get(new_url)
            html_soup = BeautifulSoup(response.text, 'html.parser')
            print(response)
            house_data = html_soup.find_all('li', class_="search-list__item search-list__item--listing")

            if house_data != []:
                houses.extend(house_data)
                value = random()
                scaled_value = 1 + (value * (9 - 5))
                print(scaled_value)
                time.sleep(scaled_value)
                new_count += 1
            # if you get empty response, stop the loop
            else:
                print('empty')
                break

      

    count += 1
