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


class Knapsack(HypothesisBag):
    def __init__(self, binary_solution, hypothesis_bag, max_weight):
        super(Knapsack, self).__init__(list, max_weight)
        self.__binary = binary_solution

        self.__total_weight = 0
        self.__quality = 0
        for index in range(len(hypothesis_bag.list)):
            self.__total_weight += hypothesis_bag.list[index].weight * int(self.__binary[index])
            self.__quality += hypothesis_bag.list[index].value * int(self.__binary[index])

    @property
    def binary(self):
        return self.__binary

    @property
    def total_weight(self):
        return self.__total_weight

    @property
    def quality(self):
        return self.__quality

    @property
    def is_valid(self):
        if self.total_weight <= self.max_weight:
            return True
        else:
            return False

    def __str__(self):
        return 'Random combination with combinatoric binary: {}'.format(self.binary)
