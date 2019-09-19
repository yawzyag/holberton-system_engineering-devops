import requests as r
"""count number of subscribers"""


def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Yesid'}
    try:
        subscribers = r.get(url, headers=headers, allow_redirects=False).json()
        data = subscribers.get("data")
        count = data.get("subscribers")
        return count
    except:
        return 0
