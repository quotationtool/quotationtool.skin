from zope.publisher.browser import BrowserView

from quotationtool.skin.interfaces import _


class UserErrorLabelView(BrowserView):
    """ A label view for user errors."""

    def __call__(self):
        return _('usererror-label',
                 u"User Error")

