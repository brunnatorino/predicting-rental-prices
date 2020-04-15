import pandas as pd
import itertools 
from bs4 import BeautifulSoup
import requests
from requests import get
import time
from random import seed
from random import random
from random import randint


url = 'https://www.pararius.com/apartments/amsterdam/page-'

houses = []
count = 1

while count <= 100: 
    new_count = 0
    
    if count == 1:
        first_page = 'https://www.pararius.com/apartments/amsterdam/page-1'
        response = get(first_page)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        house_data = html_soup.find_all('li', class_="search-list__item search-list__item--listing")
        print(first_page)
        
        if house_data != []:
            houses.extend(house_data)
            value = random()
            scaled_value = 1 + (value * (9 - 5))
            print(scaled_value)
            time.sleep(scaled_value)
    elif count != 1:
        while new_count < 4:
            count2 = new_count + count
            new_url = url + str(count2)
            print(new_url)

            response = get(new_url, headers=headers)
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
            else:
                print('empty')
                break

      

    count += 1
