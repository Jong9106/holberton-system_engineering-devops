#!/usr/bin/python3
"""
Module that create a new functions
"""

import requests
import json


def number_of_subscribers(subreddit):
    """ Function to get the numbers os subscribers """

    url = 'https://www.reddit.com'
    resp = requests.get('{}/r/{}/about.json'.format(url, subreddit))
    rspjson = resp.json()
    data = rspjson.get("data")
    return int(data.get('subscribers'))
