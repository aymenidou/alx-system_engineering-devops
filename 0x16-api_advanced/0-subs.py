#!/usr/bin/python3
"""module fetching data from reddit api"""
from requests import get


def number_of_subscribers(subreddit):
    """fetch subressit subscribers"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'custom_user_agent'}

    try:
        res = get(url, headers=headers, allow_redirects=False)
        res.raise_for_status()
        js = res.json()
        if js.get("data", {}).get("subscribers") is not None:
            return js["data"]["subscribers"]
        else:
            return 0
    except ValueError:
        return 0
