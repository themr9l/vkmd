import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

GObject.threads_init()

Gst.init(None)

class Example(dbus.service.Object):
    f = True

    def __init__(self, object_path):
        bus_name = dbus.service.BusName('com.themr9l.test', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/')

        self.pipeline = Gst.Pipeline()

        self.playbin = Gst.ElementFactory.make('playbin', None)

        self.pipeline.add(self.playbin)
        
        self.playbin.set_property('uri', 'file:///home/themr9l/Downloads/1.mp3')

    @dbus.service.method(dbus_interface='com.themr9l')
    def play(self):
        if self.f:
            self.pipeline.set_state(Gst.State.PLAYING)
            self.f = False
        else:
            self.pipeline.set_state(Gst.State.NULL)
            self.playbin.set_property('uri', 'file:///home/themr9l/Downloads/2.mp3')
            self.pipeline.set_state(Gst.State.PLAYING)



DBusGMainLoop(set_as_default=True)

test = Example(None)

main_loop = GObject.MainLoop()
main_loop.run()