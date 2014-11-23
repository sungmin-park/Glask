from __future__ import unicode_literals, print_function, absolute_import, \
    division
from urllib2 import urlopen

from flask import url_for
from glask import Glask
# noinspection PyUnresolvedReferences
from glask.pytest import live_app, wsgi_server, client
import pytest


@pytest.yield_fixture
def app():
    app = Glask(__name__)

    # noinspection PyUnusedLocal
    @app.route('/')
    def index():
        return 'It works!!'

    with app.app_context():
        yield app


# noinspection PyUnusedLocal,PyShadowingNames
def test_live_app(live_app):
    url = url_for('index', _external=True)
    assert url == 'http://localhost:5000/'
    index = urlopen(url).read()
    assert index == 'It works!!'


# noinspection PyUnusedLocal,PyShadowingNames
def test_live_app2(live_app):
    url = url_for('index', _external=True)
    assert url == 'http://localhost:5000/'
    index = urlopen(url).read()
    assert index == 'It works!!'


def test_client(client):
    assert 'It works!!' in client.get(url_for('index')).data
