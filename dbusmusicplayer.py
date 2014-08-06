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
class DBusMusicPlayer(dbus.service.Object):
    __name = None
    __pipeline = None
    __playbin = None
    __g_loop = None

    __current_pos = -1 
    __playlist = []

    __eol_callback = None

    def __init__(self, name):
        self.__name = name

        bus_name = dbus.service.BusName(self.__name, bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/')

        self.__pipeline = Gst.Pipeline()

        self.__playbin = Gst.ElementFactory.make('playbin', None)

        self.__pipeline.add(self.__playbin)

    @dbus.service.method(dbus_interface=dbus_music_player_interface_name)
    def next(self):
        if self.is_eol(self.__current_pos + 1):
            return
        self.__current_pos += 1
        self.set_uri(self.__playlist[self.__current_pos])

    def is_eol(self, position):
        eol = position < 0 or position >= len(self.__playlist)
        if self.__eol_callback:
            self.__eol_callback()
        return eol

    def run_loop(self):
        self.__g_loop = GObject.MainLoop()
        self.__g_loop.run()

    @dbus.service.method(dbus_interface=dbus_music_player_interface_name)
    def play(self):
        self.__pipeline.set_state(Gst.State.PLAYING)

    def set_playlist(self, playlist):
        self.__playlist = playlist

    def set_uri(self, uri):
        self.__pipeline.set_state(Gst.State.NULL)
        self.__playbin.set_property('uri', uri)

    def set_eol_callback(self, callback):
        self.__eol_callback = callback