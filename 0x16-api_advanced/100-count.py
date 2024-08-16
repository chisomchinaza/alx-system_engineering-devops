#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given
keywords (case-insensitive).
"""

import re
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The 'after' parameter for pagination.
        word_count (Counter): A Counter object to store keyword counts.

    Returns:
        None
    """
    if word_count is None:
        word_count = Counter()

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my_custom_user_agent"}
    params = {"after": after}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json().get("data", {})
            after = data.get("after")
            children = data.get("children", [])
            titles = [
                child.get("data", {}).get("title", "").lower()
                for child in children
            ]

            for title in titles:
                for word in word_list:
                    # Create regex pattern to match exact keywords
                    pattern = r'\b{}\b'.format(re.escape(word.lower()))
                    word_count[word.lower()] += len(re.findall(pattern, title))

            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_words = sorted(
                    word_count.items(),
                    key=lambda x: (-x[1], x[0])
                )
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")

    except requests.RequestException:
        return
