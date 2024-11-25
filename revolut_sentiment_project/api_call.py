# Importing the necessary libraries for youtube API scraping and sentiment analysis
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd
import numpy as np
import requests
import os
from urllib.parse import urlparse, parse_qs

# Google API Key
API_KEY = 'YOURAPIKEY :P'

# Extract url ids
def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    """
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    elif parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query)['v'][0]
        elif parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/')[2]
        elif parsed_url.path.startswith('/v/'):
            return parsed_url.path.split('/')[2]
    return None

def get_comments(video_id):
    """
    Fetches all comments from a YouTube video using pagination.
    """
    comments = []
    url = 'https://www.googleapis.com/youtube/v3/commentThreads'
    
    params = {
        'part': 'snippet',
        'videoId': video_id,
        'key': API_KEY,
        'textFormat': 'plainText',
        'maxResults': 1000  # Fetches 100 comments per page
    }
    
    while True:
        response = requests.get(url, params=params)
        data = response.json()

        # Check if data contains 'items' to avoid KeyErrors
        if 'items' not in data:
            print(f"No comments found for video ID {video_id}")
            break

        # Process each comment
        for item in data['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            published_at = item['snippet']['topLevelComment']['snippet']['publishedAt']
            comments.append({'video_id': video_id, 'author': author, 'comment': comment, 'published_at': published_at})

        # Check for pagination
        if 'nextPageToken' in data:
            params['pageToken'] = data['nextPageToken']
        else:
            break

    return comments

def get_comments_for_videos(video_urls):
    """
    Retrieves comments for a list of YouTube video URLs and returns a DataFrame.
    """
    all_comments = []

    for url in video_urls:
        video_id = extract_video_id(url)
        if video_id:
            video_comments = get_comments(video_id)
            all_comments.extend(video_comments)

    return pd.DataFrame(all_comments)

#Video Urls 
videos = ['https://www.youtube.com/watch?v=7MAJfcG8B7E', 'https://www.youtube.com/watch?v=p1Ni5ZuOVZ4', 
          'https://www.youtube.com/watch?v=TW__W5AGKEQ', 'https://www.youtube.com/watch?v=J5FLyHMV9og',
          'https://www.youtube.com/watch?v=gQscaDIRaMQ','https://www.youtube.com/watch?v=p7PPpw55SZI',
          'https://www.youtube.com/watch?v=FiY2RY55YTg']

video_urls = videos


df_comments = get_comments_for_videos(video_urls)

<<<<<<< HEAD
#df_comments.to_csv('comments_df.csv')
=======
print(df_comments.head())

print(len(df_comments['comment']))

#df_comments.to_csv('comments_df.csv')
>>>>>>> a30e3034aea74aea046dbecf0a6d8f43c0fde244
