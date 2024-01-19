#!/usr/bin/python3


"""
Fetch and manipulate data from the reddit API.
Function retrives number of subscribers of a given subreddit
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
