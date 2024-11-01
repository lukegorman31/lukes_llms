from transformers import pipeline

review = "I love this product, but found the loading times to be a bit slow." 

classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

prediction = classifier(review)

print(prediction)