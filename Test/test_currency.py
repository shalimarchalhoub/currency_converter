from operator import truediv
from traceback import print_tb
import unittest
from checks import check_arguments
from currency import CurrencyConverter
from frankfurter import Frankfurter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """
    def test_init(self):
        self.from_currency = "AUD"
        self.to_currency="USD"
        self.amount = 1.00
        self.rate = 0.6763854
        self.inverse_rate = 1.4786
        self.date = "2020-02-05"
        self.api = Frankfurter()

class TestCurrencyCheck(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
    def test_check_currencies(self):
        
        test1 = CurrencyConverter('USD' , 'AUD' , '2020-05-02')
        self.assertEqual(test1.check_currencies(), True)

        #from currency wrong
        test2 = CurrencyConverter('USSSD' , 'AUD' , '2020-05-02')
        with self.assertRaises(SystemExit) as cm:
            
           self.assertEqual(test2.check_currencies(), cm.exception)

        #to currency wrong
        test3 = CurrencyConverter('USD' , 'AxxUD' , '2020-05-02')
        with self.assertRaises(SystemExit) as cm:
            
           self.assertEqual(test3.check_currencies(), cm.exception)

        #both currencies are wrong
        test4 = CurrencyConverter('USfffD' , 'AxxUD' , '2020-05-02')
        with self.assertRaises(SystemExit) as cm:
            
           self.assertEqual(test4.check_currencies(), cm.exception)


class Test_Reverse_Rate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """
    def test_reverse_rate(self):

        test1 = CurrencyConverter('USD' , 'AUD' , '2020-05-02')
        test1.rate = 2.00
        inverse_rate = 0.5
        self.assertEqual(test1.reverse_rate(), inverse_rate)
        
class TestRoundRate(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    def test_check_currencies(self):

        test1 = CurrencyConverter('USD' , 'AUD' , '2020-05-02')
        rate = 2.645878
        roundrate=2.6459
        self.assertEqual(test1.round_rate(rate), roundrate)

class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    def test_historical_rate(self):

        test1 = CurrencyConverter('USD' , 'AUD' , '2020-05-02')
        self.assertEqual(test1.get_historical_rate(), None)
    
if __name__ == '__main__':
    unittest.main()