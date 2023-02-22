# Car_Finder

## This is a personal project where the aim is to create a web scraper program that allows the user to get access to the latest car ads published in a site called [Car.gr](https://www.car.gr/latest/)

The program utilized a Python library called `seleniun`, to "visit" the site's main page and then "extract" only information about the latest car ads that are uploaded to the site at that time. Then, using `bs4` and `requests` each car ad's page is parsed into text and worked on to find only the specified details, such as car model or price.

The *purpose* of the application is to have easy access to the latest car ads and some specific details of each car, such as 'Brand-model', 'Price', 'Kilometers', 'Car_category' and 'Link', without having to manually search the site.

Each car ad's details, with the corresponding headers, are written to a .csv file in the end of the program execution.

**List of packages used**

* `selenium`
* `time`
* `requests`
* `bs4`
* `csv`

**NOTE**:This program searches only the latest ads for cars and **not** every car on the page!

**NOTE**:There is a chance that this program might not work correctly due to maintenance issues! I.E., the site might change its UI, so the web-parsing will not be successfull
