import pickle
import random

chain = pickle.load(open('../data/chain.p', 'rb'))

def generate_tweet():
    new_tweet = []
    sword1 = 'BEGIN'
    sword2 = 'NOW'

    while True:
        sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        if sword2 == 'END\n':
            break
        new_tweet.append(sword2)

    return ' '.join(new_tweet)

print generate_tweet()
