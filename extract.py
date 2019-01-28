#!/usr/bin/python3

import tweepy
import csv
import json
import argparse, sys, re
from datetime import datetime


parser = argparse.ArgumentParser(description='Twitter scrapper to find gas stations')
parser.add_argument('--hashtags', '-ht', nargs='+', help='the hashtags to look on') 
parser.add_argument('--keywords', '-kw', nargs='+', help='the keywords to search for')
parser.add_argument('--version', '-v', action='version', version='%(prog)s verison 1.0')

args = parser.parse_args()

# Twitter API credentials

with open('twitter_credentials.json') as cred_data:
	info = json.load(cred_data)
	consumer_key = info['CONSUMER_KEY']
	consumer_secret = info['CONSUMER_SECRET']
	access_key = info['ACCESS_KEY']
	access_secret = info['ACCESS_SECRET']

# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# The maximum number of tweets that you want to be extracted.

maximum_number_of_tweets_to_be_extracted = 300

hashtags = parser.parse_args().hashtags
keywords = parser.parse_args().keywords
def get_searched_tweets(hashtag):
    tweets = []
    tweets = (tweepy.Cursor(api.search, q= '#' + hashtag + '-filter:retweets').items(maximum_number_of_tweets_to_be_extracted))
    
    for cursor in  tweets:
        try:
            with open('tweets' + '.txt', 'a') as the_file:
                the_file.write(datetime.strftime(cursor.created_at, '%m/%d/%y %H:%M:%S') + str(cursor.text) + '\n')
        except tweepy.error.TweepError:
         	    print("Reached Twitter rate limit")
    return hashtag


def search_keywords(keyword):
    with open('tweets.txt', 'r') as tweets:
        #readtweets = tweets.read()
        if re.findall(keyword, tweets.read()):
            print(str(tweets.text))

    #for tweet in readtweets:
    #    re.sub("[a-zA-Z]", "", str(keyword))
    #    re.sub("[a-zA-Z]", "", str(tweet))      
    #    if re.search(keyword, tweet):
    #        print(str(tweet))
        #finding = re.findall(r'[A-Z][a-z]*', keyword)
        #print(str(finding))
    return finding

for hashtag in hashtags:
    get_searched_tweets(hashtag)
    print('Getting tweets with hashtag ' + hashtag)


for keyword in keywords:
    with open("tweets.txt") as origin_file:
        for line in origin_file:
            line = re.findall(r'(.+)'+keyword+'(.+)', line)
            if line:
               #line = line[0].split('"')[1]
               print(line)




#def search_pattern(findings):
#    tweets = (hashtag)
#    print(tweets)
#    return findings

#search_pattern(findings)
