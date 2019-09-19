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
        if after is not None:
            for story in data['children']:
                storia = story.get("data")
                hot_list += storia['title']
            recurse(subreddit, hot_list, after)
        return hot_list
    except:
        return None
