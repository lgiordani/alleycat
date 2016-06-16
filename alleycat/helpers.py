import random


def insert_multiple_values(adict, key, value):
    """This checks if the dictionary already contains the key. If not it
    sets the key with an empty list as value. Then inserts the new value."""

    if key not in adict:
        adict[key] = []

    if value not in adict[key]:
        adict[key].append(value)


def get_random_couples(num, values):
    return [random.sample(values, 2) for i in range(num)]
