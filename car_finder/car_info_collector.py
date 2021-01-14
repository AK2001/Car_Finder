import requests
from latest_car_ads_links import car_links
from bs4 import BeautifulSoup


def car_info_collector(car_list_of_links):
    global price, kilometers, category, car_link
    cars = {}  # First dictionary that will contain each car found
    counter = 0  # A simple counter

    try:

        for link in car_list_of_links:          # A loop through each car link to find the info we need
            car_information = {}                # Second dictionary that will contain info for each car found

            response = requests.get(link)                       # Request to the car link
            soup = BeautifulSoup(response.text, 'html.parser')  # Parses the car link to text

            soup.find('tbody')          # We find where in the site the info we needs is
            info = soup.findAll("td")

            price_flag = True       # Basic variable flags for later conditions
            kilometers_flag = True
            category_flag = True
            link_flag = True

            for i in range(len(info)):                         # Loop through the list of all information found
                model_name = info[1].get_text().strip()        # Model name is found in the first position of our info list
                car_information["Brand-model"] = model_name

                if '€' in info[i].get_text().strip() and price_flag:    # If the euro sign is found in one of the "boxes" of info
                    price = info[i].get_text()[:20].strip()             # The scrip takes the text out of it because it is the value we need
                    price_flag = False                                  # [20] is used because sometimes after the price there are
                elif price_flag:                                        # messages like "Συζιτήσημη τιμή", which we don't want
                    price = "This information is missing"

                car_information["Price"] = price  # Enters the price value and key into the second dictionary

                if "Χιλιόμετρα" in info[i].get_text().strip() and kilometers_flag:   # -1- If the "Χιλιόμετρα" is found in one of the "boxes" of info
                    kilometers = info[i + 1].get_text().strip()                      # -2- The scrip searches for the next which has the value we need
                    kilometers_flag = False                                          # -3- Changes the boolean value to False to stop the script from
                elif kilometers_flag:                                                # -4- searching again for "Χιλιόμετρα" and not founding it
                    kilometers = "This information is missing"                       # -5- Alternative message if the value we want isn't found

                car_information["Kilometers"] = kilometers                           # -6- Enters the key and value to the second nested-dictionary

                if "Κατηγορία" in info[i].get_text().strip() and category_flag:    # Same as the above block of comments (1-6)
                    category = info[i + 1].get_text().strip()
                    category_flag = False
                elif category_flag:
                    category = "This information is missing"

                car_information["Car_category"] = category

                if "Σύνδεσμος" in info[i].get_text().strip() and link_flag:  # Same as the above block of comments (1-6)
                    car_link = info[i + 1].get_text().strip()
                    link_flag = False
                elif link_flag:
                    car_link = "This information is missing"

                car_information["Link"] = car_link

            counter += 1  # Simple counter used for the first dictionary key names

            cars["car" + str(counter)] = car_information  # Saves each car as car1,car2... as keys with each car_information as value

    except Exception:  # If car_links() doesn't find any car links this message is shown
        print("No car ads were found this moment.")

    return cars  # Returns a nested dictionary of with car1, car2.. as keys and each car's details dictionary as values


if __name__ == '__main__':  # This part of code executes only when this file is run solo, try-except to catch any code problems
    links = []
    try:
        links = car_links()
    except Exception as e:
        print("Something went wrong with car_links() function in latest_car_ads_links.py\n"
              "<-!-> Possible the website <https://www.car.gr/latest/> has changed since last code update.\n"
              "Exception: ", e)
    else:

        try:
            print(car_info_collector(links))
            print(len(links))
        except Exception as e:
            print("Something went wrong with car_info_collector() function in car_info_collector.py\n"
                  "<-!-> Possible the website of each car ad has changed since last code update.\n"
                  "Exception: ", e)


