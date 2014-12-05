import pytest
from sqlalchemy import Column, Integer

from glask import Glask

from glask.sqlalchemy import Pagination
from flask.ext.sqlalchemy import SQLAlchemy


app = Glask(__name__)
db = SQLAlchemy(app=app)


class Post(db.Model):
    id = Column(Integer, primary_key=True)


@pytest.yield_fixture
def app():
    app = Glask(__name__)
    with app.app_context():
        db.create_all()
        try:
            yield app
        finally:
            db.session.remove()
            db.drop_all()


# noinspection PyUnusedLocal
def test_pager(app):
    [db.session.add(Post()) for _ in range(1132)]
    db.session.commit()
    db.session.remove()
    # test page items
    assert Pagination(query=Post.query).items == \
           Post.query.limit(10).offset(0).all()
    assert Pagination(query=Post.query, page=1).items == \
           Post.query.limit(10).offset(10).all()

    # test page overflow
    pagination = Pagination(query=Post.query, page=114)
    assert pagination.page == 113

    # test page underflow
    pagination = Pagination(query=Post.query, page=-1)
    assert pagination.page == 0


# noinspection PyUnusedLocal
def test_pagination_navigation(app):
    [db.session.add(Post()) for _ in range(1132)]
    db.session.commit()
    db.session.remove()
    # test some random navigation
    pagination = Pagination(query=Post.query, page=77)
    assert pagination.page == 77
    assert pagination.navigation.pages == \
           [70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
    assert pagination.navigation.previous == 69
    assert pagination.navigation.next == 80
    assert pagination.navigation.has_previous
    assert pagination.navigation.has_next

    # test lower bound
    pagination = Pagination(query=Post.query)
    assert pagination.page == 0
    assert pagination.navigation.pages == \
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert pagination.navigation.previous == 0
    assert pagination.navigation.has_previous == False
    assert pagination.navigation.next == 10
    assert pagination.navigation.has_next

    # test upper bound
    pagination = Pagination(query=Post.query, page=113)
    assert pagination.page == 113
    assert pagination.navigation.previous == 109
    assert pagination.navigation.has_previous
    assert pagination.navigation.next == 113
    assert pagination.navigation.pages == \
           [110, 111, 112, 113]
    assert pagination.navigation.has_next == False


# noinspection PyUnusedLocal
def test_pagination_with_empty_table(app):
    pagination = Pagination(query=Post.query)
    assert pagination.page == 0
    assert pagination.navigation.previous == 0
    assert pagination.navigation.has_previous == False
    assert pagination.navigation.next == 0
    assert pagination.navigation.has_next == False
    assert pagination.navigation.pages == [0]
