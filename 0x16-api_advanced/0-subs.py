#!/usr/bin/python3

"""
Fetch and manipulate data from the reddit API.
Function retrives number of subscribers of a given subreddit

Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests, ensure you’re setting
a custom User-Agent.

Requirements:

Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.

"""

import praw


def number_of_subscribers(subreddit):
    """
    Fetch the total number of subscribers of a given subreddit

    Args:
        subreddit (obj) - instance of the reddit api object obtined from praw

    Return:
        Number of subscribers of the given subreddit else return 0
    """

    reddit = praw.Reddit(client_id="o5LcaoRyV02tUzF9tZZ7Xg",
                         client_secret="Pzt78Mz5WZR6AMpfEJsOtmuZJS30rA",
                         user_agent="myRedditScript/v1.0 (by /u/Eric)")

    subreddit = reddit.subreddit(subreddit)

    try:
        return subreddit.subscribers

    except Exception:
        return 0
