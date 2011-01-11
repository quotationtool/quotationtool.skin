from zope.publisher.browser import BrowserView
from z3c.pagelet.browser import BrowserPagelet


class NotImplementedPagelet(BrowserPagelet):
    pass


class NotImplementedView(BrowserView):
    
    def __call__(self):
        return u"NOT IMPLEMENTED<!-- view '%s' for object %s and request %s IS NOT IMPLEMENTED -->" % (self.__name__, str(self.context), str(self.request))
