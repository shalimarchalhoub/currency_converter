from locale import currency
from pickle import FRAME
import unittest
from urllib import response
from frankfurter import Frankfurter

class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class 
    """ 
    def test_Url(self):
        
        frankfurter_test = Frankfurter()

        base_url = 'https://api.frankfurter.app/'
        currencies_url = 'currencies'
        historical_url = None

        self.assertEqual(frankfurter_test.base_url, base_url)
        self.assertEqual(frankfurter_test.currencies_url , currencies_url)
        self.assertEqual(frankfurter_test.historical_url , historical_url)
 
class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from checks.py
    """

    
    def test_get_currencies(self):
        
        test1 = Frankfurter()

        test1.base_url = "https://api.frankfurter.app/"
        test1.currencies_url = "currencies"
        self.assertEqual(test1.get_currencies_list(), test1.get_currencies_list())
        
    

class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """
    def test_check_currencies(self):

        test1 = Frankfurter()

        currency1 = "AUD"
        currency2 = "ppp"
        self.assertEqual(test1.check_currency(currency1), True)
        self.assertEqual(test1.check_currency(currency2), False)

    
class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """
    def test_check_call_historical_rate(self):
        test1 = Frankfurter()
        currency1 = "AUD"
        currency2 = "USD"
        Date = "2020-05-02"
        Rate = 0.65526
        self.assertEqual(test1.get_historical_rate(currency1, currency2, Date), Rate)



if __name__ == '__main__':
    unittest.main()