from alleycat.actors import cat as c
from alleycat.actors import human as h


def test_cat_has_no_default_position():
    cat = c.Cat()

    assert cat.position is None
