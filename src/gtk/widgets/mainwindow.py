# window.py
#
# Copyright 2025 k
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk

from .listsview import ListsView
from .groupsview import GroupsView
from .itemsview import ItemsView


@Gtk.Template(resource_path='/io/github/kriptolix/Acervo/'
              'src/gtk/ui/mainwindow.ui')
class AcervoWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'AcervoWindow'

    _naviagation_view = Gtk.Template.Child()
    _break_point = Gtk.Template.Child()
    _lists_view = Gtk.Template.Child()
    _items_view = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self._panel_button.connect("clicked", self._show_panel)
        # self._go_button.connect("clicked", self._navigate_pages)

        self._break_point.connect("apply", self._breakpoint_applied)
        self._break_point.connect("unapply", self._breakpoint_unapplied)

    def _breakpoint_applied(self, breakpoint):

        print("apply")

        self._lists_view._revealer.set_reveal_child(False)
        self._items_view._hide_button.set_visible(False)
        self._items_view._back_button.set_visible(True)
        self._items_view._item_title.set_max_width_chars(-1)

        page = self._naviagation_view.get_visible_page()

        if (page == self._lists_view and
                self._lists_view._revealer.set_reveal_child()):

            self._naviagation_view.push_by_tag("_items")

    def _breakpoint_unapplied(self, breakpoint):

        print("unapply")

        self._lists_view._revealer.set_reveal_child(True)
        self._items_view._hide_button.set_visible(True)
        self._items_view._back_button.set_visible(False)
        self._items_view._item_title.set_max_width_chars(19)

        page = self._naviagation_view.get_visible_page()

        if (page == self._items_view and
                self._lists_view._revealer.set_reveal_child()):

            self._naviagation_view.push_by_tag("_items")
