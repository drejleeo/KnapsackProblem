from utils import load_data, base_path
import sys
from random import randint


def run(nr_of_objects, default_sack, weight_limit, sol_counter):

    while sol_counter:
        random_solution = randint(0, 2**nr_of_objects)
        binary_solution = '{0:b}'.format(random_solution)
        reversed_binary = binary_solution[::-1]
        weight = 0
        quality = 0

        for index in range(len(reversed_binary)):
            if reversed_binary[index] == '1':
                objects = default_sack.pile_of_things
                weight += objects[nr_of_objects-1-index].weight
                quality += objects[nr_of_objects-1-index].value

        if weight <= weight_limit:
            sol_counter -= 1
            print(binary_solution, 'Q: {}, W: {}'.format(quality, weight))


if __name__ == '__main__':
    sol_counter, file_rel = int(sys.argv[1]), sys.argv[2]
    total, default_sack, limit = load_data(file_path='/'.join((base_path, file_rel)))
    run(nr_of_objects=total, default_sack=default_sack, weight_limit=limit, sol_counter=sol_counter)

