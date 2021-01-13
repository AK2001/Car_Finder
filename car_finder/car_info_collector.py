import requests
from latest_car_ads_links import car_links
from bs4 import BeautifulSoup


def car_info_collector(car_links):
    global price, kilometers, category
    cars = {}  # First dictionary that will contain each car found
    counter = 0  # A simple counter

    try:
        for link in car_links:  # A loop through each car link to find the info we need

            car_information = {}  # Second dictionary that will contain info for each car found

            response = requests.get(link)  # Request to the car link
            soup = BeautifulSoup(response.text, 'html.parser')  # Parses the car link to text

            soup.find('tbody')  # We find where in the site the info we needs is
            info = soup.findAll("td")

            price_flag, kilometers_flag, category_flag = True  # Basic variable flags for later conditions


            for i in range(len(info)):  # Loop through the list of all information found

                model_name = info[1].get_text().strip()  # Model name is found in the first position of our info list
                car_information["model"] = model_name

                if '€' in info[i].get_text().strip() and price_flag:  # If the euro sign is found in one of the "boxes" of info
                    price = info[i].get_text()[:20].strip()           # The scrip searches for the next which has the value we need
                    price_flag = False                                # [20] is used because sometimes after the price there are
                elif price_flag:                                      # messages like "Συζιτήσημη τιμή", which we don't want
                    price = "This information is missing.."
                car_information["price"] = price                      # Enters the price value and key into the second dictionary

                if "Χιλιόμετρα" in info[i].get_text().strip() and kilometers_flag:
                    kilometers = info[i + 1].get_text().strip()
                    kilometers_flag = False
                elif kilometers_flag:
                    kilometers = "This information is missing.."
                car_information["kilometers"] = kilometers

                if "Κατηγορία" in info[i].get_text().strip() and category_flag:
                    category = info[i + 1].get_text().strip()
                    category_flag = False
                elif category_flag:
                    category = "This information is missing.."
                car_information["car_category"] = category

            counter += 1        # Simple counter used for the first dictionary key names

            cars["car" + str(counter)] = car_information  # Saves each car as car1,car2... as keys with each car_information as value


    except Exception:  # If latest_car_ads_links doesn't find any link this message is shown
        print("No car ads were found this moment.")

    print(cars)


if __name__ == '__main__':
    try:
        links = car_links()
    except Exception:
        print("Something went wrong")
    else:
        car_info_collector(links)
        print(links)
