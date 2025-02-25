import os
import json
from googleapiclient.discovery import build
from google.cloud import storage
from urllib.parse import urlparse, parse_qs
from datetime import datetime

def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    """
    parsed_url = urlparse(url)
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com', 'm.youtube.com']:
        if parsed_url.path == '/watch':
            query_params = parse_qs(parsed_url.query)
            if 'v' in query_params:
                return query_params['v'][0]
        elif parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/')[2]
        elif parsed_url.path.startswith('/v/'):
            return parsed_url.path.split('/')[2]
        elif parsed_url.path.startswith('/shorts/'):
            return parsed_url.path.split('/')[2]
    return None


def extract_comments(youtube_api_key, video_id, gcs_bucket_name, gcs_file_path):
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    comments = []
    next_page_token = None

    while True:
        results = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=next_page_token
        ).execute()

        for item in results.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append(comment)

        next_page_token = results.get('nextPageToken')
        if not next_page_token:
            break

    # Store comments in GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket_name)
    blob = bucket.blob(gcs_file_path)
    blob.upload_from_string(json.dumps(comments))

    print(f"Comments for video {video_id} stored in GCS: {gcs_file_path}")

if __name__ == "__main__":
    youtube_api_key = os.environ.get("YOUTUBE_API_KEY")
    video_urls = ['https://www.youtube.com/watch?v=7MAJfcG8B7E', 'https://www.youtube.com/watch?v=p1Ni5ZuOVZ4', 
          'https://www.youtube.com/watch?v=TW__W5AGKEQ', 'https://www.youtube.com/watch?v=J5FLyHMV9og',
          'https://www.youtube.com/watch?v=gQscaDIRaMQ','https://www.youtube.com/watch?v=p7PPpw55SZI',
          'https://www.youtube.com/watch?v=FiY2RY55YTg']
    gcs_bucket_name = 'revolut-sentiment-raw-data'
    for url in video_urls:
        video_id = extract_video_id(url)
        if video_id:
            gcs_file_path = f'raw_comments/{video_id}/{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
            extract_comments(youtube_api_key, video_id, gcs_bucket_name, gcs_file_path)
    else:
            print(f"Could not extract video ID from URL: {url}")

    gcs_file_path = f'raw_comments/{video_id}/{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    from datetime import datetime
    extract_comments(youtube_api_key, video_id, gcs_bucket_name, gcs_file_path)
