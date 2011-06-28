import zope.i18n
from z3c.table import header
import urllib

from quotationtool.skin.interfaces import _


class SortingColumnHeader(header.ColumnHeader):
    """ As SortingColumnHeader from z3c.table, but offers css for
    headers."""

    def render(self):
        table = self.table
        prefix = table.prefix
        colID = self.column.id

        # this may return a string 'id-name-idx' if coming from request,
        # otherwise in Table class it is intialised as a integer string
        currentSortID = table.getSortOn()
        try:
            currentSortID = int(currentSortID)
        except ValueError:
            currentSortID = currentSortID.rsplit('-', 1)[-1]

        currentSortOrder = table.getSortOrder()

        sortID = colID.rsplit('-', 1)[-1]

        sortOrder = table.sortOrder
        if int(sortID) == int(currentSortID):
            # ordering the same column so we want to reverse the order
            if currentSortOrder in table.reverseSortOrderNames:
                sortOrder = 'ascending'
            elif currentSortOrder == 'ascending':
                sortOrder = table.reverseSortOrderNames[0]

        args = self.getQueryStringArgs()
        args.update({'%s-sortOn' % prefix: colID,
                     '%s-sortOrder' % prefix: sortOrder})
        queryString = '?%s' % (urllib.urlencode(args))

        #CSS
        if table.getSortOn() == self.column.id:
            cssClass = u' class="active %s"' % sortOrder
        else:
            cssClass = u""

        return '<a href="%s" title="%s"%s>%s</a>' % (
            queryString,
            zope.i18n.translate(_('Sort'), context=self.request),
            cssClass,
            zope.i18n.translate(self.column.header, context=self.request))
