import zope.interface
import zope.component
from zope.publisher.browser import BrowserView
from zope.viewlet.manager import ViewletManager, WeightOrderedViewletManager
from zope.viewlet.interfaces import IViewletManager
from zope.contentprovider.interfaces import IContentProvider

from quotationtool.skin import interfaces


FlagsManager = ViewletManager('flags',
                              interfaces.IFlags,
                              bases = (WeightOrderedViewletManager,))


class FlagsView(BrowserView):

    def __call__(self):
        provider = zope.component.getMultiAdapter(
            (self.context, self.request, self),
            IContentProvider,
            name = 'flags')
        provider.update()
        return provider.render()
