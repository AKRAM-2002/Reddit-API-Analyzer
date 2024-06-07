#!/usr/bin/python3
from flask import Flask, request, render_template
from api.subs import number_of_subscribers
from api.top_ten import top_ten
from api.recurse import recurse
from api.count import count_words

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    subreddit = request.form['subreddit']
    task = request.form['task']
    if task == '0':
        subscribers = number_of_subscribers(subreddit)
        return render_template('results.html', result=subscribers, task="Number of Subscribers")
    elif task == '1':
        top_posts = top_ten(subreddit)
        return render_template('results.html', result=top_posts, task="Top Ten Posts")
    elif task == '2':
        hot_list = recurse(subreddit)
        return render_template('results.html', result=hot_list, task="All Hot Posts")
    elif task == '3':
        keywords = request.form['keywords'].split()
        word_counts = count_words(subreddit, keywords)
        return render_template('results.html', result=word_counts, task="Keyword Count")
    else:
        return "Invalid task selected", 400

if __name__ == '__main__':
    app.run(debug=True)
