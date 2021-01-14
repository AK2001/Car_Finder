# Car_Finder

## This is a project where the program find the most recent car ads from a site called [Car.gr](https://www.car.gr/latest/)

It manages it by using `seleniun` library to uncheck the other categories in the latest ads (by default all the other categories are active e.g. motorcycles or hobbies)

The purpose is to have easy access to the latest car ads alongside to some to its details (like 'Brand-model', 'Price', 'Kilometers', 'Car_category' and 'Link').
Each car ad's details are written to a .csv file in the end.

**Libraries used**

* `selenium`
* `time`
* `requests`
* `bs4`
* `csv`

**NOTE**:This program searches only the latest ads for cars and **not** every car on the page!

