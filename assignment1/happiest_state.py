import sys
import json
import types

def main():
    words = open(sys.argv[1])
    tweets = open(sys.argv[2])
    scores = {}
    state_scores = {}

    # Create dictionary mapping (term, score)
    for line in words:
        term, score = line.split("\t")
        scores[term] = int(score)

    # Evaluate tweets
    for line in tweets:
        sentiment = 0
        tweet = json.loads(line)
        if 'text' in tweet:
            terms = tweet['text'].lower().encode('utf-8')
            for term in terms.split():
                if scores.has_key(term):
                    sentiment += scores[term]
        if 'place' in tweet and tweet['place'] != None:
            if 'full_name' in tweet['place'] and tweet['place']['full_name'] != None:
                if 'country_code' in tweet['place'] and tweet['place']['country'] != None:
                    if tweet['place']['country'] == 'United States':
                        name_line = tweet['place']['full_name'].encode('utf-8')
                        details = name_line.split()
                        state = details[-1]
                        if len(state) == 2:
                            if state in state_scores:
                                state_scores[state] += sentiment
                            else:
                                state_scores[state] = sentiment

    happiest_state = max(state_scores, key=state_scores.get)
    print happiest_state

if __name__ == '__main__':
    main()
