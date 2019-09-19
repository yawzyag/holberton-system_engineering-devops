#!/usr/bin/python3
import requests as r
"""count number of subscribers"""


def top_ten(subreddit):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}.json?sort=hot&limit=10".format(
        subreddit)
    headers = {'User-Agent': 'Yesid'}
    try:
        subscribers = r.get(url, headers=headers, allow_redirects=False).json()
        data = subscribers.get("data")
        for story in data['children']:
            storia = story.get("data")
            print(storia['title'])
    except:
        print(None)
