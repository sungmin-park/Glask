from __future__ import unicode_literals, print_function, absolute_import, \
    division
from uuid import uuid4
from glask import Glask


def make_app():
    app = Glask(import_name=__name__)
    app.config.from_object(object())
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///glask_' + uuid4().hex
    return app