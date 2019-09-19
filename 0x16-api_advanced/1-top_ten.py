import requests as r
"""count number of subscribers"""


def top_ten(subreddit):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Yesid'}
    subscribers = r.get(url, headers=headers).json()
    try:
        for story in subscribers['data']['children']:
            print(story['data']['title'])
    except:
        print(None)
