import zope.interface
import zope.component
from zope.publisher.browser import BrowserView
from zope.viewlet.manager import ViewletManager, WeightOrderedViewletManager
from zope.viewlet.interfaces import IViewletManager
from zope.contentprovider.interfaces import IContentProvider

from quotationtool.skin import interfaces


ItemActionsManager = ViewletManager('itemactions',
                              interfaces.IItemActions,
                              bases = (WeightOrderedViewletManager,))
