from zope.viewlet.manager import ViewletManager, WeightOrderedViewletManager

from quotationtool.skin import interfaces

SidePanel = ViewletManager('sidepanel',
                           interfaces.ISidePanel,
                           bases = (WeightOrderedViewletManager,))

