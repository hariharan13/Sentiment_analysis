#import all libraries needed for performing sentiment analysis
import nltk
import nltk.sentiment.util
import nltk.sentiment.sentiment_analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def mySentimentAnalyzer():
#This instruction defines a new subfunction, score_feedback(), which takes a sentence as input and returns the score for the sentence in terms of
#-1 negative, 0 neutral, and 1 positive
    def score_feedback(text):
        positive_words = ['love', 'genuine', 'liked']
        if '_NEG' in ' '.join(nltk.sentiment.util.mark_negation(text.split())):
            score = -1
        else:
            analysis = nltk.sentiment.util.extract_unigram_feats(text.split(), positive_words)
            if True in analysis.values():
                score = 1
            else:
                score = 0
       return score
#These are the four reviews that we are interested in processing using our algorithm to print the score.    
    feedback = """I love the items in this shop, very genuine and quality is well maintained.
    I have visited this shop and had samosa, my friends liked it very much.
    ok average food in this shop.
    Fridays are very busy in this shop, do not place orders during this day."""
    print(' -- custom scorer --')
    for text in feedback.split("\n"):
        print("score = {} for >> {}".format(score_feedback(text), text))
def advancedSentimentAnalyzer():
    sentences = [
        ':)',
        ':(',
        'She is so :(',
        'I love the way cricket is played by the champions',
        'She neither likes coffee nor tea',
    ]
    senti = SentimentIntensityAnalyzer()
#Iterate over all the sentences and store the current one in the variable sentence
#Invoke the polarity_scores() function on this sentence; store the result in a variable called kvp
#Traverse through the dictionary kvp and print the key (negativity, neutral, positivity, or compound types) and the score computed for these types
  print(' -- built-in intensity analyser --')
    for sentence in sentences:
        print('[{}]'.format(sentence), end=' --> ')
        kvp = senti.polarity_scores(sentence)
        for k in kvp:
            print('{} = {}, '.format(k, kvp[k]), end='')
        print()        
advancedSentimentAnalyzer()
mySentimentAnalyzer()
