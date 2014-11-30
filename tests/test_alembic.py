from __future__ import unicode_literals, print_function, absolute_import, \
    division
from uuid import uuid4

from glask import Glask
from glask.alembic import pg_cursor, parse_dbname, upgrade
import pytest


@pytest.yield_fixture
def app():
    app = Glask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///glask_' + uuid4().hex
    with app.app_context():
        yield app


def db_exists(name):
    with pg_cursor() as cursor:
        cursor.execute(
            'SELECT EXISTS(SELECT 1 FROM pg_database WHERE datname = %s)',
            (name, )
        )
        return cursor.fetchone()[0]


def test_upgrade(app):
    dbname = parse_dbname(app=app)
    assert not db_exists(name=dbname)
    with upgrade(app=app):
        assert db_exists(name=dbname)
        with pg_cursor(database=dbname) as cursor:
            cursor.execute('SELECT * FROM alembic_version')
            assert cursor.fetchone()[0] == '14eb5bc5ddfb'
    assert not db_exists(name=dbname)
