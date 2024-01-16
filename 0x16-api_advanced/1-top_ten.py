#!/usr/bin/python3
"""module fetching data from reddit api"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed
    for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'custom_user_agent'}

    response = requests.get(url, headers=headers)
    data = response.json()

    posts = data['data']['children']
    if not posts:
        print("None")
        return None

    for post in posts:
        title = post['data']['title']
        print(title)
