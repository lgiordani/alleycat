from alleycat.actors import human as h


def test_human_has_no_default_position():
    human = h.Human()

    assert human.position is None

def test_cat_init_accepts_name():
    human = h.Human(name="Robert")

    assert human.name == "Robert"
    assert str(human) == "Human Robert"

def test_human_with_not_routes_does_not_move():
    human = h.Human(position='A')
    human.travel([])

    assert human.position == 'A'

def test_human_can_travel_and_changes_position_if_possible():
    positions = ['A', 'B', 'C', 'D', 'E', 'F']

    human = h.Human(position=positions[0])
    human.travel(positions)

    assert human.position != positions[0]


def test_human_knows_visited_positions():
    positions = ['A', 'B', 'C', 'D', 'E', 'F']

    human = h.Human(position=positions[0])
    human.travel(positions)
    human.travel(positions)

    assert len(human.visited_positions) == 2


def test_human_does_not_visit_already_visited_position_if_possible():
    positions = ['A', 'B', 'C', 'D', 'E', 'F']

    human = h.Human(position=positions[0])
    for i in range(len(positions) - 1):
        human.travel(positions)

    assert len(set(human.visited_positions)) == 5


def test_human_visits_already_visited_position_if_unavoidable():
    positions = ['A', 'B', 'C', 'D', 'E', 'F']

    human = h.Human(position=positions[0])
    for i in range(len(positions) * 2):
        human.travel(positions)

    assert len(set(human.visited_positions)) == 6
