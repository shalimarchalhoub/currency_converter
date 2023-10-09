from locale import currency
from os import truncate
from pickle import NONE
import sys
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """
    
    def __init__(self, from_currency, to_currency, date):

        self.from_currency : str = from_currency
        self.to_currency : str = to_currency
        self.amount = 1.00
        self.rate = 0.00
        self.inverse_rate = 0.00
        self.date : str = date
        self.api = Frankfurter()

    def check_currencies(self):
    
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        Use the Frankfurter check_currency function to check the validity of from_currency and save it in variable
        Use the Frankfurter check_currency function to check the validity of to_currency and save it in variable
      
        Returns 
        -------
        Str:
            Relevant string message if one or both currencies are wrong mentioning the wrong currency/currencies
        Sys:
            System.Exit(); the system will exit if a currency is invalid
        Boolean:
            True: If the currencies are accurate

        """
        
        check_from_currency = self.api.check_currency(self.from_currency)
        check_to_currency = self.api.check_currency(self.to_currency)

        if check_from_currency == False and check_to_currency == False:
             raise SystemExit(f"{self.from_currency} and {self.to_currency} are not valid currency codes")
            
        elif check_from_currency == False and check_to_currency == True:
            raise SystemExit(f"{self.from_currency} is not a valid currency code")

        elif check_from_currency == True and check_to_currency == False:
            raise SystemExit(f"{self.to_currency} is not a valid currency code")

        else: return True


    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        Take the rate attribute from the class and inverse it
        Round rate to 4th decimal place
        Save it in self.inverse_rate class attribute
        
        Returns
        -------
        float: reverse_rate
            inverse rate rounded to the 4th decimal place

        """
        
        inverse = (1.00 / self.rate)
        self.inverse_rate = round(inverse , 4)
        return self.inverse_rate


    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        float: rate
            The conversion rate to be applied on the origin amount (origin -> destination)


        Pseudo-code
        ----------
        Preform the function roud() on the rate and round it to 4 decimal places

        Returns
        -------
        float:rate
            The conversion rate rounded to 4 decimal places
        """

        rounded_rate = round(float(rate), 4)
        self.rate = rounded_rate
        return self.rate
        

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        call function Frankfurter.get_historical_rate and give the relevant parameters from the class and save it in self.rate
        call the round rate for self.rate
        call reverse_rate and save it in self.inverse_rate

        Returns
        -------
        str:
            relevant message displaying results
        """
        
        rate = self.api.get_historical_rate(self.from_currency, self.to_currency, self.date, self.amount)
        self.rate = self.round_rate(rate)
        self.inverse_rate = self.reverse_rate()
        return print(f"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.rate}. The inverse rate was {self.inverse_rate}")
        