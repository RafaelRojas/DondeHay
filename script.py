#!/usr/bin/python3

import tweepy


def get_searched_tweets(hashtag):
        """
        Search all tweets for a hashtag
        """
        if self.api is None:
            self._authenticate()

        tweets = []
        if since_id:
            cursor = tweepy.Cursor(self.api.search, q=hashtag, count=100, since_id=since_id)
        else:
            cursor = tweepy.Cursor(self.api.search, q=hashtag, count=100)
        try:
            for item in cursor.items():
                tweets.append(item)
        except tweepy.error.TweepError:
            print("Reached Twitter rate limit")
        return tweets 

hashtag = "DesabastoGDL"
get_searched_tweets(hashtag)
