"""
Artificial intelligence - Lab1
Author: Leonte Andrei
"""

class Nugat(object):
    def __init__(self, value, weight):
        self.__value = value
        self.__weight = weight

    @property
    def value(self):
        return self.__value

    @property
    def weight(self):
        return self.__weight

    def __repr__(self):
        return 'Object with value {} and weight {}'.format(self.value, self.weight)


class Knapsack(object):
    def __init__(self):
        self.pile_of_things = []

    def put_in_knapsack(self, new_thing):
        self.pile_of_things.append(new_thing)

    def __str__(self):
        return 'Knapsack!? what did u expect?'


if __name__ == '__main__':
    pass
