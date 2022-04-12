import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class Launcher(Gtk.Button):

    def __init__(self):
        super().__init__()
        self._appname = None
        self.connect('clicked', self.launch)

    def set_app_name(self, name):
        self._appname = name

    def launch(self, button):
        print("test")
