#!/usr/bin/python3
"""
Module to print titles of the first 10 hot posts of a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    If subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Python3:api_advanced:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
