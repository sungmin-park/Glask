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


def test_id():
    class SomeLongNamedForm(Form):
        pass

    some_long_named_form = SomeLongNamedForm()
    assert some_long_named_form.form_id == 'some_long_named_form'


def test_prefix():
    class SomePrefixedForm(Form):
        pass

    some_prefixed_form = SomePrefixedForm()

    # noinspection PyProtectedMember
    assert some_prefixed_form._prefix == 'some_prefixed_form_'
