from flask import request
from glask import Glask

app = Glask(__name__)


@app.route('/glask/edit')
def edit_glask():
    return 'edit_glask'


def test_http_methods():
    with app.test_request_context('/glask/edit', method='GET'):
        assert request.is_get is True
        assert request.is_post is False
    with app.test_request_context('/glask/edit', method='POST'):
        assert request.is_get is False
        assert request.is_post is True


def test_config_from_object_current_method_signiture():
    glask = Glask(import_name=__name__)
    glask.config.from_object(obj=object())
