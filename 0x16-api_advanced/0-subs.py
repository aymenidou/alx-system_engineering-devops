#!/usr/bin/python3
"""module fetching data from reddit api"""
from requests import get


def number_of_subscribers(subreddit):
    """fetch subressit subscribers"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'custom_user_agent'}

    res = get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    try:
        js = res.json()
    except ValueError:
        return 0

    data = js.get("data")
    if data:
        sub_count = data.get("subscribers")
        if sub_count:
            return sub_count
    # subscribers = data.get('data', {}).get('subscribers', 0)
    return 0
