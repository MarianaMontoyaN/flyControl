
''' 
    UNIT TESTING

    Devoloped By: Mariana Montoya Naranjo
    Written in Python 3.7 using unittest unit testing framework
'''

import unittest
from pyunitreport import HTMLTestRunner 
from dollar_today import dollar_today_scrap
from price_ticket import calculate_price
from package import Package
from flight import Flight

class Testing(unittest.TestCase):

    '''
    ------ VALIDATION FUNCTION DOLLAR_TODAY ------  
    Test the update of the dollar price
    '''

    def test_validations_inputs(self):
        
        result_dollar_today  = dollar_today_scrap() 

        self.assertFalse(result_dollar_today == 0)

    '''
    ------ VALIDATION FUNCTION DOLLAR_TODAY ------  
    Test the calculation of the price of an air ticket depending on the distance traveled and the days of stay
    '''

    def test_price_ticket(self):
        
        result_price_ticket, result_discount = calculate_price(8, 150) 
        result_expected_price_ticket = 5250
        result_expected_discount = False

        self.assertEqual(result_price_ticket, result_expected_price_ticket)
        self.assertEqual(result_discount, result_expected_discount)

    def test_price_ticket_with_discount(self):
        
        result_price_ticket, result_discount = calculate_price(10, 1200) 
        result_expected_price_ticket = 29400
        result_expected_discount = True

        self.assertEqual(result_price_ticket, result_expected_price_ticket)
        self.assertEqual(result_discount, result_expected_discount)

    
    '''
    ------ VALIDATION CLASS PACKAGE ------  
    Test the calculation of the baggage price in pesos and dollars
    '''

    def test_calculate_price_pesos(self):

        package1 = Package(22, 3500)
        
        result1 = package1.calculate_price_pesos() 
        result_expected1 = 0

        self.assertEqual(result1, result_expected1)

        package2 = Package(128, 3500)
        
        result2 = package2.calculate_price_pesos() 
        result_expected2 = 192000

        self.assertEqual(result2, result_expected2)

        package3 = Package(400, 3500)
        
        result3 = package3.calculate_price_pesos() 
        result_expected3 = 1000000

        self.assertEqual(result3, result_expected3)

    def test_calculate_price_pesos(self):
    
        package1 = Package(22, 3500)
        
        result1 = package1.calculate_price_dollar() 
        result_expected1= 0

        self.assertEqual(result1, result_expected1)

        package2 = Package(128, 3500)
        
        result2 = package2.calculate_price_dollar() 
        result_expected2 = 54.86

        self.assertEqual(result2, result_expected2)

        package3 = Package(400, 3500)
        
        result3 = package3.calculate_price_dollar() 
        result_expected3 = 285.71

        self.assertEqual(result3, result_expected3)
    


if __name__ == "__main__":

    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name= 'unittests-report'))