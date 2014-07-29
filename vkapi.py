import requests
import urllib
import json #test TODO remove

api_base_url = urllib.parse.urlunparse(('https', 'api.vk.com', 'method/', '', '', '')) 

class VkApi:
    __access_token = None
    audio = None

    def __init__(self, access_token):
        self.__access_token = access_token
        self.audio = VkAudio(self.__access_token)

class VkAudio:
    __access_token = None
    __get_url = urllib.parse.urljoin(api_base_url, 'audio.get') 

    def __init__(self, access_token):
        self.__access_token = access_token

    def get(self, owner_id=None, album_id=None, audio_ids=None, need_user=False, offset=0, count=None):
        if audio_ids:
            audio_ids = list(map(str, audio_ids))
            audio_ids = ','.join(audio_ids)

        need_user = int(need_user)

        payload = {
            'owner_id': owner_id,
            'album_id': album_id,
            'audio_ids': audio_ids,
            'need_user': need_user,
            'offset': offset,
            'count': count,
            'access_token': self.__access_token
        }

        responce = requests.get(self.__get_url, params=payload)
        return responce.json()

if __name__ == '__main__':
    access_token = 'c0b23ba69dbc300339842d6446d2e2d4e8f87fc5eef85fcdab68c3730d5d65e0a77bc70acbae83b246a77'
    api = VkApi(access_token)
    print(json.dumps(api.audio.get(count=1), sort_keys=True, indent=4, separators=(',', ': ')))