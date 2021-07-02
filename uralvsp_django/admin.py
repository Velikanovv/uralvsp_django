from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class MyAdminSite(AdminSite):
    # Text to put at the end of each page <title>.
    site_title = ugettext_lazy('a1')

    # Text to put in each page <h1> (and above login form).
    site_header = ugettext_lazy('a2')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('a3')

admin_site = MyAdminSite()