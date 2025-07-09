#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit. Prints nothing if the subreddit is invalid.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alx:0.1 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params,
                                allow_redirects=False,
                                timeout=10)
        if response.status_code != 200:
            # Invalid subreddit: do not print anything
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        # Do nothing on exception as well (silent failure)
        pass
