#!/usr/bin/python3
"""Fetch and print titles of first 10 hot posts from a subreddit."""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:alx.api:v1.0 (by /u/fakeuser)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])

        if not data:
            print(None)
            return

        for post in data:
            print(post["data"]["title"])

    except Exception:
        print(None)
