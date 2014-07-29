import dbusmusicplayer
import vkapi

if __name__ == '__main__':
    access_token = 'c0b23ba69dbc300339842d6446d2e2d4e8f87fc5eef85fcdab68c3730d5d65e0a77bc70acbae83b246a77'
    api = vkapi.VkApi(access_token)

    vk_playlist = api.audio.get()
    # for key in vk_playlist.keys():
    #     print(key)
    # import pdb; pdb.set_trace()
    # print(vk_playlist)
    playlist = []
    for record in vk_playlist['response']:
        playlist.append(record['url'])

    player = dbusmusicplayer.DBusMusicPlayer('com.github.themr9l.vkmd')
    player.set_playlist(playlist)
    player.run_loop()
