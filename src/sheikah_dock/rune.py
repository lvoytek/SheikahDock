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
        self._is_active = False
        self._size = size
        pix_buf = GdkPixbuf.Pixbuf.new_from_file('./rune_background.svg')
        self._rune_background = Gtk.Image()
        self._rune_background.set_from_pixbuf(pix_buf)
        self._rune_background.set_size_request(size, size)

        self.set_child(self._rune_background)

        self._app_image = Gtk.Image()
        self.add_overlay(self._app_image)

        self.launcher = launcher.Launcher(self)
        self.add_overlay(self.launcher)

        self._appname = None
        self._app = None

    def set_app_name(self, name):
        if name != self._appname:
            self._appname = name
            self._app = get_app_from_name(name)

            icon = self._app.get_icon()

            # check if icon is a gtk icon name or snap filename
            if icon.to_string()[0] != '/':
                self._app_image.set_from_icon_name(icon.to_string())
            else:
                # if snap try to replace with existing gtk icon based on desktop filename
                self._app_image.set_from_icon_name(self._app.get_id().replace('_', '.').split('.')[0])

            self._app_image.set_icon_size(Gtk.IconSize.LARGE)
            self._app_image.set_pixel_size(int(self._size * .6))

    def activate_rune(self):
        if not self._is_active:
            pix_buf = GdkPixbuf.Pixbuf.new_from_file('./rune_background_selected.svg')
            self._rune_background.set_from_pixbuf(pix_buf)
            self._is_active = True

    def deactivate_rune(self):
        if self._is_active:
            pix_buf = GdkPixbuf.Pixbuf.new_from_file('./rune_background.svg')
            self._rune_background.set_from_pixbuf(pix_buf)
            self._is_active = False

    def launch(self):
        if self._app is not None:
            self._app.launch()
