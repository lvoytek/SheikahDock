import gi
import launcher
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class Rune(Gtk.Overlay):
    def __init__(self):
        super().__init__()
        self.launcher = launcher.Launcher()
        self.add_overlay(self.launcher)
