"""
This program
"""
from car_info_collector import car_info_collector
from latest_car_ads_links import car_links
from csv import writer


def car_finder(cars_dict):
    with open('CarFinder.csv', 'w') as csv_file:  # We open a csv file in order to save the values we want:
        csv_writer = writer(csv_file)

        headers = ['Brand-model', 'Price', 'Kilometers', 'Car_category', 'Link']  # We set the headers we want in our .csv file

        csv_writer.writerow(headers)  # It's best to open the new csv file in Excel

        for car in cars_dict:                           # We want to search each car's details separately
            car_details = cars_dict.get(car)            # Remember cars_dict is a nested dictionary where keys are car1, car2...
            csv_writer.writerow(                        # and values are dictionaries of each car's details (keys shown to the left)
                [car_details.get('Brand-model'),        # Writes each of car's details to the .csv file
                 car_details.get('Price'),
                 car_details.get('Kilometers'),
                 car_details.get('Car_category'),
                 car_details.get('Link')])

    print("Successfully created .csv file <CarFinder.csv> with every car ad alongside some of it's details.")


if __name__ == '__main__':  # This part of code executes only when this file is run solo, try-except to catch any code problems
    links = []
    car_dict = {}
    try:
        links = car_links()
    except Exception as e:
        print("Something went wrong with car_links() function in latest_car_ads_links.py\n"
              "Possible the website <https://www.car.gr/latest/> has changed since last code update\n"
              "Exception: ", e)
    else:
        try:
            if (len(car_info_collector(links)) != (len(links))):
                print("car_info_collector() didn't work correctly.\n"
                      "<-!-> Possible syntax error went unnoticed.\n"
                      "While there are ad links found the function didn't manage to work on them.\n"
                      "<-!-> Possible the website of each car ad has changed since last code update.")
            else:
                car_dict = car_info_collector(links)
        except Exception as e:
            print("Something went wrong with car_info_collector() function in car_info_collector.py\n"
                  "Exception: ", e)
        else:
            try:
                car_finder(car_dict)
            except Exception as e:
                print("Something went wrong with car_finder() function in car_finder.py\n"
                      "Exception: ", e)
