#!/usr/bin/python3
"""This script gets number of subscribers from a subreddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    headers = {"User-Agent": "aUserAgent"}
    url = "https://www.reddit.com/r/{}/about.json"\
        .format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    status_code = response.status_code
    if status_code != 200:
        return 0
    else:
        response_json = response.json().get('data')
        return response_json.get('subscribers')


# #!/usr/bin/python3
# '''
# Module contains a function that makes an api call
# '''
# import requests


# def number_of_subscribers(subreddit):
#     '''
#     Makes an api call to get the number of subscribers in a given subreddit
#     Args:
#         subreddit(str) - The name of the subreddit to check the no of subs
#     '''
#     url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
#     headers = {'User-Agent': 'aUserAgent'}

#     response = requests.get(url, headers=headers, allow_redirects=False)

#     if response.status_code == 200:
#         return response.json().get('data').get('subscribers')
#     else:
#         return 0
