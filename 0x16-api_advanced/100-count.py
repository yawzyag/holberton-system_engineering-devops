#!/usr/bin/python3
import requests as r
"""count number of subscribers"""


def count_words(subreddit, word_list, lista=[], dicty={}, after="null"):
    """Get number of subscribers"""

    if lista == [] or after is not None:
        url = "https://www.reddit.com/r/{}.json?sort=hot&after={}&limit=100"\
            .format(subreddit, after)
        headers = {'User-Agent': 'Yesid'}
        try:
            subscribers = r.get(url, headers=headers,
                                allow_redirects=False).json()
            data = subscribers.get("data")
            after = subscribers.get("data").get("after")
            lista += [story.get("data")['title'] for story in data['children']]
            if after is not None:
                count_words(subreddit, word_list, lista, dicty, after)
        except:
            return None
    if after is None:
        count = 0
        word_list = list(set(word_list))
        if word_list != [] and lista:
            for item in lista:
                if word_list[0].lower() in item.lower().split():
                    if word_list[0] in dicty.keys():
                        count = dicty[word_list[0]]
                    count += 1
                    dicty[word_list[0]] = count
            word_list.pop(0)
            count_words(subreddit, word_list, lista, dicty, after)
        else:
            for key in sorted(dicty.items(), key=lambda kv: (-kv[1], kv[0])):
                print("{}: {}".format(key[0], key[1]))
