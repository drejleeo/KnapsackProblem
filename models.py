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


class Knapsack(object):
    def __init__(self):
        self.__list = []

    @property
    def list(self):
        return self.__list

    def add_object(self, object):
        self.__list.append(object)


class RandomCombinationData(object):
    def __init__(self, binary_solution, sack):
        self.__binary = binary_solution
        self.__total_weight = 0
        self.__quality = 0

        for index in range(sack.nr_of_objects):
            self.__total_weight += sack.list[index].weight * int(self.__binary[index])
            self.__quality += sack.list[index].value * int(self.__binary[index])

    @property
    def binary(self):
        return self.__binary

    @property
    def total_weight(self):
        return self.__total_weight

    def quality(self):
        return self.__quality

    def __str__(self):
        return 'Random combination with combinatoric binary: {}'.format(self.binary)


class Solutions(object):
    def __init__(self, max_weight):
        self.__list = []
        self.__max_weight = max_weight

    @classmethod
    def if_verifies_then_add(cls, possible_sol):
        inst = cls(cls.__max_weight)
        if possible_sol.weight <= cls.__max_weight:
            cls.__list.append(possible_sol)
        return inst

    def add(self, obj):
        self.__list.append(obj)
