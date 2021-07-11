"""
Copyright (c) 2021
Author: Kevin Omyonga
"""

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports
import requests

# Local imports
from constants import *

# Append the endpoint to the base URL
MOBILE_MONEY_URL = urljoin(BASE_URL, f"mobile/{CHANNEL}")
TRANSACTION_STATUS_URL = urljoin(BASE_URL, 'transaction/status')

# Request to send money through specified channel
def send_money():
    params = {
        "vid" : VID,
        "reference" : "KOB2CTEST20210711",
        "phone" : PHONE_NUMBER,
        "hash" : SECURITY_KEY,
        "amount" : 500
    }

    # Make request and get response
    response = requests.post(MOBILE_MONEY_URL, json = params)

    # Handle API Error
    if response.status_code != 201:
        raise ApiError(f"POST {MOBILE_MONEY_URL}" " {}".format(response.status_code))

    print('iPay Response Reference {}'.format(response.json()["reference"]))

# Request to retrieve transaction status
def transaction_search():
    params = {
        "vid" : VID,
        "reference" : "KOB2CTEST20210711",
        "hash" : SECURITY_KEY,
    }

    # Make request and get response
    response = requests.post(TRANSACTION_STATUS_URL, json = params)

    # Handle API Error
    if response.status_code != 201:
        raise ApiError(f"POST {TRANSACTION_STATUS_URL}"" {}".format(response.status_code))

    print('iPay Transaction {}'.format(response.json()))

