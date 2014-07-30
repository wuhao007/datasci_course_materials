import sys
import json

def hw(sent_file, tweet_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    #print 'Hello, world!'
    tweet_scores = {}
    new_words = []
    for line in tweet_file:
        tweet = json.loads(line) 
        sentiment = 0
        if 'text' in tweet:
            text = tweet['text'].encode('utf-8').lower()
            for word in text.split():
                if word in scores:
                    sentiment += scores[word]
                else:
                    new_words += [word]
            tweet_scores[text] = sentiment
    #print tweet_scores 
    for word in new_words:
        pos = neg = total = 0
        for text in tweet_scores:
            if word in text:
                if tweet_scores[text] > 0:
                    pos += 1
                elif tweet_scores[text] < 0:
                    neg += 1
                total += 1
        print word, ' ', (pos-neg)/total
    #print new_words

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
