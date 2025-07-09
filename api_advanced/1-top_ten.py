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
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:reddit.api.advanced:v1.0.0 (by /u/student)"}
    params = {"limit": 10}
    
    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code != 200:
            print(None)
            return
        
        data = response.json()
        
        # Check if we got valid subreddit data
        if not data or 'data' not in data or 'children' not in data['data']:
            print(None)
            return
            
        posts = data['data']['children']
        
        # If no posts found, it might be an invalid subreddit
        if not posts:
            print(None)
            return
            
        # Print titles of first 10 posts
        for post in posts[:10]:
            if 'data' in post and 'title' in post['data']:
                title = post['data']['title']
                if title:  # Make sure title is not empty
                    print(title)
                    
    except (requests.exceptions.RequestException, ValueError, KeyError):
        print(None)
