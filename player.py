import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

GObject.threads_init()
Gst.init(None)
DBusGMainLoop(set_as_default=True)

dbus_music_player_interface_name = 'com.themr9l.dbusmusicplayer'

class Player(dbus.service.Object):
    def __init__(self, player_name):
        self.player_name = player_name

        #init dbus
        dbus_name = dbus.service.BusName(self.player_name, bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, dbus_name, '/')

        #init gstreamer
        self.pipeline = Gst.Pipeline()
        self.playbin = Gst.ElementFactory.make('playbin', None)
        self.pipeline.add(self.playbin)

        pipeline_bus = self.pipeline.get_bus()
        pipeline_bus.add_signal_watch()
        pipeline_bus.connect('message::eos', self.on_eos)

        self.set_current_state(StopState())

    def set_current_state(self, state):
        self.current_state = state

    @dbus.service.method(dbus_interface=dbus_music_player_interface_name)
    def play(self):
        self.current_state.play(self)

    @dbus.service.method(dbus_interface=dbus_music_player_interface_name)
    def next(self):
        self.current_state.next(self)

    def run_loop(self):
        self.g_loop = GObject.MainLoop()
        self.g_loop.run()

    def set_playlist(self, playlist):
        self.playlist = playlist
        self.current_pos = 0

    def on_eos(self, bus, msg):
        self.next()

class PlayerState:
    def __init__(self):
        pass

        def play(self, player):
            pass

        def next(self, player):
            pass

class PlayState(PlayerState):
    def __init__(self):
        pass

    def play(self, player):
        print('PlayState -> PauseState')
        player.playbin.set_state(Gst.State.PAUSED)
        player.set_current_state(PauseState())

    def next(self, player):
        player.pipeline.set_state(Gst.State.NULL)
        player.current_pos += 1
        player.playbin.set_property('uri', player.playlist[player.current_pos])
        player.pipeline.set_state(Gst.State.PLAYING)

class PauseState(PlayerState):
    def __init__(self):
        pass

    def play(self, player):
        print('PauseState -> PlayState')
        player.pipeline.set_state(Gst.State.PLAYING)
        player.set_current_state(PlayState())

    def next(self, player):
        print('PauseState -> PlayState')
        player.pipeline.set_state(Gst.State.NULL)
        player.current_pos += 1
        player.playbin.set_property('uri', player.playlist[player.current_pos])
        player.pipeline.set_state(Gst.State.PLAYING)
        player.set_current_state(PlayState())


class StopState(PlayerState):
    def __init__(self):
        pass

    def play(self, player):
        print('StopState -> PlayState')
        player.playbin.set_property('uri', player.playlist[player.current_pos])
        player.pipeline.set_state(Gst.State.PLAYING)
        player.set_current_state(PlayState())
