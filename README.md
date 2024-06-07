# Reddit API Analyzer

This project is a web application that interacts with the Reddit API to provide various analytical tasks. Users can input a subreddit and select a task to get the number of subscribers, top ten posts, all hot post titles, or count specific keywords in hot post titles. The application is built using Flask for the web interface and Python for interacting with the Reddit API.

## Features

- **Number of Subscribers**: Returns the total number of subscribers for a given subreddit.
- **Top Ten Posts**: Displays the titles of the first 10 hot posts listed for a given subreddit.
- **All Hot Posts**: Recursively fetches and displays titles of all hot articles for a given subreddit.
- **Keyword Count**: Counts the occurrences of specific keywords in the titles of hot posts for a given subreddit.

## Requirements

- Python 3.4.3 or later
- Flask
- Requests

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/reddit_api_analyzer.git
   cd reddit_api_analyzer

    ```

2. **Install dependencies:**


## Running the Application:


## Usage:


## Project Structure:
```	bash
reddit_api_analyzer/
├── templates/
│   ├── index.html
│   ├── results.html
├── static/
│   ├── style.css
├── app.py
├── 0-subs.py
├── 1-top_ten.py
├── 2-recurse.py
├── 100-count.py
├── README.md
└── requirements.txt
```

### Explanation of Files

- app.py: The main Flask application file that defines routes and handles requests.
- 0-subs.py: Script to get the number of subscribers for a subreddit.
- 1-top_ten.py: Script to get the top ten hot posts for a subreddit.
- 2-recurse.py: Script to get all hot posts for a subreddit recursively.
- 100-count.py: Script to count occurrences of specific keywords in hot posts for a subreddit.
- templates/: Directory containing HTML templates for the web pages.
    - index.html: The main page where users can input the subreddit and select tasks.
    - results.html: The page to display results from the selected task.
- static/: Directory containing static files such as CSS for styling.
    - style.css: The CSS file for styling the web pages.
- requirements.txt: The file listing project dependencies.


### Author
- Akram Boutzouga
