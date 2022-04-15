import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class Launcher(Gtk.Button):

    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self.connect('clicked', self.launch)

    def launch(self, button):
        self._parent.launch()

