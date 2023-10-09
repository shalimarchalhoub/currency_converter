from ast import arg
from locale import currency
from subprocess import call
import sys
from api import call_get
from frankfurter import Frankfurter
from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":
    """
    Main logics of the program.

    Pseudo-code
    ----------
    Extract the input arguments
    Remove the first argument (name of Python script)
    Check there are 3 items in the remaining list of argument (using your defined check_arguments() function)
    Check the validity of the input date (using your defined check_date() function)
    Instantiate an objet from your defined CurrencyConverter class with the verified 2 currency codes and date
    Check the validity of the 2 currency codes (using your defined check_currencies() method from CurrencyConverter class)
    Extract the historical rate and calculate its inverse rate (using your defined get_historical_rate() method from CurrencyConverter class)
    """

    args = sys.argv[1:]
    check_arguments(args)
    check_date(args[0])
    
    from_currency = args[1]
    to_currency = args[2]
    date = args [0]

    currency_conv = CurrencyConverter(from_currency, to_currency, date)
    currency_conv.from_currency= args[1]
    currency_conv.to_currency= args[2]
    currency_conv.date = args[0]
    currency_conv.amount = 1

    currency_conv.check_currencies()    
    currency_conv.get_historical_rate()


    
    