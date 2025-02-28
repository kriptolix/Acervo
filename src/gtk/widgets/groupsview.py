# groupsview.py
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

from .grouprow import GroupRow

@Gtk.Template(resource_path='/io/github/kriptolix/Acervo/'
              'src/gtk/ui/groupsview.ui')
class GroupsView(Adw.NavigationPage):
    __gtype_name__ = 'GroupsView'

    _list_box = Gtk.Template.Child()
    _close_button = Gtk.Template.Child()
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)        

        for i in range(0,6):
            row = GroupRow()
            self._list_box.append(row)


        self._list_box.connect("child-activated", self._collection_selected)
        self._close_button.set_action_name("app.quit")

    def _collection_selected(self, box, child):
        
        win = self.get_root()    
        win._naviagation_view.push_by_tag("_lists")