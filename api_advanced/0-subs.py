#!/usr/bin/python3
"""
Module to query the number of subscribers for a subreddit using Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    Returns 0 if subreddit is invalid or request fails.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:sub.counter:v1.0 (by /u/alustudent)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json()["data"]["subscribers"]
        else:
            return 0
    except Exception:
        return 0
