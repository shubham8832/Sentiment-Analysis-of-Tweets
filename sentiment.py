import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

df = pd.read_csv("tweets.csv")

print("Original Data:")
print(df.head(5))

sia = SentimentIntensityAnalyzer()

df['score'] = df['text'].apply(lambda x: sia.polarity_scores(x)['compound'])

def get_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df['sentiment'] = df['score'].apply(get_sentiment)

print("\nProcessed Data:")
print(df)

df.to_csv("output.csv", index=False)
print("\nOutput saved as output.csv")

sentiment_counts = df['sentiment'].value_counts()

plt.figure(figsize=(8, 5))

bars = plt.bar(sentiment_counts.index, sentiment_counts.values)

plt.title("Sentiment Analysis Overview", fontsize=14, fontweight='bold')
plt.xlabel("Sentiment", fontsize=12)
plt.ylabel("Number of Tweets", fontsize=12)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             str(int(height)),
             ha='center', va='bottom', fontsize=11)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()



plt.figure(figsize=(6, 6))

plt.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    autopct='%1.1f%%',
    startangle=140
)

plt.title("Sentiment Distribution", fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()