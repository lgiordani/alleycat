import random

class Human(object):
    def __init__(self, position=None):
        self.visited_positions = []
        self.path = []
        self._set_position(position)

    def _set_position(self, position):
        self.position = position
        if position is not None:
            self.path.append(position)

    def travel(self, positions):
        good_positions = [i for i in positions if i != self.position and i not in self.visited_positions]

        if len(good_positions) == 0:
            # Safe to do because good_positions is never altered
            good_positions = positions

        self.visited_positions.append(self.position)
        self._set_position(random.choice(good_positions))

