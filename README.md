# Currency Coverter using Frankfurt API

## Author
Name: <first and last name> Shalimar Chalhoub

## Description
### Application description
This application takes a date and two currencies and returns the exchange rate from the first currency to the second on that specific date as well as the inverse rate

### Challenges
A few challenges were faced when working on this project some of which were related to calling the API as it needed a specific way to write is and saving the results was also a bit of a challenge.
Another major issue I faced was with exiting when an error occurs, as it kept exiting for the wrong reasons at first

### Future Features and Implementations
For future features, the user can add the exact amount that he wants converted and the program will return that amount.
As for implementations, this program can be used to predict future currency rates.


## How to Setup
The first thing to do is downlaod vidual studio and install python.
After that, load the following packages:
* from ast import arg
* from locale import currency
* from subprocess import call
* import sys
* from api import call_get
* from frankfurter import Frankfurter
* from currency import CurrencyConverter
* from checks import check_arguments, check_date

In the main, call the system arguments and use the check_arguments function to check the length.

After that, use the check_date() function on the first argument and assign all the arguments to variables.

Create a currency converter item and give it those arguments as parameters.

Use the check_currency() function to check that the currencies are valid

The last thing to do is to call the get_historical_rate() function and the code is done.

The python version that was used for this project was 3.10


## How to Run the Program
In order to run in the program, the following command must be written in the terminal

python main.py YYYY-MM-DD from_currency to_currency

A sample command is below

python main.py 2020-02-05 AUD USD 


## Project Structure

This project has the following files:
* api.py: python script that is used to make the API call

* checks.py: python script that will check there are exactly 3 arguments and will check the validity and format of the date argument

* currency.py: python script that has the CurrencyConverter class and is used to check the validity of the currencies as well as extracting currency conversion rate, rounding it and getting the inverse rate

* frankfurter.py: python script that contains the Frankfurter class and gets the currencies list as well as checks if an argument is in the list or not it also calculates the rate and returns the appropriate value.

* main.py: main program used for running your business logics

* test_api.py: python script for testing code from api.py

* test_checks.py: python script for testing code from checks.py
 
* test_currency.py: python script for testing code from currency.py

* test_frankfurter.py: python script for testing code from frankfurter.py
