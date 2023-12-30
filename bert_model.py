from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import mysql.connector

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def sentiment_score(review):
    tokens = tokenizer.encode(review,return_tensors='pt')
    result= model(tokens)
    return int(torch.argmax(result.logits))+1

# Function to get user review and provide a suitable reply

sentiment = 0.00
def review(msg,ref1):
    # Perform sentiment analysis
    sentiment = sentiment_score(msg)
    conn = mysql.connector.connect(host="localhost", username="root", password="mymysqlZ666#", database="cmdet")
    cmdet_cursor = conn.cursor()
    cmdet_cursor.execute("update restcdata set rev_score=%s where ref_no=%s", (sentiment, ref1))
    conn.commit()
    conn.close()
    # Provide suitable reply based on sentiment
    if sentiment > 3:
        return "Thank you for your positive review! \nWe thrive to put a smile on your face. \nPlease visit again !!"
    else:
        return "We are sorry to hear that!! \nYour feedback is valuable to us. \nWe will try to better our services"

