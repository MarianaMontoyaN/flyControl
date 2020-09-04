'''
Written in Python 3.7 

Function that calculates the price of an air ticket depending on the distance traveled and the days of stay

Inputs:
    * Days: int value
    * Distance : float value

Outputs:
    * The price of the ticket: float value 
    * If a discount was applied or not: boolean value
'''

def calculate_price (days, distance):

    _PRICE_KM = 35.00 
    discount = False

    if days > 7 and distance > 1000:

        price = distance * _PRICE_KM * 0.7
        price = round(price, 2)
        discount = True
        return price, discount

    else:
        price = distance * _PRICE_KM
        price = round(price, 2)
        return price, discount

