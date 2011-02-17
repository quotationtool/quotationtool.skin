# Extensions to the login form (e.g. a link to a signuo form) may be
# registered for a viewlet manager that implements
# quotationtool.skin.interfaces.ILoginFormExtensions

from zope.viewlet.manager import ViewletManager, WeightOrderedViewletManager

from quotationtool.skin import interfaces


LoginFormExtensions = ViewletManager('loginformextensions',
                                     interfaces.ILoginFormExtensions,
                                     bases = (WeightOrderedViewletManager,),
                                     )

