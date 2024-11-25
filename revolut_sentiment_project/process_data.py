import pandas as pd
from api_call import get_comments_for_videos

videos = ['https://www.youtube.com/watch?v=7MAJfcG8B7E', 'https://www.youtube.com/watch?v=p1Ni5ZuOVZ4', 
          'https://www.youtube.com/watch?v=TW__W5AGKEQ', 'https://www.youtube.com/watch?v=J5FLyHMV9og',
          'https://www.youtube.com/watch?v=gQscaDIRaMQ','https://www.youtube.com/watch?v=p7PPpw55SZI',
          'https://www.youtube.com/watch?v=FiY2RY55YTg', 'https://www.youtube.com/watch?v=92XoU9cSYdM']

video_urls = videos

df = get_comments_for_videos(video_urls)  # Check if this step works

def clean_data(df):
    #columns 
    df = df.drop(columns=['author','video_id'])
    #date conversion
    df['published_at']= df['published_at'].astype('datetime64[ns]')
    df['month'] = df['published_at'].dt.month
    df['year'] = df['published_at'].dt.year

    df = df.dropna(subset=['comment'])  # Drop rows where 'comment' column is NaN

    #lowercase
    df['comment'] = df['comment'].str.lower()

    #remove links and generic comments about the video
    df = df[~df.comment.str.contains("https")]
    generic_comments  = r'(good video|great video|nice video|awesome video|amazing video|cool video|interesting video)' 
    df = df[~df.comment.str.contains(generic_comments)]

    return df

df = clean_data(df)  # Check if this step works

print("df cleaned:", df.head())

