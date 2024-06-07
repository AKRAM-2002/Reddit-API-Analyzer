#!/usr/bin/python3
import sys
from subs import number_of_subscribers
from top_ten import top_ten
from recurse import recurse
from count import count_words

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./main.py <task_number> <subreddit> [additional_args]")
    else:
        task = sys.argv[1]
        subreddit = sys.argv[2]
        
        if task == '0':
            print(number_of_subscribers(subreddit))
        elif task == '1':
            top_ten(subreddit)
        elif task == '2':
            hot_list = recurse(subreddit)
            if hot_list:
                print(len(hot_list))
            else:
                print("None")
        elif task == '3':
            if len(sys.argv) < 4:
                print("Usage: ./cmd_main.py 100 <subreddit> <list_of_keywords>")
            else:
                keywords = sys.argv[3].split()
                count_words(subreddit, keywords)
        else:
            print("Invalid task number.")
