from __future__ import unicode_literals, print_function, absolute_import, \
    division


class Pagination(object):
    def __init__(self, query, page=0, per_page=10):
        self.page = page
        self.items = query[self.page * per_page:(self.page + 1) * per_page]
