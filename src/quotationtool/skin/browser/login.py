# The login and logout pages are defined in the subpackage
# quotationtool.skin.browser.authetication. In this module we only
# define extensions to the login form and other login related
# components used in the skin.
#
# Extensions to the login form (e.g. a link to a signuo form) may be
# registered for a viewlet manager that implements
# quotationtool.skin.interfaces.ILoginFormExtensions

from zope.viewlet.manager import ViewletManager, WeightOrderedViewletManager

from quotationtool.skin import interfaces


LoginFormExtensions = ViewletManager('loginform_extensions',
                                     interfaces.ILoginFormExtensions,
                                     bases = (WeightOrderedViewletManager,),
                                     )

