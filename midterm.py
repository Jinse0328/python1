import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
text1 = "I like a dog"
text2 = "I hate a bird"
text3 = "This is a midterm project"
a = SentimentIntensityAnalyzer()

def sentiment(text):
    score = a.polarity_scores(text)
    compound_score = score['compound']

    if compound_score >= 0.01:
        return 'posiive'
    elif compound_score <= -0.01:
        return 'negative'
    else:
        return 'neatural'
    
b = sentiment(text1)
c = sentiment(text2)
d = sentiment(text3)

print(f"The sentiment is {b}")
print(f"The sentiment is {c}")
print(f"The sentiment is {d}")