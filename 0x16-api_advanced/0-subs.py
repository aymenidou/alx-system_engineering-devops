#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'custom_user_agent'}

    response = requests.get(url, headers=headers)
    data = response.json()

    subscribers = data.get('data', {}).get('subscribers', 0)
    return subscribers
