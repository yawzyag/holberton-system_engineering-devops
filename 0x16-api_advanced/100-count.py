#!/usr/bin/python3
import requests as r
"""count number of subscribers"""


def count_words(subreddit, word_list, lista=[], after="null"):
    """Get number of subscribers"""

    url = "https://www.reddit.com/r/{}.json?sort=hot&after={}&limit=100"\
        .format(subreddit, after)
    headers = {'User-Agent': 'Yesid'}
    subscribers = r.get(url, headers=headers,
                        allow_redirects=False).json()
    data = subscribers.get("data")
    after = subscribers.get("data").get("after")
    lista += [story.get("data")['title'] for story in data['children']]
    if after is not None:
        count_words(subreddit, word_list, lista, after)
    if after is None:
        count, dicty = 0, {}
        word_list = list(set(word_list))
        for item in lista:
            for word in word_list:
                if word.lower() in item.lower().split():
                    if word in dicty.keys():
                        count = dicty[word]
                    count += 1
                    dicty.update({word: count})
        for key in sorted(dicty.items(), key=lambda kv: (-kv[1], kv[0])):
            print("{}: {}".format(key[0], key[1]))
