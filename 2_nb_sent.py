import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from spellchecker import SpellChecker

rev=pd.read_csv('Restaurant_Reviews.tsv',delimiter='\t',quoting=3)

print(rev.iloc[0,0]) # checking one record

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


cv=CountVectorizer(max_features=1500)
X=cv.fit_transform(corpus).toarray()
y=rev.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=.2,random_state=0)

from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)


from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
acc=accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc*100}%")

# Calculate additional performance metrics
# Calculate additional performance metrics for both positive and negative reviews separately
from sklearn.metrics import precision_score, recall_score, f1_score

# Metrics for positive reviews (class 1)
precision_pos = precision_score(y_test, y_pred, pos_label=1)
recall_pos = recall_score(y_test, y_pred, pos_label=1)
f1_pos = f1_score(y_test, y_pred, pos_label=1)

# Metrics for negative reviews (class 0)
precision_neg = precision_score(y_test, y_pred, pos_label=0)
recall_neg = recall_score(y_test, y_pred, pos_label=0)
f1_neg = f1_score(y_test, y_pred, pos_label=0)

# Print additional metrics
print("\nMetrics for Positive Reviews (Class 1):")
print(f"Precision: {precision_pos:.2f}")
print(f"Recall: {recall_pos:.2f}")
print(f"F1 Score: {f1_pos:.2f}")

print("\nMetrics for Negative Reviews (Class 0):")
print(f"Precision: {precision_neg:.2f}")
print(f"Recall: {recall_neg:.2f}")
print(f"F1 Score: {f1_neg:.2f}")

new_rev='just awesome'
new_rev=re.sub('[^a-zA-Z]',' ',new_rev)
new_rev=new_rev.lower()
new_rev=new_rev.split()
ps=PorterStemmer()
stpwor= stopwords.words('english')
stpwor.remove('not')
new_rev=[ps.stem(word) for word in new_rev if not word in set(stpwor)]
new_rev = ' '.join(new_rev)
new_corpus=[new_rev]
new_X_test=cv.transform(new_corpus).toarray()
new_y_pred=classifier.predict(new_X_test)
print(new_y_pred)