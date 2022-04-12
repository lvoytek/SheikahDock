import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_decorated(False)
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)

        self.button = Gtk.Button(label="Test")
        self.box1.append(self.button)
        self.button.connect('clicked', self.print_test)

    def print_test(self, button):
        print("Test")


class SheikahDock(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, application):
        self.win = MainWindow(application=application)
        self.win.present()


if __name__ == "__main__":
    app = SheikahDock(application_id="com.example.GtkApplication")
    app.run(sys.argv)