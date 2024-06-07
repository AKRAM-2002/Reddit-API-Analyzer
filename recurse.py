#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:RedditAPIAnalyzer:v1.0 (by /u/yourusername)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get('data', {})
        after = data.get('after')
        posts = data.get('children', [])
        
        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))
        
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
