import pandas as pd
import seaborn as sns
import matplotlib as plt
from textblob import TextBlob

data = {
    'video_id': ['7MAJfcG8B7E', '7MAJfcG8B7E', '7MAJfcG8B7E', '7MAJfcG8B7E', '7MAJfcG8B7E'],
    'comment': [
        "i can clearly see that revolut paid you. lol",
        "what is the value of 10k points in euros ?",
        "using the ultra plan, if you pay via your revo...",
        "spare change is scam! i have spent 130£ witho...",
        "i just noticed i spent 280 euros in the last 0..."
    ],
    'month': [11, 11, 11, 10, 10],
    'year': [2024, 2024, 2024, 2024, 2024]
}

df = pd.DataFrame(data)


def add_polarity(df):
    polarity = []
    for i in df['comment']:
        if isinstance(i, str):  # Ensure it's a string
            blob = TextBlob(i)
            polarity.append(round(blob.sentiment.polarity, 3))
        else:
            polarity.append(0)  # Default polarity for non-string comments
    df['polarity'] = polarity
    print('Polarity Column added to the dataframe')

    return df

def sentiment(df):
    sentiment = []
    for i in df['polarity']:
        if i > 0:
            sentiment.append('positive')
        elif i < 0:
            sentiment.append('negative')
        else:
            sentiment.append('neutral')

    df['NLP_sentiment'] = sentiment

    return df

