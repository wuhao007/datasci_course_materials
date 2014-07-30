import sys
import json

def hw(sent_file, tweet_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    #print 'Hello, world!'
    for line in tweet_file:
        tweet = json.loads(line) 
        sentiment = 0
        if 'text' in tweet:
            text = tweet['text'].encode('utf-8').lower()
            for word in text.split():
                if word in scores:
                    sentiment += scores[word]
            print sentiment

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
