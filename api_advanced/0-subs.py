#!/usr/bin/python3
"""
0-subs module

This module contains a function to query the Reddit API and retrieve
the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers for the subreddit,
             or 0 if the subreddit is invalid or the request fails.
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
