#!/usr/bin/python3
"""Fetch and print the titles of the first 10 hot posts from a subreddit."""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.
    If subreddit is invalid or inaccessible, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "CustomUserAgent/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post["data"]["title"])
    except Exception:
        print("None")
