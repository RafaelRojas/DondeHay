#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tweepy
import csv
import json
import re

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

hashtags = ['DesabastoGDL', 'GasolinaGDL']

for hashtag in hashtags:
	for tweet in tweepy.Cursor(api.search, q='#' + hashtag, rpp=100).items(maximum_number_of_tweets_to_be_extracted):
		with open('tweets' + '.txt', 'a') as the_file:
			the_file.write(str(tweet.text.encode('utf-8')) + '\n')
	print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) + ' tweets with hashtag #' + hashtag)


def search (search_string):
	for line in open("tweets.txt"):
		#if "search_string" in line:
		#	print (line)
		if re.search(search_string):
			print (line)
search('margarita')

