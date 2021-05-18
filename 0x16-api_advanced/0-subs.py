#!/usr/bin/python3
"""
Module that create a new functions
"""

import requests
import json

def number_of_subscribers(subreddit):

    resp = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit))
    rspjson = resp.json()
    data = rspjson.get("data")
    return int(data.get('subscribers'))
