from selenium import webdriver
import time

def car_links():

    PATH = "C:\Program Files (x86)\chromedriver.exe"  # Location of the chromedriver on the system
    driver = webdriver.Chrome(PATH)  # Creating webdriver

    driver.get("https://www.car.gr/latest/")  # Accessing the website

    categories = driver.find_elements_by_class_name("btn.btn-sm.recent-btn.active") # Finds all the categories for ads in the site

    for i in range(1,len(categories)):  # By default there are 9 categories, the last one (Μικρές αγγελίες) is already non-active
        categories[i].click()           # We want only the car (Αυτοκίνητα) category to be active so we "click" every other to
                                        # disable it.
    links = []

    time.sleep(2)  # Waits x seconds to ensure that the correct category (Αυτοκίνητα = cars) is active and the car ads are
                   # shown. If we want to wait longer to see more ads just increase the x value (ideal 5 mins for approx. 20 car ads)

    ads = driver.find_elements_by_class_name("f-wrapper.entry")  # Finds all the ads from the site

    for i in range(len(ads)):  # Gets the href attribute and stores it in a list named "Links"
        links.append(ads[i].get_attribute("href"))


    #print(len(links)) # We can check if the number of car links that were saved are actually the same as the number of car ads

    #time.sleep(1)  # Waits x second (Useful if we want to double check the length of links and the content on the page

    driver.quit()  # Closes the browser

    return links  # Returns the links list containing the latest car ad links for the website
