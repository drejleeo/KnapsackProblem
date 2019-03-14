from utils import generate_binary_solution, load_data, base_path,\
    output_excel
import sys
from models import Solutions, RandomCombinationData


def run(nr_of_objects, default_sack, weight_limit,  given_runtimes):

    solutions = Solutions(max_weight=weight_limit)
    while given_runtimes:
        bin_sol = generate_binary_solution(len(default_sack.list))
        combination_data = RandomCombinationData(
            binary_solution=bin_sol,
            sack=default_sack,
        )
        solutions.if_verifies_then_add(combination_data)
    return solutions


if __name__ == '__main__':
