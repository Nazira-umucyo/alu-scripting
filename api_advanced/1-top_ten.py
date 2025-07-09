#!/usr/bin/python3
"""
Fetch and print the titles of the first 10 hot posts from a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "MyRedditClient/1.0"
    }
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])

    if not posts:
        print("None")
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
