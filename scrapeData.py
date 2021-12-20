import requests
from bs4 import BeautifulSoup
from firebase import firebase
from datetime import datetime

fb_app = firebase.FirebaseApplication(
    'https://cars-details-73d46-default-rtdb.firebaseio.com/', None)

URL = "https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&page=1&page_size=100&sort=best_match_desc&stock_type=cpo&year_max=&year_min=&zip="
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
cars = soup.find_all('div', class_='vehicle-card')

name = []
mileage = []
dealer_name = []
rating = []
rating_count = []
price = []


for car in cars:
    #name
    name.append(car.find('h2').get_text())
    #mileage
    mileage.append(car.find('div', {'class':'mileage'}).get_text())
    #dealer_name
    dealer_name.append(car.find('div', {'class':'dealer-name'}).get_text())
    #rate
    try:
        rating.append(car.find('span', {'class':'sds-rating__count'}).get_text())
    except:
        rating.append("n/a")
    #rate_count
    rating_count.append(car.find('span', {'class':'sds-rating__link'}).get_text())
    #price
    price.append(car.find('span', {'class':'primary-price'}).get_text())


#firbase database function
def firebase():
    car_data = {'Name': name,
        'mileage': mileage,
        'dealer_name': dealer_name,
        'rating': rating,
        'rating_count': rating_count,
        'price': price,
        }


    result = fb_app.post('/cars', car_data)
    print(result)


#Schedler function to automate the scraper
def scheduler():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # Trigger scraper function everyday on 12 AM
    if current_time == "00:00:00":   
        firebase()

scheduler()




