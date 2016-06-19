import six

from alleycat.actors.actor import Actor


class Human(Actor):
    def __init__(self, name=None, position=None):
        if six.PY2:
            super(Human, self).__init__(name, position)
        else:
            super().__init__(name, position)
        self.visited_positions = []

    def travel(self, positions):
        good_positions = [i for i in positions if i != self.position and i not in self.visited_positions]

        if len(good_positions) == 0:
            # Safe to do because good_positions is never altered
            good_positions = positions

        self.visited_positions.append(self.position)
        if six.PY2:
            super(Human, self).travel(good_positions)
        else:
            super().travel(good_positions)
