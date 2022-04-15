import gi
import launcher
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GdkPixbuf


class Rune(Gtk.Overlay):
    def __init__(self, size=200):
        super().__init__()
        self._size = size
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('./rune_background.svg')
        image = Gtk.Image()
        image.set_from_pixbuf(pixbuf)
        image.set_size_request(size, size)

        self.set_child(image)
        self.launcher = launcher.Launcher()
        self.add_overlay(self.launcher)
