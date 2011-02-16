import zope.interface
from z3c.pagelet.browser import BrowserPagelet
from zope.viewlet.manager import ViewletManager, WeightOrderedViewletManager

from quotationtool.skin import interfaces


class DiagnosticsPagelet(BrowserPagelet):
    """ A pagelet that shows some diagnostic info on the running
    instance and calls the diagnostics viewlet manager that shows more
    info provided by viewlets in quotationtool.* packages. """

    zope.interface.implements(interfaces.IDiagnosticsPagelet)


DiagnosticsManager = ViewletManager('diagnostics',
                                    interfaces.IDiagnostics,
                                    bases = (WeightOrderedViewletManager,))
