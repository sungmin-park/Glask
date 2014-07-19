from glask.datetimes import now


def test_now():
    assert now().tzinfo
