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
from gi.repository import Gtk

@Gtk.Template(resource_path='/io/github/kriptolix/Acervo/'
              'src/gtk/ui/listsview.ui')
class ListsView(Adw.NavigationPage):
    __gtype_name__ = 'ListsView'

    #_panel_button = Gtk.Template.Child()
    _plus_button = Gtk.Template.Child()
    _search_button = Gtk.Template.Child()
    _close_button = Gtk.Template.Child()    
    _grid_view = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
