# import dbusmusicplayer
import vkapi
import random
import subprocess
import player

# def on_next(pos):
#     record = vk_playlist_responce[pos]
#     subprocess.call(['notify-send', record['artist'], record['title']])

if __name__ == '__main__':
    access_token = 'c0b23ba69dbc300339842d6446d2e2d4e8f87fc5eef85fcdab68c3730d5d65e0a77bc70acbae83b246a77'
    api = vkapi.VkApi(access_token)

    vk_playlist = api.audio.get()
    vk_playlist_responce = vk_playlist['response']
    random.shuffle(vk_playlist_responce)
    playlist = []
    for record in vk_playlist_responce:
        playlist.append(record['url'])

    p = player.Player('com.github.themr9l.vkmd')
    p.set_playlist(playlist)
    p.run_loop()
