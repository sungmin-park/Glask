from flask import url_for, redirect
from glask import current_for, Glask, redirect_for, return_for

app = Glask(__name__)


@app.route('/glask')
def show_glask():
    return 'hello glask'


def test_current_for():
    with app.test_request_context('/glask'):
        assert current_for() == url_for('show_glask')

    # test can access current_for in jinja
    assert app.jinja_env.globals.get('current_for') == current_for


def test_redirect_for():
    with app.test_request_context('/glask'):
        assert redirect_for('show_glask').response == redirect(
            url_for('show_glask')).response


def test_return_for():
    with app.test_request_context('/glask'):
        assert return_for('show_glask', name='value').response == redirect_for(
            'show_glask', name='value').response

    with app.test_request_context('/glask?return_to=/'):
        assert return_for('show_glask', name='value').response == redirect(
            '/').response