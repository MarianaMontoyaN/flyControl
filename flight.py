'''
Written in Python 3.7 

Class that models each flight

INPUTS:
    * name_flight: string value
'''

from database import database
from package import Package

class Flight:

    def __init__(self, name_flight):

        self._MAXIMUM_LOAD = 18000
        self.name_flight = name_flight
        self.list_packages = database.show_packages(self.name_flight)
        self.number_packages = len(self.list_packages)
        self.total_weight=0

        self.weight_total_packages()


    '''
    Method that calculates the total weight of the cargo
    '''
    def weight_total_packages(self):

        for package_one in self.list_packages:
            self.total_weight += package_one[1]


    '''
    Method that adds a package on the fly

    Output:
        *capacity : boolean value that indicates if in the flight there is capacity
    '''
    def add_package(self, weight, price_pesos, price_dollars):

        capacity = True

        if self.total_weight + weight <= self._MAXIMUM_LOAD:

            database.add_package_db(self.name_flight, weight, price_pesos, price_dollars)

        else:
            capacity = False

        return capacity


    '''
    Method that calculate the average weight per package

    Output:
        *average : int value 
    '''
    def average_weight(self):

        average = self.total_weight//self.number_packages

        return average


    '''
    Method that indicates the weight of the heaviest and lightest packages

    Output:
        *lighter_package : int value 
        *heavier_package : int value 
    '''
    def heavier_lighter_package(self):
        
        weight_packages = []
        
        for package in self.list_packages:
            weight_packages.append(package[1])

        index_lighter = weight_packages.index(min(weight_packages))
        index_heavier = weight_packages.index(max(weight_packages))

        lighter_package = self.list_packages[index_lighter][1]
        heavier_package = self.list_packages[index_heavier][1]

        return lighter_package, heavier_package

    '''
    Method that calculate income in pesos

    Output:
        *total_pesos : float value 
    '''
    def income_pesos(self):
        
        total_pesos = 0

        for package_one in self.list_packages:
            total_pesos += package_one[2]

        return round(total_pesos, 2)

    '''
    Method that calculate income in dollars

    Output:
        *total_dollars : float value 
    '''
    def income_dollars(self):

        total_dollars = 0

        for package_one in self.list_packages:
            total_dollars += package_one[3]

        return round(total_dollars, 2)
