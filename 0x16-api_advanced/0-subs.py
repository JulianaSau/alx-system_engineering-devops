#!/usr/bin/python3
'''
Module contains a function that makes an api call
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Makes an api call to get the number of subscribers in a given subreddit
    Args:
        subreddit(str) - The name of the subreddit to check the no of subs
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'aUserAgent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
