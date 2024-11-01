First tests and experimenting with LLMs and NLP.

Project 1) 
Revolut Youtube sentiment: Here I scraped all of the comments from the 10 7 videos on Youtube about Revolut from Finfluencers. 
The from the 7 videos I pulled 269 comments for analysis.
![output](https://github.com/user-attachments/assets/061c0a32-7d93-4636-b389-59fe7e27ecf8)

Result: 
Using polarity scores and older NLP methods yielded more neutral and negative sentiment. 
![Polarity_barchart](https://github.com/user-attachments/assets/4203f232-1e0d-4096-89a5-d3c8238c2462)

Using a modern LLM (roBERTa), trained on 126M tweets picked up 50 more Negative comments and
![roBERTa_barchart](https://github.com/user-attachments/assets/c4ba2b91-c5a7-4673-b65a-224eae4d628f)

