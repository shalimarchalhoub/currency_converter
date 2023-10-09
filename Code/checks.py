import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    args: 
        The system arguments that are going to be used 

    Pseudo-code
    ----------
    Check if arguments not equal to 3

    Returns
    -------
    Boolean:
        True: If there are 3 arguments
        Error message If there are more or less than 3 arguments
    """

    if len(args) != 3:
        raise SystemExit("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>") 
    else: return True

def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case. 
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    date: str
        The date when we want the conversion rate from in the format YYYY-MM-DD

    Pseudo-code
    ----------
    Store the date paramter in a variable called inputDate
    Split the given date by the dash symbol "-"
    Check if the date format is correct

    Returns
    -------
    Boolean: True
        if date is valid
    Str:
        relevant error message if date is invalid
    SystemExit:
        Exit if date is invalid
    
    """

    inputDate = date

    isValidDate = True
    try:
        day, month, year = inputDate.split('-')
        datetime.datetime(int(day), int(month), int(year))
    except ValueError:
        isValidDate = False

    if(isValidDate):
        return True
    else:
        raise SystemExit("Provided date is invalid")
        