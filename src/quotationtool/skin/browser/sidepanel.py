from zope.viewlet.manager import ViewletManager, WeightOrderedViewletManager
import os.path

from quotationtool.skin import interfaces


sidepanel_template = os.path.join(os.path.dirname(__file__), 'sidepanel.pt')


SidePanel = ViewletManager('sidepanel',
                           interfaces.ISidePanel,
                           template = sidepanel_template,
                           bases = (WeightOrderedViewletManager,))

