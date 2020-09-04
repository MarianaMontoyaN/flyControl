'''
Written in Python 3.7 

Class that models each packet of a flight's cargo

INPUTS:
    * Weight: int value
    * Value dollar: float value
'''

class Package:

    def __init__(self, weight, dollar_today):

        self.weight = weight
        self.dollar_today = dollar_today
        self.price_pesos=0
        self.price_dollar=0

        self.calculate_price_pesos()
        self.calculate_price_dollar()

    '''
    Method that calculates the price of luggage in pesos

    Outputs:
    * Price: float value 
    '''

    def calculate_price_pesos(self):

        if self.weight >= 0 and self.weight <= 25:
            self.price_pesos=0

        elif self.weight >= 26 and self.weight <= 300:
            self.price_pesos = 1500*self.weight
        
        elif self.weight >= 301 and self.weight <= 500:
           self.price_pesos = 2500*self.weight
        
        return self.price_pesos

    '''
    Method that calculates the price of luggage in dollars

    Outputs:
    * Price: float value 
    '''

    def calculate_price_dollar(self):

        self.price_dollar = round(self.price_pesos/self.dollar_today, 2)

        return self.price_dollar

