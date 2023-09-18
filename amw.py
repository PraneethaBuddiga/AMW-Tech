import requests

api_key = 'AIzaSyCYXRjbqEwAjtWH3W_WJmOFj0Xe2ZxvzOs'
video_id = 'vBpQ1SlfVtU'

url = 'https://www.googleapis.com/youtube/v3/commentThreads'
params = {
    'part': 'snippet',
    'videoId': video_id,
    'key': api_key,
    'maxResults': 50
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    for item in data['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        username = item['snippet']['topLevelComment']['snippet']['authorDisplayName']

        print(f'Username: {username}')
        print(f'Comment: {comment}')
        print('-' * 30)  # Just to separate each comment for better visibility
    else:
        print(f'Error: {response.status_code}')


