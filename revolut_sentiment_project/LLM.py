from transformers import AutoTokenizer, AutoConfig, AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np
import pandas as pd

MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# No preprocessing needed
def get_sentiment(text):
    try:
        # Print the comment being processed for debugging
        print(f"Processing comment: {text}")
        
        encoded_input = tokenizer(text, return_tensors='pt', truncation=True, padding='max_length', max_length=512)
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        
        top_label = config.id2label[ranking[0]]
        top_score = np.round(float(scores[ranking[0]]), 4)
        
        # Print the result for debugging
        print(f"Sentiment: {top_label}, Score: {top_score}")
        
        return top_label, top_score
    except Exception as e:
        # Print the error for debugging
        print(f"Error processing comment: {text}\nError: {e}")
        return None, None

