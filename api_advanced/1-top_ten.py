#!/usr/bin/python3
"""
This module defines a function that prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json().get("data", {}).get("children", [])
        for post in data:
            print(post.get("data", {}).get("title"))
    except Exception:
        return
