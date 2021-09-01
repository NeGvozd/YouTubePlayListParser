import requests
import json
import datetime
import APIKey


def get_array(playlist_link:str, api_key:str):
    request_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist_link}&key={api_key}"
    response = requests.get(request_url)
    return json.loads(response.text)['items']


def parse_array(lastest_video:dict, json_array)->dict:
    lastest_json_record = json_array[len(json_array)-1]['snippet']
    lastest_video["date"] = lastest_json_record['title'].split("от ")[1]
    lastest_video["title"] = lastest_json_record['title']
    lastest_video['url'] = f"https://www.youtube.com/watch?v={lastest_json_record['resourceId']['videoId']}"


def save_video(current:dict):
    with open('current_video.json', 'w') as f:
        j = json.dumps(current)
        f.writelines(j)


def compare_videos(updated:dict):
    def get_date(str_date:str):
        return datetime.datetime.strptime(str_date, '%d.%m.%Y')

    try:
        f = open('current_video.json')
    except IOError as e:
        print('No file')
        save_video(updated)
    else:
        with f:
            current = json.load(f)
            if get_date(updated["date"]) <= get_date(current["date"]):
                return
            else:
                print('update video')
                save_video(updated)


def main():
    playlist_link = 'PLqmJZgbzEiLuSiCboeBiGLB0veDJxiWQL'
    api_key = APIKey.key

    lastest_video = {"title":None, "date":None, "url":None}
    parse_array(lastest_video, get_array(playlist_link, api_key))
    compare_videos(lastest_video)


if __name__ == "__main__":
    main()
