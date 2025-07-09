#!/usr/bin/python3
"""
DEBUG version - shows what's happening
"""

import requests


def top_ten(subreddit):
    """
    Debug version to see what's happening
    """
    print(f"DEBUG: Testing subreddit: {subreddit}")
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditApp/0.1"}
    params = {"limit": 10}
    
    print(f"DEBUG: URL: {url}")
    print(f"DEBUG: Headers: {headers}")
    
    try:
        response = requests.get(url, headers=headers, params=params,
                              allow_redirects=False)
        
        print(f"DEBUG: Status code: {response.status_code}")
        print(f"DEBUG: Response headers: {dict(response.headers)}")
        
        if response.status_code != 200:
            print("DEBUG: Non-200 status code")
            print(None)
            return
        
        data = response.json()
        print(f"DEBUG: Response keys: {list(data.keys())}")
        
        if 'data' in data:
            print(f"DEBUG: Data keys: {list(data['data'].keys())}")
            
            if 'children' in data['data']:
                children = data['data']['children']
                print(f"DEBUG: Found {len(children)} posts")
                
                for i, post in enumerate(children[:10]):
                    if 'data' in post and 'title' in post['data']:
                        title = post['data']['title']
                        print(f"DEBUG: Post {i+1}: {title}")
                    else:
                        print(f"DEBUG: Post {i+1}: Missing title data")
            else:
                print("DEBUG: No 'children' in data")
                print(None)
        else:
            print("DEBUG: No 'data' in response")
            print(None)
            
    except Exception as e:
        print(f"DEBUG: Exception: {e}")
        print(None)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
