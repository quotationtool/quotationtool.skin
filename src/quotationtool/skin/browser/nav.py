import zope.interface
from zope.viewlet.manager import ViewletManager
from z3c.menu.ready2go import ISiteMenu
from z3c.menu.ready2go.manager import MenuManager
from z3c.menu.ready2go.item import SiteMenuItem

from quotationtool.skin import interfaces


MainNav = ViewletManager('mainnav', ISiteMenu,
                         bases = (MenuManager,))

interfaces.IMainNav.implementedBy(MainNav)

class MainNavItem(SiteMenuItem):
    pass


OtherNav = ViewletManager('othernav', ISiteMenu,
                          bases = (MenuManager,))

interfaces.IOtherNav.implementedBy(OtherNav)

class OtherNavItem(SiteMenuItem):
    pass
