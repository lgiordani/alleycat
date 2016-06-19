from alleycat.actors import actor as a


def test_actor_has_no_default_position_no_default_name():
    actor = a.Actor()

    assert actor.position is None
    assert actor.name is None


def test_actor_init_accepts_id():
    actor = a.Actor(name="Pixel")

    assert actor.name == "Pixel"
    assert str(actor) == "Pixel"


def test_actor_init_accepts_position():
    actor = a.Actor(position='aposition')

    assert actor.position == 'aposition'


def test_actor_can_travel():
    positions = {'A', 'B', 'C', 'D', 'E', 'F'}

    actor = a.Actor(position='A')
    actor.travel(positions)

    assert actor.position in positions


def test_actor_with_not_routes_does_not_move():
    actor = a.Actor(position='A')
    actor.travel({})

    assert actor.position == 'A'


def test_actor_path_contains_initial_position():
    actor = a.Actor(position='aposition')

    assert actor.path == ['aposition']


def test_actor_knows_their_path():
    positions = {'A', 'B', 'C', 'D', 'E', 'F'}

    actor = a.Actor(position='A')
    for i in range(50):
        actor.travel(positions)

    assert len(actor.path) == 51


def test_actor_knows_how_many_moves_they_did():
    positions = {'A', 'B', 'C', 'D', 'E', 'F'}

    actor = a.Actor(position='A')
    for i in range(50):
        actor.travel(positions)

    assert actor.moves == 50
