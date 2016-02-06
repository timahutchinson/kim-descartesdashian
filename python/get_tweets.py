'''Get 3200 most recent tweets from a user (max allowed by Twitter API), in
batches of 200. Ignores all tweets starting with "RT" and strips links.
'''

import time
from os.path import exists

from twython import Twython

# Read data/twitter_tokens.txt, and get appropriate tokens out
with open('../data/twitter_tokens.txt') as f:
    tokens = f.readlines()

CONSUMER_KEY = tokens[0].strip('\n')
CONSUMER_SECRET = tokens[1].strip('\n')
ACCESS_KEY = tokens[2].strip('\n')
ACCESS_SECRET = tokens[3].strip('\n')

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# If tweet_id.txt file exists, read tweet_id from it. Otherwise, start from most recent tweet.
if exists('../data/tweet_id.txt'):
    with open('../data/tweet_id.txt') as f:
        tweet_id = eval(f.readlines()[0].strip('\n'))
    user_timeline = twitter.get_user_timeline(screen_name='KimKardashian', count=200,
                                              include_retweets=False, max_id=tweet_id)
else:
    user_timeline = twitter.get_user_timeline(screen_name='KimKardashian', count=200,
                                              include_retweets=False)

for tweet in user_timeline:
    if tweet['text'][:2] != 'RT':
        try:
            this_tweet = tweet['text']

            # Strip links from tweet
            this_tweet = this_tweet.replace('\n', ' ')
            words = this_tweet.split(' ')
            while True:
                if 'http' in ' '.join(words):
                    for word in words:
                        if 'http' in word:
                            words.remove(word)
                else:
                    break

            this_tweet = ' '.join(words)
            if this_tweet == 'Vote for Kanye!!!': import pdb; pdb.set_trace()
            print this_tweet
        except UnicodeEncodeError:
            pass
    tweet_id = tweet['id']

with open('../data/tweet_id.txt', 'w') as f:
    f.write(repr(tweet_id))
