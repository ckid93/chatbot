# transformers module is for our bert model: multilingual uncased sentiment (gives a sentiment score between 1 and 5)
# requests library is to make request to a site to do data scraping
# beautifulsoup helps us to extract the data we actually need
# pandas to structure the data
# numpy gives additional data transformation processes

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd


tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

df = pd.read_csv('Restaurant_Reviews.tsv',delimiter='\t',quoting=3)

def sentiment_score(review):
    tokens = tokenizer.encode(review,return_tensors='pt')
    result= model(tokens)
    return int(torch.argmax(result.logits))+1

#note that the nlp model is limited to 512 tokens
df['Sentiment'] = df['Review'].apply(lambda x:sentiment_score(x[:512]))

# Accuracy of 5 rated reviews by the model
x=df[(df['Sentiment'] == 5) & (df['Liked'] == 0)].shape[0]
y=df[(df['Sentiment'] == 5) & (df['Liked'] == 1)].shape[0]
acc=(y/(x+y))*100
print("Accuracy of reviews rated 5:",acc)

# Accuracy of 4 rated reviews by the model
x=df[(df['Sentiment'] == 4) & (df['Liked'] == 0)].shape[0]
y=df[(df['Sentiment'] == 4) & (df['Liked'] == 1)].shape[0]
acc=(y/(x+y))*100
print("Accuracy of reviews rated 4:",acc)

# Accuracy of 3 rated reviews by the model
x=df[(df['Sentiment'] == 3) & (df['Liked'] == 0)].shape[0]
y=df[(df['Sentiment'] == 3) & (df['Liked'] == 1)].shape[0]
acc=(x/(x+y))*100
print("Accuracy of reviews rated 3:",acc)

# Accuracy of 2 rated reviews by the model
x=df[(df['Sentiment'] == 2) & (df['Liked'] == 0)].shape[0]
y=df[(df['Sentiment'] == 2) & (df['Liked'] == 1)].shape[0]
acc=(x/(x+y))*100
print("Accuracy of reviews rated 2:",acc)

# Accuracy of 1 rated reviews by the model
x=df[(df['Sentiment'] == 1) & (df['Liked'] == 0)].shape[0]
y=df[(df['Sentiment'] == 1) & (df['Liked'] == 1)].shape[0]
acc=(x/(x+y))*100
print("Accuracy of reviews rated 1:",acc)

# Create a function to apply the specified rules
def map_sentiment(sentiment):
    if sentiment in [1, 2, 3]:
        return 0
    elif sentiment in [4, 5]:
        return 1

# Apply the function to create the new column 'sentiment_mod'
df['Sentiment_mod'] = df['Sentiment'].apply(map_sentiment)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Assuming 'Liked' is the true labels (y_test) and 'Sentiment_mod' is the predicted labels (y_pred)
y_test = df['Liked']
y_pred = df['Sentiment_mod']

accuracy = accuracy_score(y_test, y_pred)
# Metrics for Positive Reviews

precision_positive = precision_score(y_test, y_pred, pos_label=1)
recall_positive = recall_score(y_test, y_pred, pos_label=1)
f1_positive = f1_score(y_test, y_pred, pos_label=1)

# Metrics for Negative Reviews

precision_negative = precision_score(y_test, y_pred, pos_label=0)
recall_negative = recall_score(y_test, y_pred, pos_label=0)
f1_negative = f1_score(y_test, y_pred, pos_label=0)


print("Accuracy of Model :", accuracy)

# Print Results for Positive Reviews
print("Metrics for Positive Reviews:")
print("Precision:", precision_positive)
print("Recall:", recall_positive)
print("F1 Score:", f1_positive)


# Print Results for Negative Reviews
print("\nMetrics for Negative Reviews:")
print("Precision:", precision_negative)
print("Recall:", recall_negative)
print("F1 Score:", f1_negative)
