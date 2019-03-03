from utils import load_data, base_path, output_excel
import sys
from random import randint


def run(nr_of_objects, default_sack, weight_limit,  given_runtimes):
    solutions = []

    while given_runtimes:
        random_solution = randint(0, 2**nr_of_objects)
        binary_solution = '{0:b}'.format(random_solution)
        reversed_binary = binary_solution[::-1]
        weight = 0
        quality = 0

        for index in range(len(reversed_binary)):
            if reversed_binary[index] == '1':
                objects = default_sack.list_o
                weight += objects[nr_of_objects-1-index].weight
                quality += objects[nr_of_objects-1-index].value

        if weight <= weight_limit:
            given_runtimes -= 1
            solutions.append((binary_solution, quality, weight))
            print(binary_solution, quality, weight)

    return solutions


if __name__ == '__main__':
    given_runtimes, file_rel = int(sys.argv[1]), sys.argv[2]
    total_objects, default_sack, limit = load_data(file_path='/'.join((base_path, file_rel)))
    solutions = run(
        nr_of_objects=total_objects,
        default_sack=default_sack,
        weight_limit=limit,
        given_runtimes= given_runtimes,
    )
    output_excel(nr_of_objects=total_objects, objects=default_sack,  given_runtimes=given_runtimes, solutions=solutions)