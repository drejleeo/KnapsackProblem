from utils import load_data, base_path, output_excel
import sys
from models import Solution
from random import randint


def run(nr_of_objects, default_sack, weight_limit,  given_runtimes):

    solutions = []
    while given_runtimes:
        random_solution = randint(0, 2**nr_of_objects)
        binary = '{0:b}'.format(random_solution)
        binary_solution = (default_sack.nr_of_objects - len(binary)) * '0' + binary
        weight = 0
        quality = 0

        for obj_index in range(default_sack.nr_of_objects):
            if binary_solution[obj_index] == '1':
                weight += default_sack.list_of_objects[obj_index].weight
                quality += default_sack.list_of_objects[obj_index].value

        if weight <= weight_limit:
            given_runtimes -= 1
            solutions.append(
                Solution(binary_solution, weight, quality)
            )
            print(binary_solution, weight, quality)

    return solutions


if __name__ == '__main__':
    given_runtimes, file_rel = int(sys.argv[1]), sys.argv[2]
    total_objects, default_sack, limit = load_data(file_path='/'.join((base_path, file_rel)))

    solutions = run(
        nr_of_objects=total_objects,
        default_sack=default_sack,
        weight_limit=limit,
        given_runtimes=given_runtimes,
    )
    output_excel(nr_of_objects=total_objects, default_sack=default_sack,  given_runtimes=given_runtimes, solutions=solutions)
