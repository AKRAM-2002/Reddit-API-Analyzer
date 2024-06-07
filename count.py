#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, counts={} ):
    
    if not word_list or word_list == [] or not subreddit:
        return 
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    params=  {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    results = response.json().get("data")
    children = results.get("children")

    for child in children:
        title = child.get("data").get("title").lower()
        for word in word_list:
            if word.lower() in title:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
    after = results.get('data', {}).get('after')

    if after:
        return count_words(subreddit, word_list, after, counts)

    else:
        sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_words:
            print("{}: {}".format(word, count))
        return sorted_words
