import os
from google.cloud import storage, bigquery, language_v1
import json


print("Started.....")


def process_comments(bucket_name, file_name):
    """
    Processes new JSON files in GCS, performs sentiment analysis, and loads results to BigQuery.
    """

    # Download the file from GCS
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    json_data = json.loads(blob.download_as_string())  # Load the JSON data from the file
    
    print(f"Processing {len(json_data)} comments from {file_name}")

    # Perform sentiment analysis
    client = language_v1.LanguageServiceClient()
    comments_with_sentiment = []
    for comment in json_data:
        text = comment['textDisplay']  # Get the comment text
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment  # Analyze sentiment
        comments_with_sentiment.append({
            'video_id': comment['videoId'],  # Add video ID, comment text, etc. to the results
            'comment_text': text,
            'author_name': comment['authorDisplayName'],
            'comment_date': comment['publishedAt'][:10],  # Extract date
            'sentiment_score': sentiment.score,  # Add sentiment score and magnitude
            'sentiment_magnitude': sentiment.magnitude
        })

    print(f"Performed sentiment analysis on {len(comments_with_sentiment)} comments.")

    # Load data into BigQuery
    bq_client = bigquery.Client()
    table_id = 'revolut-sentiment.revolut_sentiment_staging.youtube_comments_staging'  
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("video_id", "STRING"),
            # Define the schema for your BigQuery table
            bigquery.SchemaField("comment_text", "STRING"),
            bigquery.SchemaField("author_name", "STRING"),
            bigquery.SchemaField("comment_date", "DATE"),
            bigquery.SchemaField("sentiment_score", "FLOAT"),
            bigquery.SchemaField("sentiment_magnitude", "FLOAT"),
        ],
        write_disposition="WRITE_APPEND",  # Append new data to the table
    )
    try:
        job = bq_client.load_table_from_json(comments_with_sentiment, table_id, job_config=job_config)
        job.result()  # Wait for the job to complete
        print(f"Successfully loaded {len(comments_with_sentiment)} comments into BigQuery.")
    except Exception as e:
        print(f"Error loading data to BigQuery: {e}")


if __name__ == "__main__":
    bucket_name = 'revolut-sentiment-raw-data'  # Replace with your bucket name
    file_name = 'raw_comments/TW__W5AGKEQ/20250224_155645.json' # Replace with the actual file name
    process_comments(bucket_name, file_name)