import zope.interface
import zope.component
from zope.tales.interfaces import ITALESFunctionNamespace
from zope.dublincore.interfaces import IZopeDublinCore
from zope.authentication.interfaces import IAuthentication
from zope.app.component import hooks

from quotationtool.skin.interfaces import IItemInfo


class QuotationtoolTalesAPI(object):
    """A tales namespace adapter to conveneantly access info widely
    used in quotationtool via TAL Expressions."""

    zope.interface.implements(ITALESFunctionNamespace,
                              IItemInfo)

    def __init__(self, context):
        self.context = context

    def setEngine(self, engine):
        self._engine = engine

    @property
    def creator(self):
        """ Returns the creator for the context item. Returns the real
        title given in the pau, not the dc.creator string, which is an
        internal computed value."""
        creator = u"Unkown"
        dc = IZopeDublinCore(self.context, None)
        if dc is None:
            return creator
        pau = zope.component.queryUtility(
            IAuthentication,
            context = hooks.getSite()
            )
        if pau is not None:
            try:
                creator = pau.getPrincipal(dc.creators[0]).title
            except Exception:
                pass
        return creator

    @property
    def editor(self):
        """ Returns the creator for the context item. Returns the real
        title given in the pau, not the dc.creator string, which is an
        internal computed value."""
        creator = u"Unkown"
        dc = IZopeDublinCore(self.context, None)
        if dc is None:
            return creator
        pau = zope.component.queryUtility(
            IAuthentication,
            context = hooks.getSite()
            )
        if pau is not None:
            try:
                creator = pau.getPrincipal(dc.creators[-1]).title
            except Exception:
                pass
        return creator
