#!/usr/bin/python3
"""Module that sends requests to the reddit API
"""

import requests


def count_words(subreddit, word_list):
    """Sends a request to the reddit api and returns a list of all hot
    aricles of a specific subreddit
    """

    after = ""
    count = ""
    metadata = subreddit.split()
    if len(metadata) > 1:
        if metadata[0] is not None and metadata[0].startswith("t3_"):
            after = "&after={}".format(metadata[0])
            subreddit = metadata[1]
        else:
            return None

    if len(hot_list) > 0:
        count = "&count={}".format(len(hot_list))

    url = "https://www.reddit.com/r/{}/hot.json?limit=100{}{}".format(
            subreddit, after, count
            )
    headers = {"User-Agent": "aUserAgent"}
    posts_titles = []

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return None
    else:
        json = res.json()
        posts = json["data"]["children"]
        next_page = json["data"]["after"]
        metadata = "{} {}".format(next_page, subreddit)
        for post in posts:
            posts_titles.append(post["data"]["title"])
        hot_list = hot_list + posts_titles
        lst = recurse(metadata, hot_list)

    return hot_list

def recurse(subreddit, hot_list=[], after=None):
    '''
    Makes an api call to get the top ten hot posts in a given subreddit
    Args:
        subreddit(str) - The name of the subreddit to check
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    data = requests.get(url, headers={'User-agent': 'my-bot'},
                        params={'after': after}, allow_redirects=False)

    if data.status_code == 200:
        after = data.json().get('data').get('after')
        post_list = data.json().get('data').get('children')

        for post in post_list:
            hot_list.append(post.get("data").get("title"))

        if after is None:
            # If there is no new page
            if len(hot_list) == 0:
                return None

            return hot_list
        else:
            # If there is another page
            return recurse(subreddit, hot_list, after)
    else:
        return None