'''Get 3200 most recent tweets from a user (max allowed by Twitter API), in
batches of 200. Ignores all tweets starting with "RT" and strips links.
'''

from twython import Twython
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
lis = [695067860435992576] ## Latest starting tweet id
for i in range(0,1):
    user_timeline = twitter.get_user_timeline(screen_name='KimKardashian', count=200,
                                              include_retweets=False, max_id=lis[-1])
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
                lis.append(tweet['id'])
            except UnicodeEncodeError:
                pass
    #time.sleep(301) ## 5 minutes betwen api calls
