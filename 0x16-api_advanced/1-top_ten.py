#!/usr/bin/python3
"""module fetching data from reddit api"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed
    for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'custom_user_agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return None

    try:
        js = response.json()
    except ValueError:
        print(None)
        return None

    try:
        data = js.get('data')
        posts = data.get('children')
        for post in posts:
            title = post.get('data')
            print(title.get("title"))
    except:
        print(None)
