from zope.publisher.browser import BrowserView
from z3c.pagelet.browser import BrowserPagelet

from quotationtool.skin.interfaces import _


class SiteLabelView(BrowserView):
    """ A label view for the site."""

    def __call__(self):
        return _('sitelabel', u"quotationtool.org web-application")


class SiteFrontPage(BrowserPagelet):
    """ A pagelet for the site."""
