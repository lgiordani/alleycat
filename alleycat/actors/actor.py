import random


class Actor(object):
    def __init__(self, position=None):
        self.path = []
        self._set_position(position)

    @property
    def moves(self):
        return len(self.path)

    def _set_position(self, position):
        self.position = position
        if position is not None:
            self.path.append(position)

    def travel(self, positions):
        if len(positions) > 0:
            self._set_position(random.choice(positions))
