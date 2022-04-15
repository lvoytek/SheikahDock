import gi
import launcher
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GdkPixbuf, Gio


def get_app_from_name(name):
    for application in Gio.AppInfo.get_all():
        if application.get_display_name() == name:
            return application

    return None


class Rune(Gtk.Overlay):
    def __init__(self, size=200):
        super().__init__()
        self._size = size
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('./rune_background.svg')
        image = Gtk.Image()
        image.set_from_pixbuf(pixbuf)
        image.set_size_request(size, size)

        self.set_child(image)
        self.launcher = launcher.Launcher(self)
        self.add_overlay(self.launcher)

        self._appname = None
        self._app = None

    def set_app_name(self, name):
        if name != self._appname:
            self._appname = name
            self._app = get_app_from_name(name)

    def launch(self):
        if self._app is not None:
            self._app.launch()
