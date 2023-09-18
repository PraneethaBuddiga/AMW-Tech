import requests

api_key = 'AIzaSyCYXRjbqEwAjtWH3W_WJmOFj0Xe2ZxvzOs'
search_query = 'technology'

#requesting parameters
search_url = 'https://www.googleapis.com/youtube/v3/search'
search_params = {
    'part': 'snippet',
    'q': search_query,
    'key': api_key,
    'maxResults': 10
}

#Making API request
search_response = requests.get(search_url, params=search_params)

if search_response.status_code == 200:
    search_data = search_response.json()

    for item in search_data['items']:
        if item['id'].get('videoId'):
            video_id = item['id']['videoId']
            video_link = f'https://www.youtube.com/watch?v={video_id}'
            comments_url = 'https://www.googleapis.com/youtube/v3/commentThreads'
            comments_params = {
                'part': 'snippet',
                'videoId': video_id,
                'key': api_key,
                'maxResults': 50
            }

            comments_response = requests.get(comments_url, params=comments_params)

            if comments_response.status_code == 200:
                comments_data = comments_response.json()

                # Process the comments data
                for item in comments_data['items']:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    print(f'Video Link: {video_link}')
                    print(f'Comment: {comment}')
                    print('-' * 30)
            else:
                print(f'Error getting comments for video {video_link}: {comments_response.status_code}')
else:
    print(f'Error: {search_response.status_code}')
