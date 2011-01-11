import zope.interface
from zope.viewlet.manager import ViewletManager
from z3c.menu.ready2go import IContextMenu
from z3c.menu.ready2go.manager import MenuManager

from quotationtool.skin import interfaces


ItemTabs = ViewletManager('itemtabs', IContextMenu,
                          bases = (MenuManager,))

interfaces.IItemTabs.implementedBy(ItemTabs)
