#common/api_client.py

import requests
from config.settings import *

def _headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }

def get(url,params=None,token=None):
    return requests.get(url,params=params,headers=_headers(token),timeout=TIMEOUT)
def post(url,json=None,token=None):
    return requests.post(url,json=json,headers=_headers(token),timeout=TIMEOUT)
def delete(url,token=None):
    return requests.delete(url,headers=_headers(token),timeout=TIMEOUT)