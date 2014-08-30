from sqlalchemy import Column, Integer

from glask import Glask

from glask.sqlalchemies import Pagination
from flask.ext.sqlalchemy import SQLAlchemy


app = Glask(__name__)
db = SQLAlchemy(app=app)


class Post(db.Model):
    id = Column(Integer, primary_key=True)


def test_pager():
    db.create_all()
    [db.session.add(Post()) for _ in range(123)]
    db.session.commit()
    assert Pagination(query=Post.query).items ==\
           Post.query.limit(10).offset(0).all()
    assert Pagination(query=Post.query, page=1).items ==\
           Post.query.limit(10).offset(10).all()
    pagination = Pagination(query=Post.query, page=1)
    assert pagination.items == Post.query.limit(10).offset(10).all()
