import requests
import json
import APIKey


playlist_link = 'PLqmJZgbzEiLuSiCboeBiGLB0veDJxiWQL'
api_key = APIKey.key
request_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist_link}&key={api_key}"

response = requests.get(request_url)
json_array = json.loads(response.text)['items']

lastets_video = {"title":None, "date":None, "url":None}
lastest_json_record = json_array[len(json_array)-1]['snippet']

lastets_video["date"] = lastest_json_record['title'].split("от")[1]
lastets_video["title"] = lastest_json_record['title']
lastets_video['url'] = lastest_json_record['resourceId']['videoId']

print()