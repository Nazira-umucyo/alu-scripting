#!/usr/bin/python3
"""
Fetch and print the titles of the first 10 hot posts
from a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a subreddit.
    If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:reddit.api.advanced:v1.0.0 (by /u/student)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                              allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        print(None)
