#!/usr/bin/env python3
"""
    deadcolorful  simple dead pixel check
"""
import argparse
import signal


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


ARGP = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)


class DeadColorful():
    def __init__(self):
        self.window = Gtk.Window(
            title=self.__class__.__name__t,
        )
        self.window.connect('destroy', self.on_destroy)

    def main(self):
        self.window.show_all()
        Gtk.main()

    def on_destroy(self, *args, **kwargs):
        Gtk.main_quit()


def main(argp=None):
    if argp is None:
        argp = ARGP.parse_args()  # pragma: no cover

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    instance = DeadColorful()
    instance.main()

if __name__ == '__main__':
    main()  # pragma: no cover
