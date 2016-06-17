from alleycat.actors import cat as c
from alleycat.actors import human as h


def test_cat_has_no_default_position():
    cat = c.Cat()

    assert cat.position is None

def test_cat_init_accepts_name():
    actor = c.Cat(name="Pixel")

    assert actor.name == "Pixel"
    assert str(actor) == "Cat Pixel"