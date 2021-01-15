# Car_Finder

## This is a project where the program find the most recent car ads from a site called [Car.gr](https://www.car.gr/latest/)

It manages it by using `seleniun` library to uncheck the other categories in the latest ads (by default all the other categories are active e.g. motorcycles or hobbies). Then, using `bs4` and `requests` each car ad's page is parsed into text and worked on to find only the details we want.

The purpose is to have easy access to the latest car ads and some specific details of each car (like 'Brand-model', 'Price', 'Kilometers', 'Car_category' and 'Link').
Each car ad's details, with the corresponding headers, are written to a .csv file in the end of the program.

**Libraries used**

* `selenium`
* `time`
* `requests`
* `bs4`
* `csv`

**NOTE**:This program searches only the latest ads for cars and **not** every car on the page!

