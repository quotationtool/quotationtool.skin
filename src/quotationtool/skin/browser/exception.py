from zope.publisher.browser import BrowserView

from quotationtool.skin.interfaces import _


class UserErrorLabelView(BrowserView):
    """ A label view for user errors."""

    def __call__(self):
        return _('usererror-label',
                 u"User Error")


class SystemErrorLabelView(BrowserView):
    """ A label view for system errors."""

    def __call__(self):
        return _('systemerror-label',
                 u"System Error")


class UnauthorizedErrorLabelView(BrowserView):
    """ A label view for unauthorized errors."""

    def __call__(self):
        return _('unauthorizederror-label',
                 u"Error 403: Unauthorized")


class NotFoundErrorLabelView(BrowserView):
    """ A label view for a 404 error."""

    def __call__(self):
        return _('notfounderror-label',
                 u"Error 404: Not Found")
