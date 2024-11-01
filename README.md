First tests and experimenting with LLMs and NLP.

Project 1) 

Revolut Youtube sentiment: Here I scraped all of the comments from the top 7 videos on Youtube about Revolut from Finfluencers. 
The from the 7 videos I pulled 279 comments for analysis.

![output](https://github.com/user-attachments/assets/061c0a32-7d93-4636-b389-59fe7e27ecf8)

Result: 
Using polarity scores and older NLP methods yielded moslty Positive sentiment. 

![sentiment-polarity](https://github.com/user-attachments/assets/9f730222-2eda-4300-aae5-1aba7eb1e0db)


Using a modern LLM (roBERTa), trained on 126M tweets picked up 50 more Negative comments with neutral comments being most dominant

![roBERTa_barchart](https://github.com/user-attachments/assets/c4ba2b91-c5a7-4673-b65a-224eae4d628f)

Example of one comment and difference in scores: 

"Metal user here. Rev points are not a good deal. Cashback was better. It's a gimmick.
You can get prices for flights hotels and experiences cheaper elsewhere with out using rev points for ""discounts""."

roBERTa - Negative

Polarity Score - Positive

What do you think ??:)
