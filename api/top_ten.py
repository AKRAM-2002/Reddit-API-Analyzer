#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python:RedditAPIAnalyzer:v1.0 (by /u/yourusername)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    post_titles = []

    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
            post_titles.append(post.get('data').get('title'))
        return post_titles
    else:
        return 0
