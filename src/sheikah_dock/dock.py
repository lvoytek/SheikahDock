import sys
import rune
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk


def get_default_screen_width():
    display = Gdk.Display.get_default()
    return display.get_primary_monitor().get_geometry().width


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._num_runes = 6
        self._edge_width = int(get_default_screen_width() / 20)
        self._separation_width = int(get_default_screen_width() / 40)

        self.set_decorated(False)
        self.set_default_size(get_default_screen_width(), self.get_rune_size())

        self.rune_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.rune_box.set_spacing(self._separation_width)
        self.rune_box.set_margin_start(self._edge_width)
        self.set_child(self.rune_box)

        self.runes = []
        for i in range(self._num_runes):
            self.runes.append(rune.Rune(self.get_rune_size()))
            self.rune_box.append(self.runes[i])

        i = 0
        for app_name in self.get_apps_list():
            self.runes[i].set_app_name(app_name)
            i += 1

        self._active_rune = 0
        mouse_motion_control = Gtk.EventControllerMotion.new()
        mouse_motion_control.connect("motion", self.mouse_motion)
        self.add_controller(mouse_motion_control)

        key_control = Gtk.EventControllerKey.new()
        key_control.connect("key-pressed", self.key_press)
        self.add_controller(key_control)

    def mouse_motion(self, motion, x, y):
        for i in range(self._num_runes):
            if self.runes[i].contains(x - self._edge_width - i * (self.get_rune_size() + self._separation_width), y):
                self.set_active_rune(i)
                break

    def key_press(self, keypress, keyval, keycode, state):
        if keyval in {Gdk.KEY_Left, Gdk.KEY_leftarrow}:
            self.move_active_rune_left()
        elif keyval in {Gdk.KEY_Right, Gdk.KEY_rightarrow}:
            self.move_active_rune_right()
        elif keyval in {Gdk.KEY_space, Gdk.KEY_Return}:
            self.runes[self._active_rune].launch()

    def move_active_rune_right(self):
        if self._active_rune >= len(self.runes) - 1:
            self.set_active_rune(0)
        else:
            self.set_active_rune(self._active_rune + 1)

    def move_active_rune_left(self):
        if self._active_rune <= 0:
            self.set_active_rune(len(self.runes) - 1)
        else:
            self.set_active_rune(self._active_rune - 1)

    def set_active_rune(self, rune_num):
        self.runes[self._active_rune].deactivate_rune()
        self._active_rune = rune_num
        self.runes[self._active_rune].activate_rune()

    def get_rune_size(self):
        return int((get_default_screen_width() - 2 * self._edge_width - (self._num_runes - 1) * self._separation_width)
                   / self._num_runes)

    def get_apps_list(self):
        return ['Files', 'Firefox Web Browser', 'Tilix', 'LibreOffice']

    def mousemove(self, widget, event):
        print("mouse")


class SheikahDock(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, application):
        self.win = MainWindow(application=application)
        self.win.present()


def main():
    app = SheikahDock(application_id="com.github.lvoytek.sheikahdock")
    app.run(sys.argv)


if __name__ == "__main__":
    main()
