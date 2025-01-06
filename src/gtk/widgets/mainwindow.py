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
from .itensview import ItensView

@Gtk.Template(resource_path='/io/github/kriptolix/Acervo/'
              'src/gtk/ui/mainwindow.ui')
class AcervoWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'AcervoWindow'

    #_panel_button = Gtk.Template.Child()
    #_go_button = Gtk.Template.Child()
    
    #_overlay_view = Gtk.Template.Child()
    #_split_view = Gtk.Template.Child()
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

        #self._panel_button.connect("clicked", self._show_panel)
        #self._go_button.connect("clicked", self._navigate_pages)
        

    def _show_panel(self, button):
        self._overlay_view.set_show_sidebar(True)

    def _navigate_pages (self, button):

        if button == self._go_button:
            self._split_view.set_show_content(True)        
        
