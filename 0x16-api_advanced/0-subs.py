#!/usr/bin/python3
"""module fetching data from reddit api"""
from requests import get


def number_of_subscribers(subreddit):
    """fetch subressit subscribers"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'custom_user_agent'}

    try:
        res = get(url, headers=headers)
        if res.status_code == 200:
            js = res.json()
            data = js.get("data")
            sub_count = data.get("subscribers")
            return sub_count
        else:
            return 0
    except ValueError:
        return 0
