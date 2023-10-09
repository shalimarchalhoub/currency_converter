import requests
import sys

def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    url: str
        The URL of the endpoint we are going to call

    Pseudo-code
    ----------
    Get request of the specified url and save it in response
    if response status = 200 then return response
    if response status != 200, print error message

    Returns
    ------- 
    requests.models.Response
        Response from API request
    Str:
        Relevant string message
    Sys: 
        Exit code
    
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        raise SystemExit("There is an error with Frankfurter API")





