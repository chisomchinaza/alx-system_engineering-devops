#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for a
given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of
    all hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot posts.
        after (str): The 'after' parameter for pagination.

    Returns:
        list: A list of titles of hot posts or None if the subreddit is invalid
    """
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
            for child in children:
                hot_list.append(
                    child.get("data", {}).get("title", "")
                )
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
