from googleapiclient.discovery import build

from youtube_videos.models import Video

DEVELOPER_KEY = ['AIzaSyAOz50l1c96OfIOZTQlP3h3e-SbeaoCR1E', 'AIzaSyAxprKX25j2swRx65jOLDS_uoddtfSydRs']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

i = 0


def youtube_cron():
    global i
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY[i])
    search_response = {}
    # Call the search.list method to retrieve results matching the specified
    # query term.
    try:
        search_response = youtube.search().list(
            part=['snippet'],
            maxResults=5,
            type='video',
            order='date',
            publishedAfter='2023-01-01T00:00:00Z',
            relevanceLanguage='hi'
        ).execute()
    except Exception as err:
        if i < len(DEVELOPER_KEY):
            i += 1
        else:
            print("Error Occurred while calling YouTube API", err)

    for search_result in search_response.get('items', []):
        video = Video(title=search_result['snippet']['title'], description=search_result['snippet']['description'],
                      thumbnails_url=search_result['snippet']['thumbnails']['high']['url'],
                      published_date=search_result['snippet']['publishTime'])
        video.save()
