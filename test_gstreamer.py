#!/usr/bin/python3

from os import path

import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst, Gtk

import sys

GObject.threads_init()
Gst.init(None)

class Player(object):
    def __init__(self):
        self.pipeline = Gst.Pipeline()

        # self.filesrc = Gst.ElementFactory.make('filesrc', None)

        # self.pipeline.add(self.filesrc)
        
        # self.filesrc.set_property('location', 'home/themr9l/Downloads/1.mp3')

        # self.decodebin = Gst.ElementFactory.make('decodebin', None)

        # self.pipeline.add(self.decodebin)

        # self.alsasink = Gst.ElementFactory.make('alsasink', None)

        # self.pipeline.add(self.alsasink)

        self.playbin = Gst.ElementFactory.make('playbin', None)

        self.pipeline.add(self.playbin)
        
        self.playbin.set_property('uri', 'file:///home/themr9l/Downloads/1.mp3')

        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message::eos', self.on_eos)

    def run(self):
        # self.window.show_all()
        # You need to get the XID after window.show_all().  You shouldn't get it
        # in the on_sync_message() handler because threading issues will cause
        # segfaults there.
        # self.xid = self.drawingarea.get_property('window').get_xid()
        self.pipeline.set_state(Gst.State.PLAYING)
        # Gtk.main()

    # def quit(self, window):
    #     self.pipeline.set_state(Gst.State.NULL)
    #     Gtk.main_quit()

    # def on_sync_message(self, bus, msg):
    #     if msg.get_structure().get_name() == 'prepare-window-handle':
    #         print('prepare-window-handle')
    #         msg.src.set_window_handle(self.xid)

    def on_eos(self, bus, msg):
        print('on_eos(): seeking to start of video')

    # def on_error(self, bus, msg):
    #     print('on_error():', msg.parse_error())

def handle_keypress(source, cb_condition):
    print(source)
    print(cb_condition)


p = Player()
p.run()

loop = GObject.MainLoop()
# GObject.io_add_watch(sys.stdin, GObject.IO_IN, handle_keypress)
# context = loop.get_context()

# while True:
#     context.iteration(True)
#     print('LOLOOKSDFFFF')

loop.run()