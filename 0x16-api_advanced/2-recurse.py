#!/usr/bin/python3
import requests as r
"""count number of subscribers"""


def recurse(subreddit, hot_list=[], after="null"):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}.json?sort=hot&after={}".format(
        subreddit, after)
    headers = {'User-Agent': 'Yesid'}
    try:
        subscribers = r.get(url, headers=headers,
                            allow_redirects=False).json()
        data = subscribers.get("data")
        after = subscribers.get("data").get("after")
        hot_list += [story.get("data")['title'] for story in data['children']]
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    except:
        return None
