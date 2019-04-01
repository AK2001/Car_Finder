'''
Το πρόγραμμα αυτο κοιτάει τις πιό πρόσφατες αγγελίες από το Car.gr
και εμφανίζει κάποιο ή και κανένα αμάξι ανάλογα με την τιμή και
τα χιλιόμετρα που του ζητείται να ψάξει

'''


import requests
from bs4 import BeautifulSoup
from csv import writer

def Car_Finder(price_,kilometers_):
    response = requests.get('https://www.car.gr/latest/')    #Takes request from URL

    soup = BeautifulSoup(response.text,'html.parser')          #Parses the HTML

    posts = soup.select(".classified")     #Finds the classes which we will take the link to the car

    final_cars = 0

    with open('CarFinder.csv','w') as csv_file:                             #We open a csv file in order to save the values:
        csv_writer = writer(csv_file)                                       #'Price','Kilometers','Car Type' and 'Link' as text
        headers = ['Price','Kilometers','Car Type','Link']                  #Headers are made only for looks
        csv_writer.writerow(headers)                                        #It's best to open the new csv file in Excel

        print('Wait a moment...')
        for post in posts:

            link = post.find('a')['href']                                   #Finds the link to the car
            if "/parts" in link:
                continue

            correct_link = 'https://www.car.gr' + link                      #Note:The link we found was incomplete(missing https://...)


            new_response =requests.get(correct_link)
            new_soup = BeautifulSoup(new_response.text,'html.parser')       #Second request to the new completed link

            item = str(new_soup.find(id ='breadcrumb'))

            if 'Αυτοκίνητα' not in item:                                    #Makes sure we only get links for cars and not boats,motorcycles etc.
                pass
            else:

                INFO = new_soup.find_all('tr')
                try:
                    KM_List = INFO[5].find_all('td')
                    Kilometers = KM_List[1].get_text()                                                                  #Finds the Kilometers of the car
                    price = int(INFO[2].find(class_='p_p').get_text().strip('€').strip().replace('.',''))               #Finds the Price of the car and set it an int for later use
                    Kilometers = int(Kilometers.strip("χλμ").strip().replace('.',''))                                   #Makes the value for the kilometers an int for later use
                    car_type = (INFO[3].find_all('td'))[1].get_text().replace('Αυτοκίνητο - ','')                       #Finds the Car Type
                except Exception as e:
                    print("Sorry, something went wrong",e)                                                                #Try-Except because sometimes the values are missing from the site and it raises and error
                if str(Kilometers).isdigit():

                    if price <= price_ and Kilometers <= kilometers_:                                                   #This is where the maximum price and kilometers are set
                        print('FOUND CAR')
                        final_cars += 1
                        needed_price = str(price)+'€'
                        needed_KHM= str(Kilometers)+' KHM'
                        needed_link = correct_link                                                                      #Sets new name from the already found values for easier use
                        needed_type = car_type
                        csv_writer.writerow([needed_price,needed_KHM,needed_type,needed_link])                          #Writes the values needed

    if final_cars == 0:
        print("Sorry, no Cars found, try again in a moment please")


print('Please enter your maximum price and kilometers')
try:
    max_price = int(input('Price: '))
    max_kilo = int(input("Kilometers: "))
except ValueError:
    print("Please enter a number and not a text and try again")
else:
    Car_Finder(max_price,max_kilo)
