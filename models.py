"""
Artificial intelligence - Lab1
Author: Leonte Andrei
"""


class Object(object):
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


class HypothesisBag(object):
    def __init__(self, list, max_weight):
        self.__list = list
        self.__max_weight = max_weight

    @property
    def list(self):
        return self.__list

    @property
    def max_weight(self):
        return self.__max_weight

    def add_object(self, object):
        self.__list.append(object)
