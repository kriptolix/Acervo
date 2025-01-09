# listsview.py
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
from gi.repository import Gtk, Gio

from typing import Any

from .listnode import ListNode
from .musicdata import MusicObject


@Gtk.Template(resource_path='/io/github/kriptolix/Acervo/'
              'src/gtk/ui/ListsView.ui')
class ListsView(Adw.NavigationPage):
    __gtype_name__ = 'ListsView'

    _all_button = Gtk.Template.Child()
    _add_button = Gtk.Template.Child()
    _revealer = Gtk.Template.Child()
    _search_button = Gtk.Template.Child()
    _close_button = Gtk.Template.Child()
    _back_button = Gtk.Template.Child()
    _grid_view = Gtk.Template.Child()
    _items_view = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._list_store = Gio.ListStore.new(item_type=MusicObject)

        self.reset_timer = None

        self._list_element_factory = Gtk.SignalListItemFactory()
        self._list_element_factory.connect("setup", self._on_setup)
        self._list_element_factory.connect("bind", self._on_bind)

        self._filter = Gtk.CustomFilter.new(self._do_filter)
        self._model = Gtk.FilterListModel.new(self._list_store, self._filter)
        self._model.set_incremental(True)

        self._selection = Gtk.MultiSelection.new()
        self._selection.set_model(self._model)

        self._grid_view.set_model(self._selection)
        self._grid_view.set_factory(self._list_element_factory)

        self._add_button.connect("clicked", self._add_element, None)

        title = _("Nothing Here Yet")
        description = _("Use the '+' button to add a element")
        icon = "info-symbolic"

        # self._status_page.set_status(title, description, icon)

        self._grid_view.connect("activate", self._show_item_details)

        # self._list_store.connect("items-changed", self._on_no_elements)
        # self._list_store.items_changed(0, 0, 0)

        self._close_button.set_action_name("app.quit")
        self._back_button.connect("clicked", self._back_page)
        self._items_view._hide_button.connect("clicked",
                                              self._hide_item_details)

        for i in range(0, 12):
            self._add_element(None, None)

    def _back_page(self, button):

        win = self.get_root()
        win._naviagation_view.pop_to_tag("_groups")

    def _on_setup(self,
                  factory: Gtk.SignalListItemFactory,
                  item: Gtk.ListItem) -> None:
        """Setup the widget to show in the Gtk.Listview"""

        element_widget = ListNode()
        item.set_child(element_widget)

    def _on_bind(self,
                 factory: Gtk.SignalListItemFactory,
                 item: Gtk.ListItem) -> None:
        """bind data from the NodeObject to the visibel widget"""

        element_widget = item.get_child()
        element_object = item.get_item()

        element_widget._title.set_text(element_object._title)

    def _add_element(self,
                     button: Gtk.Button | None,
                     data: Any) -> None:

        element = MusicObject("musica qualquer")

        '''if (data):  # programmatically

            title, text, tag = data

            if (title):
                element.title_buffer.insert_text(0, title, -1)

            element.content_buffer.set_text(text)
            element.tag = tag '''

        self._list_store.insert(0, element)

        # self._grid_view.scroll_to(0, Gtk.ListScrollFlags.NONE)

    def _remove_element(self, element: str) -> None:

        def _dialog_response(dialog: Adw.MessageDialog,
                             response: str) -> None:

            if (response == "cancel"):
                return

            _, position = self._list_store.find(element)

            self._list_store.remove(position)

        ##

        # dialog = MessageDialog(self.get_root(), "remove_element")

        # dialog.connect("response", _dialog_response)

    def _do_filter(self, filter):
        """This will be useful in the future"""
        return True

    def _on_no_elements(self, *_) -> None:

        items = self._list_store.get_n_elements()

        if (items == 0):
            self._element_stack.set_visible_child(self._status_page)
        else:
            self._element_stack.set_visible_child(self._scrolled)

    def _show_item_details(self, grid, position):

        print(self._items_view._hide_button.get_visible())
        
        '''if self._items_view._hide_button.get_visible():

            self._revealer.set_reveal_child(True)
            self._close_button.set_visible(False)

            return

        win = self.get_root()
        win._naviagation_view.push_by_tag("_items")'''

    def _hide_item_details(self, button):

        self._revealer.set_reveal_child(False)
        self._close_button.set_visible(True)
