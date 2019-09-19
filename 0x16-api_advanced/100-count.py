#!/usr/bin/python3
import requests as r
"""count number of subscribers"""


def recurse(subreddit, hot_list=[], after="null"):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}.json?sort=hot&after={}&limit=100"\
          .format(subreddit, after)
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


def count_words(subreddit, word_list, lista=[], dicty={}):
    """Get number of subscribers"""

    if lista == []:
        lista = recurse(subreddit)
    count = 0
    if len(word_list) > 0 and lista:
        if word_list[0] in dicty.keys():
            dicty[word_list[0]] = 0
        for item in lista:
            if word_list[0].lower() in item.lower().split():
                if word_list[0] in dicty.keys():
                    count = dicty[word_list[0]]
                count += 1
                dicty[word_list[0]] = count
        word_list.pop(0)
        count_words(subreddit, word_list, lista, dicty)
    else:
        for key in sorted(dicty.items(), key=lambda t: t[::-1], reverse=True):
            print("{}: {}".format(key[0], key[1]))
