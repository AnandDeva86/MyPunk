import logging
import requests

# -----------------------------------------------------------
# File name: punk_API.py
# Author: Anand Devarajan
# Date created: 1/04/2022
# Date last modified: 3/04/2022
# Python Version: >3.6
# -----------------------------------------------------------

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class PunkAPI:
    """API to call on the punkapi"""
    def __init__(self):
        self.url = 'https://api.punkapi.com/v2/beers'

    def get_data(self):
        """Calls the punkapi and gets the json data"""
        try:
            response_API = requests.get(f'{self.url}')
            return response_API
        except Exception as e:
            logging.error(f'Error in fetching data: {e}')
            return
