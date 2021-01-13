import requests
from latest_car_ads_links import car_links
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.car.gr/classifieds/cars/view/15035629-lancia-dedra?fromfeed=1")
soup = BeautifulSoup(response.text, 'html.parser')  # Second request to the new completed link

info = soup.find('tbody')
info = soup.findAll("td")

price_flag = True
kilometers_flag = True
category_flag = True

for i in range(len(info)):

    model_name = info[1].get_text().strip()
    if '€' in info[i].get_text().strip() and price_flag:
        price = info[i].get_text()[:20].strip()
        price_flag = False
    elif price_flag:
        price = "This information is missinga.."

    if "Χιλιόμετρα" in info[i].get_text().strip() and kilometers_flag:
        kilometers = info[i+1].get_text().strip()
        kilometers_flag = False
    elif kilometers_flag:
        kilometers = "This information is missing.."

    if "Κατηγορία" in info[i].get_text().strip() and category_flag:
        category = info[i+1].get_text().strip()
        category_flag = False
    elif category_flag:
        category = "This information is missing.."

counter = 0
for i in range (10):
    counter +=1
    print(counter)


print(model_name)
print(price)
print(kilometers)
print(category)
