from arguments import args
from analyzer import Analyzer


def sentiment_score(input):
    analyzer = Analyzer(will_train=False, args=args)
    sentiment, percentage = analyzer.classify_sentiment(input)

    return sentiment,percentage
