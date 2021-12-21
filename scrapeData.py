import requests
from bs4 import BeautifulSoup
from save_to_mysql import insertScrapedCars

URL = "https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&page=1&page_size=100&sort=best_match_desc&stock_type=cpo&year_max=&year_min=&zip="
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
scrapedCars = soup.find_all('div', class_='vehicle-card')

cars = []



for car in scrapedCars:
    #name
    name = car.find('h2').get_text()
    #mileage
    mileage = car.find('div', {'class':'mileage'}).get_text()
    #dealer_name
    dealer_name = car.find('div', {'class':'dealer-name'}).get_text()
    #rate
    try:
        rating = car.find('span', {'class':'sds-rating__count'}).get_text()
    except:
        rating = "n/a"
    #rate_count
    rating_count = car.find('span', {'class':'sds-rating__link'}).get_text()
    #price
    price = car.find('span', {'class':'primary-price'}).get_text()
    toAppend = name, mileage, dealer_name, rating, rating_count, price
    cars.append(toAppend)

insertScrapedCars(cars)
    