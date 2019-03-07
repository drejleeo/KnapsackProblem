'''
5. STEEPEST ASCENT HILL-CLIMBING(SAHC)
    1.Se selecteaza un punct aleator c(current hilltop) in spatiul de cautare.
    2.Se determinatoate punctele x din vecinatatea lui c: x apartine lui N(c)
    3.Daca oricare x apartine N(c) are un fitness mai bun decat c atunci c=x , unde x are cea mai buna valoare eval(x).
    4.Daca nici un punct x apartine N(c) nu are un fitness mai bun decat c, se salveaza si se trece la pasul 1.
    Altfel, se trece la pasul 2 cu noul c.
    5.Dupa un numar maxim de evaluari, se returneaza cel mai bun c(hilltop).
'''
from utils import load_data_to_instance, base_path, generate_binary_solution
from models import Object, HypothesisBag, Knapsack
import sys


def sahc(current_hilltop, searching_area):

    neighbourhood = get_neighbours(current_hilltop)
    best = find_best_neighbour(neighbourhood, searching_area)
    if best > current_hilltop:
        sahc(best, searching_area)
    else:
        return current_hilltop


def get_neighbours(current_hill_top):
    neighbourhood = [
        flip_bit(current_hill_top, bit_index) for bit_index in range(len(bin_sol))
    ]
    neighbourhood.insert(0, current_hill_top)
    return neighbourhood


def find_best_neighbour(neighbourhood, searching_area):
    processed_neighbourhood = process_neighbours(neighbourhood, searching_area)
    return max(neighbour.quality for neighbour in processed_neighbourhood)


def process_neighbours(neighbourhood, searching_area):
    processed = [
        Knapsack(
            binary_solution=neighbour,
            hypothesis_bag=searching_area,
            max_weight=max_weight,
        ) for neighbour in neighbourhood
    ]
    return processed


def flip_bit(bin_nr, bit):
    if bin_nr[bit] == '0':
        bin_nr = '{}1{}'.format(bin_nr[:bit], bin_nr[bit+1:])
    elif bin_nr[bit] == '1':
        bin_nr = '{}0{}'.format(bin_nr[:bit], bin_nr[bit+1:])
    return bin_nr


if __name__ == '__main__':
    given_runtimes, file_rel = int(sys.argv[1]), sys.argv[2]
    solutions = []
    all_objects, max_weight = load_data_to_instance(file_path='/'.join((base_path, file_rel)))
    hypothesis_bag = HypothesisBag(all_objects, max_weight)

    for run in range(given_runtimes):
        bin_sol = generate_binary_solution(len(hypothesis_bag.list))
        sol = sahc(
            current_hilltop=bin_sol,
            searching_area=hypothesis_bag,
        )
        solutions.append(sol)
    for sol in solutions:
        print(sol)
