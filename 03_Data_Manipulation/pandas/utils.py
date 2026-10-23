"""
utils.py: a file that has ready-datasets
"""

import numpy as np
import pandas as pd

#========================
# Sample Data

DRINKS_URL = 'http://bit.ly/drinksbycountry'
MOVIES_URL = 'http://bit.ly/imdbratings'
STOCKS_URL = 'http://bit.ly/smallstocks'
TITANIC_URL = 'http://bit.ly/kaggletrain'
UFO_URL = 'http://bit.ly/uforeports'
ORDERS_URL = 'http://bit.ly/chiporders'        # tab-separated file
USERS_URL = 'http://bit.ly/movieusers'         # pipe-separated file, no header

drinks = pd.read_csv(DRINKS_URL)
movies = pd.read_csv(MOVIES_URL)
stocks = pd.read_csv(STOCKS_URL)
titanic = pd.read_csv(TITANIC_URL)
ufo = pd.read_csv(UFO_URL)
orders = pd.read_table(ORDERS_URL)