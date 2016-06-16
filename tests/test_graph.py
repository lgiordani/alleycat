import json

import pytest
from alleycat import graph as g


# The test graph is the following
#
# A *------* B
#   |      |
#   |      |
# C *------* D
#   | \    |
#   |   \  |
# E *------* F
#
# (C is also connected with F)

@pytest.fixture
def graph_json():
    # Some connections are listed twice
    # either in the same order or reversed
    # to take into account data source
    # errors (I spotted them =) )
    connections_list = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('D', 'C'),
        ('E', 'C'),
        ('E', 'F'),
        ('F', 'D'),
        ('C', 'F'),
    ]

    return json.dumps(connections_list)


@pytest.fixture
def graph_json_errors():
    # Some connections are listed twice
    # either in the same order or reversed
    # to take into account data source
    # errors (I spotted them =) )
    connections_list = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('D', 'B'),
        ('D', 'C'),
        ('E', 'C'),
        ('E', 'F'),
        ('F', 'D'),
        ('C', 'F'),
        ('E', 'F')
    ]

    return json.dumps(connections_list)


@pytest.fixture
def graph_dictionary():
    return {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D', 'E', 'F'],
        'D': ['B', 'C', 'F'],
        'E': ['C', 'F'],
        'F': ['E', 'D', 'C']
    }


def test_build_graph_from_json(graph_json, graph_dictionary):
    graph = g.Graph.from_json(graph_json)

    assert graph.as_dict() == graph_dictionary


def test_build_graph_from_json_can_handle_data_errors(graph_json_errors, graph_dictionary):
    graph = g.Graph.from_json(graph_json_errors)

    assert graph.as_dict() == graph_dictionary


def test_graph_can_return_node_neighbours(graph_json):
    graph = g.Graph.from_json(graph_json)

    assert graph.get_node_neighbours('C') == ['A', 'D', 'E', 'F']


def test_graph_can_return_nodes(graph_json):
    graph = g.Graph.from_json(graph_json)

    assert set(graph.get_nodes()) == {'A', 'B', 'C', 'D', 'E', 'F'}


def test_build_graph_can_remove_node_connections(graph_json):
    graph = g.Graph.from_json(graph_json)
    graph.remove_node_connections('C')

    expected_dictionary = {
        'A': ['B'],
        'B': ['A', 'D'],
        'C': [],
        'D': ['B', 'F'],
        'E': ['F'],
        'F': ['E', 'D']
    }

    assert graph.as_dict() == expected_dictionary
