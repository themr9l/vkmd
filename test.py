import dbusmusicplayer

playlist = ['file:///home/themr9l/Downloads/1.mp3', 'file:///home/themr9l/Downloads/2.mp3']

p = dbusmusicplayer.DBusMusicPlayer('com.music.test')

p.set_playlist(playlist)

p.run_loop()