# FLIGHT CONTROL

Desktop application written in python 3.7 (necessary to run the application), consists of two parts, the first calculates the price of a ticket depending on the distance traveled and the days of stay, it also conditions a discount of 30% when the distance traveled is greater than 1000 km and the stay is longer than 7 days.

The second part controls the reception of luggage on a flight. Each package cannot exceed the load capacity of the plane, nor exceed 500 kg. The price of the package is calculated depending on its weight, it is delivered in colombian pesos and in dollars, the TMR is updated by searching the web for the current value. There are three flights available for shipping.

The project is structured with Object Oriented Programming, where the flights and packages are modeled as classes. The following Python 3 libraries are used: Tkinter for the graphical interface, sqlite3 for the database, selenium for webscraping, unittest and pyunitreport for the unit tests and their report.

## SETUP

The requirements to run the application must be installed.

```
pip install -r requirements.txt
```

To run the application you must run the following command in the command console

```
python index.py
```

## WEB SCRAPING TO CALCULATE DOLLAR PRICE

It is necessary to have version 85 of the Google Chrome browser and run the application on the Windows operating system, if any of the above requirements are not met, the baggage price will be calculated with TMR = 3500

## DATABASE

sqlite3 database, when executing the application for the first time, 30 random packages are generated for each flight.

## UNIT TESTS

To run the unit tests run the following file

```
python unitTesting.py
```

An HTML report is created in the reports folder




