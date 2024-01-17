#!/usr/bin/python3
"""module fetching data from reddit api"""
import requests


def number_of_subscribers(subreddit):
    """fetch subressit subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'custom_user_agent'}

    data = requests.get(url, headers=headers, allow_redirects=False).json()
    subscribers = data.get('data', {}).get('subscribers', 0)
    return subscribers
