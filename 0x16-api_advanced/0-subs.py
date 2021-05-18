#!/usr/bin/python3
"""
Module that create a new functions
"""

import requests


def number_of_subscribers(subreddit):
    """ Function to get the numbers os subscribers """

    agent = {"user-agent": 'Juan/007'}
    url = 'https://www.reddit.com'
    resp = (requests.get('{}/r/{}/about.json'.format(url, subreddit),
            headers=agent, allow_redirects=False))
    if resp.status_code != 200:
        return 0
    rspjson = resp.json()
    if rspjson:
        data = rspjson.get('data')
        if data:
            return data.get('subscribers')
    return 0
