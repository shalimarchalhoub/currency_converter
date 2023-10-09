from pickle import TRUE
from api import call_get

class Frankfurter:
    """ 
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """
    def __init__(self):
        self.base_url = "https://api.frankfurter.app/"
        self.currencies_url = "currencies"
        self.historical_url = None
        self.currencies = [list]

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        Define the endpoint by combining base_url and currencies_url
        Call the end point and save it in response as json
        Create the currencies list 

        Returns
        -------
        list:
            Currencies list 

        """ 
        
        endpoint = self.base_url + self.currencies_url
        self.currencies = (call_get(endpoint).json())
        return list(self.currencies)

        

    def check_currency(self, currency : str):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

        Parameters
        ----------
        Str:
            Provided currency code to check

        Pseudo-code
        ----------
        Does an if function to check if the given currency is in the currencies list by calling
        get_currencies_list() function

        Returns
        -------
        Boolean:
            True if Currency is in currencies list
            False if Currency is not in currencies list

        """
        
        if currency in self.get_currencies_list():
            return True
        else:
            return False
        
        

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.

        Parameters
        ----------
        Str: from_currency
            The currency to convert from
        Str: to_currency
            The currency to convert to
        Str: from_date
            The historical date to get the rate from
        Int: amount
            Amount =1

        Pseudo-code
        ----------
        combine base_url with the from_date, from_currecy and to_currency in relevant code
        save code in self.historical_url
        call the call_get function on self.historical_usl and save it in rate_response as json file
        convert the rates_list to a list for the attribute rates
        take the first argument from the rates_list and save it in rate
        
        Returns
        -------
        float: rate
            conversion rate on a given date and currencies
            
        """
        self.historical_url = (self.base_url + from_date + "?from=" + from_currency + "&to=" + to_currency)
        rate_response = call_get(self.historical_url).json()
        rates_list = list(rate_response['rates'].values())
        rate = rates_list[0]
        return rate
        
        
 