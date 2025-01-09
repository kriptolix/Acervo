# TemplateMusic.py
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

from gi.repository import GObject
from gi.repository import Gtk

class MusicObject(GObject.Object):
    __gtype_name__ = 'MusicObject'

    #_title = GObject.Property(type=str, default="title")    
    
    def __init__(self, title):
        super().__init__()

        self._title = title



@Gtk.Template(resource_path='/io/github/kriptolix/Acervo/'
              'src/gtk/ui/TemplateMusic.ui')
class TemplateMusic(Gtk.Box):
    __gtype_name__ = 'TemplateMusic'   
    
    _cover = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)