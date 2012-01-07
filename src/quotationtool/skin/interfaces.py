import zope.interface
from z3c.form.interfaces import IFormLayer
from z3c.formui.interfaces import IDivFormLayer
from z3c.layer.pagelet import IPageletBrowserLayer
from z3c.menu.ready2go.interfaces import IMenuManager
from zope.viewlet.interfaces import IViewletManager
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('quotationtool')


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


class IItemActions(IViewletManager):
    """ A manager for actions on a database item."""


class ISidePanel(IViewletManager):
    """A viewlet manager for components that should show up in the
    side panel."""


class IFlags(IViewletManager):
    """A viewlet manager for flags on an item."""


class IItemInfo(zope.interface.Interface):
    """ There is a tales namespace adapter named 'quotationtool' that
    provides info about an item in the database."""

    creator = zope.interface.Attribute(
        "The Title (Name) of the prncipal who created the item.")


class IDiagnostics(IViewletManager):
    """ A Viewletmanager for diagnostics """


class IDiagnosticsPagelet(zope.interface.Interface):
    """ A pagelet view that calls the diagnostics viewlet manager."""


class ILoginFormExtensions(IViewletManager):
    """ Extensions e.g. "sign up" for the login form."""


class ICSS(IViewletManager):
    """ CSS viewlet."""
