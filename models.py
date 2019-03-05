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
        self.__list_of_objects = []
        self.__nr_of_objects = 0

    @property
    def list_of_objects(self):
        return self.__list_of_objects

    @property
    def nr_of_objects(self):
        return self.__nr_of_objects

    def put_in_sack(self, new_thing):
        self.__list_of_objects.append(new_thing)
        self.__nr_of_objects += 1

    def __str__(self):
        return 'sack with {} objects'.format(self.nr_of_objects)


class Solution(object):
    def __init__(self, binary_solution, weight, quality, sack):
        self.__binary_solution = binary_solution
        self.__weight = weight
        self.__quality = quality

    @property
    def weight(self):
        return self.__weight

    @property
    def quality(self):
        return self.__quality

    @property
    def binary_solution(self):
        return self.__binary_solution

    @property
    def sol_len(self):
        return len(self.__binary_solution)
