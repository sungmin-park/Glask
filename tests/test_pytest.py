from __future__ import unicode_literals, print_function, absolute_import, \
    division
from urllib2 import urlopen

from flask import url_for
from glask import Glask, redirect_for
# noinspection PyUnresolvedReferences
from glask.pytest import live_app, wsgi_server, client, browser
import pytest


@pytest.yield_fixture
def app():
    app = Glask(__name__)

    # noinspection PyUnusedLocal
    @app.route('/')
    def index():
        return 'It works!!'

    # noinspection PyUnusedLocal
    @app.route('/redirect')
    def redirect():
        return redirect_for('index')

    with app.app_context():
        yield app


# noinspection PyUnusedLocal,PyShadowingNames
def test_live_app(live_app):
    url = url_for('index', _external=True)
    assert url == 'http://localhost:7000/'
    index = urlopen(url).read()
    assert index == 'It works!!'


# noinspection PyUnusedLocal,PyShadowingNames
def test_live_app2(live_app):
    url = url_for('index', _external=True)
    assert url == 'http://localhost:7000/'
    index = urlopen(url).read()
    assert index == 'It works!!'


def test_client(client):
    # check client works
    assert 'It works!!' in client.get(url_for('index')).data

    # check url_for external works
    assert client.get(url_for('redirect')).location == \
           url_for('index', _external=True)


# noinspection PyUnusedLocal
def test_browser(live_app, browser):
    browser.get(url_for('index', _external=True))
    assert browser.find_element_by_tag_name('body').text == 'It works!!'
