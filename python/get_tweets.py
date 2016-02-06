'''Get 3200 most recent tweets from a user (max allowed by Twitter API), in
batches of 200. Ignores all tweets starting with "RT" and strips links.
'''

from twython import Twython
import time

# Read data/twitter_tokens.txt, and get appropriate tokens out
with open('../data/twitter_tokens.txt') as f:
    tokens = f.readlines()

# Read data/tweet_id.txt to get id of most recent tweet
with open('../data/tweet_id.txt') as f:
    tweet_id = eval(f.readlines()[0].strip('\n'))

CONSUMER_KEY = tokens[0].strip('\n')
CONSUMER_SECRET = tokens[1].strip('\n')
ACCESS_KEY = tokens[2].strip('\n')
ACCESS_SECRET = tokens[3].strip('\n')

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
user_timeline = twitter.get_user_timeline(screen_name='KimKardashian', count=200,
                                          include_retweets=False, max_id=tweet_id)
for tweet in user_timeline:
    if tweet['text'][:2] != 'RT':
        try:
            this_tweet = tweet['text']

            # Strip links from tweet
            words = this_tweet.split(' ')
            while True:
                if 'http' in ' '.join(words):
                    for word in words:
                        if word[:4] == 'http':
                            words.remove(word)
                else:
                    break

            this_tweet = ' '.join(words)
            print this_tweet
        except UnicodeEncodeError:
            pass
    tweet_id = tweet['id']

with open('../data/tweet_id.txt', 'w') as f:
    f.write(repr(tweet_id))
