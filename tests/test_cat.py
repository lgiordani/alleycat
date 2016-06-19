from alleycat.actors import cat as c


def test_cat_has_no_default_position():
    cat = c.Cat()

    assert cat.position is None
