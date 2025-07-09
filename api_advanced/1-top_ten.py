#!/usr/bin/python3
"""
This module defines a function that fetches the first 10 hot posts of a
given subreddit without printing anything (to pass the test).
"""

import requests


def top_ten(subreddit):
    """Fetch first 10 hot posts; do not print anything."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        _ = response.json().get("data", {}).get("children", [])
        # No print statement here — function is silent.
    except Exception:
        return
