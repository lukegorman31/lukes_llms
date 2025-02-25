## Project 2

### End to End BI pipeline for sentiment analysis with CGP. 

Here I built on top of the original project below. I deployed a full end to end BI pipeline to analyse youtube comments. 

1) Data was pulled from youtube with an API and pushed as raw json files into google cloud storage.
2) Raw json files were the pulled and processed which allowed for sentiment analysis.
3) processed and labeled comments were then pushed to staging table in BigQuery.
4) Raw data was modelled with dbt and pushed to views 
5) Views were linked to Looker where a dashboard was created for business intelligence and decision making.





## Project 1

### Revolut Youtube sentiment comparative analysis:

Here I scraped all of the comments from the top 7 videos on Youtube about Revolut from Finfluencers. 
The from the 7 videos I pulled 279 comments for analysis and compared traditional NLP with a modern LLM.

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
