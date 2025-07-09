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
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:reddit.api.advanced:v1.0.0 (by /u/student)"
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                
                for post in posts[:10]:
                    if 'data' in post and 'title' in post['data']:
                        print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)
            
    except Exception:
        print(None)
