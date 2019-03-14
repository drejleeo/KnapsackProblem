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


class Hypothesis(object):
    def __init__(self, objs_list, max_weight):
        self.__objs = objs_list
        self.__max_weight = max_weight
        self.__total_objs = len(objs_list)

    @property
    def list(self):
        return self.__objs

    @property
    def max_weight(self):
        return self.__max_weight

    @property
    def total_objects(self):
        return self.__total_objs

    @max_weight.setter
    def max_weight(self, value):
        if isinstance(self.__max_weight, int) and self.__max_weight > 0:
            self.__max_weight = value

    def add_object(self, object):
        self.__objs.append(object)
        self.__max_weight += 1
