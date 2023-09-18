import requests

api_key = 'AIzaSyCYXRjbqEwAjtWH3W_WJmOFj0Xe2ZxvzOs'
search_query = 'technology'


url = 'https://www.googleapis.com/youtube/v3/search'
params = {
    'part': 'snippet',
    'q': search_query,
    'key': api_key,
    'maxResults': 10
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Step 5: Process the data (get video links)
    for item in data['items']:
        if item['id'].get('videoId'):
            video_id = item['id']['videoId']
            video_link = f'https://www.youtube.com/watch?v={video_id}'
            print(video_link)
else:
    print(f'Error: {response.status_code}')
