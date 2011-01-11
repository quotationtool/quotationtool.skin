import zope.interface
from z3c.form.interfaces import IFormLayer
from z3c.formui.interfaces import IDivFormLayer
from z3c.layer.pagelet import IPageletBrowserLayer
from z3c.menu.ready2go.interfaces import IMenuManager


class IQuotationtoolBrowserLayer(IFormLayer,
                                 IDivFormLayer,
                                 IPageletBrowserLayer):
    pass
                          

class IQuotationtoolBrowserSkin(IDivFormLayer,
                                IQuotationtoolBrowserLayer):
    """The Quotationtool browser skin for quotationtool uses the div
    form layout.""" 

    pass


class ITabbedContentLayout(zope.interface.Interface):
    """A marker interface for (browser) pagelets that needs
    layout_tabbedcontent.pt as layout instead of layout.pt.

    Yust implement it to the BrowserPagelet in question and there we
    go...
    """


class IMainNav(IMenuManager):
    """A manager for the main navigation."""


class ISubNavManager(IMenuManager):
    """A manager for a subnavigation. This is only a base interface
    and should be derived by each subnavigation manager."""

class IItemTabs(IMenuManager):
    """A manager for the tabs."""



