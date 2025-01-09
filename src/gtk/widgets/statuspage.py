from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(resource_path='/io/gitlab/kriptolix/'
              'Exilium/src/gtk/ui/StatusPage.ui')
class StatusPage(Adw.Bin):

    __gtype_name__ = 'StatusPage'

    _status_page = Gtk.Template.Child()

    def __init__(self):

        super().__init__(self)

    def set_status(self, title, description, icon):

        self._status_page.set_title(title)
        self._status_page.set_description(description)
        self._status_page.set_icon_name(icon)
