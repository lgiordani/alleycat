from alleycat.actors import human as h


def test_human_has_no_default_position():
    human = h.Human()

    assert human.position == None


def test_human_init_accepts_position():
    human = h.Human(position='aposition')

    assert human.position == 'aposition'

def test_human_changes_position():
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
    for i in range(len(positions)*2):
        human.travel(positions)

    assert len(set(human.visited_positions)) == 6


def test_human_knows_their_path():
    human = h.Human(position='aposition')

    assert human.path == ['aposition']

# def test_human_knows_their_path():
#     positions = ['A', 'B', 'C', 'D', 'E', 'F']
#
#     human = h.Human(position=positions[0])
#     for i in range(50):
#         human.travel(positions)
#
#     assert len(human.path) == 2
