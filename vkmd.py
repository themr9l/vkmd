#!/usr/bin/env python
# -*- coding: utf-8 -*-
import vkapi
import random
# import subprocess
import player


# def on_next(pos):
#     record = vk_playlist_responce[pos]
#     subprocess.call(['notify-send', record['artist'], record['title']])

if __name__ == '__main__':
    access_token = '73ab34b523418d78c8db07948f2d50514e2202c2c9abb5a93f86bd5bb4eb28b66c6647278fad527121953'
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

# gst-launch-1.0 playbin uri=file:///home/joe/my-random-media-file.mpeg #test
