import pdb
from api_call import get_comments_for_videos
from process_data import clean_data
from NLP import add_polarity, sentiment
from LLM import get_sentiment

# Step 1: Get data from API
videos = ['https://www.youtube.com/watch?v=7MAJfcG8B7E', 'https://www.youtube.com/watch?v=p1Ni5ZuOVZ4', 
          'https://www.youtube.com/watch?v=TW__W5AGKEQ', 'https://www.youtube.com/watch?v=J5FLyHMV9og',
          'https://www.youtube.com/watch?v=gQscaDIRaMQ','https://www.youtube.com/watch?v=p7PPpw55SZI',
          'https://www.youtube.com/watch?v=FiY2RY55YTg', 'https://www.youtube.com/watch?v=92XoU9cSYdM']

video_urls = videos
# Step 1: Get comments for videos
print("Fetching comments for videos...")
df_comments = get_comments_for_videos(video_urls)  # Check if this step works
print("Comments fetched successfully.")

# Step 2: Process data
print("Cleaning data...")
df = clean_data(df_comments)  # Check if this step works
print("Data cleaned successfully.")
print("df clean:", df.head())

# Sentiment analysis: NLP
print("Adding polarity...")
df = add_polarity(df)
print("Polarity added successfully.")

print("Performing sentiment analysis...")
df = sentiment(df)
print("Sentiment analysis completed successfully.")

# Apply the sentiment analysis to each comment
print("Applying sentiment analysis to each comment...")

# Debugging: Check the first few comments
print("First few comments:", df['comment'].head())

# Apply sentiment analysis with detailed debugging
df['LLM sentiment'], df['LLM score'] = zip(*df['comment'].map(get_sentiment))
print("Sentiment analysis applied successfully.")

# Save the DataFrame to a CSV file
print("Saving DataFrame to CSV...")
df.to_csv('df.csv', index=False)
print("DataFrame saved to df.csv successfully.")