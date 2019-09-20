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
        pass


def count_words(subreddit, word_list, lista=None, dicty={}):
    """Get number of subscribers"""

    if dicty == {}:
        for word in word_list:
            dicty.update({word: 0})
    if lista is None:
        lista = recurse(subreddit)
    if lista and len(lista) > 0:
        if word_list != []:
            word_list = list(set(word_list))
            for item in lista:
                item = item.lower()
                if word_list[-1].lower() in item.split():
                    if word_list[-1] in dicty.keys():
                        dicty[word_list[-1]] += 1
            word_list.pop(-1)
            count_words(subreddit, word_list, lista, dicty)
        else:
            for key in sorted(dicty.items(), key=lambda kv: (-kv[1], kv[0])):
                if key[1] != 0:
                    print("{}: {}".format(key[0], key[1]))
