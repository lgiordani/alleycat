import json

from alleycat import helpers as h


class Graph(object):
    def __init__(self, connections_list):
        self._connections = {}

        for connection in connections_list:
            self._set_connection(connection[0], connection[1])

    @classmethod
    def from_json(cls, json_content):
        connections = json.loads(json_content)

        return cls(connections)

    def _set_connection(self, start_node, end_node):
        h.insert_multiple_values(self._connections, start_node, end_node)
        h.insert_multiple_values(self._connections, end_node, start_node)

    def as_dict(self):
        return self._connections

    def get_nodes(self):
        return self._connections.keys()

    def get_node_neighbours(self, node_key):
        return self._connections[node_key]

    def remove_node_connections(self, node_key):
        self._connections[node_key] = []

        for key in self._connections:
            if node_key in self._connections[key]:
                self._connections[key].remove(node_key)
