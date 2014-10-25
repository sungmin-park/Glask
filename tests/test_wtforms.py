from glask import Glask
from glask.wtforms import Form
from wtforms import StringField

app = Glask(__name__)
app.config['SECRET_KEY'] = 'SECRET'

ctx = app.test_request_context()
ctx.push()


def test_form_fields():
    class BlankForm(Form):
        pass

    class NotBlankForm(Form):
        item = StringField()

    blank_form = BlankForm()
    assert blank_form.fields() == tuple()
    not_blank_form = NotBlankForm()
    assert not_blank_form.fields() == (not_blank_form.item,)
