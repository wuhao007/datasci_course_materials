import sys
import json
import types
import operator

def main():
    tweets = open(sys.argv[1])
    hashtag_count = {}
    top = 10

    # Evaluate tweets
    for line in tweets:
        tweet = json.loads(line)
        if 'entities' in tweet and tweet['entities'] != None:
            if 'hashtags' in tweet['entities'] and tweet['entities']['hashtags'] != None:
                hashtags = tweet['entities']['hashtags']
                for hashtag in hashtags:
                    tag = hashtag['text'].encode('utf-8')
                    if hashtag_count.has_key(tag):
                        hashtag_count[tag] += 1
                    else:
                        hashtag_count[tag] = 1

    # Compute top ten hashtags
    for x in sorted(hashtag_count, key=hashtag_count.get)[-1:-top-1:-1]:
        print x + ' ' + str(hashtag_count[x])

if __name__ == '__main__':
    main()
