import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

rev=pd.read_csv('Restaurant_Reviews.tsv',delimiter='\t',quoting=3)

print(rev.iloc[0,0])

corpus=[]

for i in range(0,1000):
    revi=re.sub('[^a-zA-Z]',' ',rev['Review'][i])
    revi=revi.lower()
    revi=revi.split()
    ps=PorterStemmer()
    stpwor= stopwords.words('english')
    stpwor.remove('not')
    revi=[ps.stem(word) for word in revi if not word in set(stpwor)]
    revi = ' '.join(revi)
    corpus.append(revi)
    # Initialize the VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    # Perform sentiment analysis on each review in the corpus
    sentiment_scores = []
    for review in corpus:
        sentiment_scores.append(sid.polarity_scores(review))



# Map VADER sentiment scores to positive (1) or negative (0) labels
predicted_labels = [1 if score['compound'] >= 0 else 0 for score in sentiment_scores]

# Get the actual labels from the second column of the rev DataFrame
actual_labels = rev.iloc[:, -1].values

# Compare predicted labels with actual labels
correct_predictions = sum(predicted_labels[i] == actual_labels[i] for i in range(len(actual_labels)))
accuracy = correct_predictions / len(actual_labels)

# Calculate true positives, false positives, false negatives for positive class
true_positives_pos = sum(predicted_labels[i] == 1 and actual_labels[i] == 1 for i in range(len(actual_labels)))
false_positives_pos = sum(predicted_labels[i] == 1 and actual_labels[i] == 0 for i in range(len(actual_labels)))
false_negatives_pos = sum(predicted_labels[i] == 0 and actual_labels[i] == 1 for i in range(len(actual_labels)))

# Calculate true positives, false positives, false negatives for negative class
true_positives_neg = sum(predicted_labels[i] == 0 and actual_labels[i] == 0 for i in range(len(actual_labels)))
false_positives_neg = sum(predicted_labels[i] == 0 and actual_labels[i] == 1 for i in range(len(actual_labels)))
false_negatives_neg = sum(predicted_labels[i] == 1 and actual_labels[i] == 0 for i in range(len(actual_labels)))

# Calculate precision, recall, and F1 score for positive class
precision_pos = true_positives_pos / (true_positives_pos + false_positives_pos) if (true_positives_pos + false_positives_pos) != 0 else 0
recall_pos = true_positives_pos / (true_positives_pos + false_negatives_pos) if (true_positives_pos + false_negatives_pos) != 0 else 0
f1_score_pos = 2 * (precision_pos * recall_pos) / (precision_pos + recall_pos) if (precision_pos + recall_pos) != 0 else 0

# Calculate precision, recall, and F1 score for negative class
precision_neg = true_positives_neg / (true_positives_neg + false_positives_neg) if (true_positives_neg + false_positives_neg) != 0 else 0
recall_neg = true_positives_neg / (true_positives_neg + false_negatives_neg) if (true_positives_neg + false_negatives_neg) != 0 else 0
f1_score_neg = 2 * (precision_neg * recall_neg) / (precision_neg + recall_neg) if (precision_neg + recall_neg) != 0 else 0

# Print the results
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Metrics for Positive Reviews:")
print(f"Precision: {precision_pos:.2f}")
print(f"Recall: {recall_pos:.2f}")
print(f"F1 Score: {f1_score_pos:.2f}")
print("\nMetrics for Negative Reviews:")
print(f"Precision: {precision_neg:.2f}")
print(f"Recall: {recall_neg:.2f}")
print(f"F1 Score: {f1_score_neg:.2f}")