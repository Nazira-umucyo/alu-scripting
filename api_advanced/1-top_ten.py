#!/usr/bin/python3
"""Fetches and prints the first 10 hot posts of a given subreddit."""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints titles of the first 10 hot posts.
    Prints None if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; RedditScraper/1.0; +https://www.example.com/bot)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {}).get("children", [])
        if not data:
            print("None")
            return

        for post in data:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
