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
import time


def sahc(current_hilltop, searching_area):

    neighbours = get_neighbours(current_hilltop)
    best = find_best_neighbour(neighbours, searching_area)
    current_quality = neighbour_intel(current_hilltop, searching_area)['quality']

    # print('{} <-- current hilltop with {}'.format(current_hilltop, current_quality))
    # for nei in neighbours:
    #     print('{} with intel: {}'.format(nei, neighbour_intel(nei, searching_area)))
    # print('\n')
    # print(best)
    best_quality = neighbour_intel(best, searching_area)['quality']
    # print('COMPARE best: {}      WITH     current: {}'.format(best_quality, current_quality))
    # print('\n\n')

    if best and best_quality > current_quality:
        return sahc(best, searching_area)
    else:
        return current_hilltop


def flip_bit(bin_nr, bit_index):
    if bin_nr[bit_index] == '0':
        bin_nr = '{}1{}'.format(bin_nr[:bit_index], bin_nr[bit_index+1:])
    else:
        return None
    return bin_nr


def get_neighbours(current_hilltop):
    neighbours = []
    for bit_index in range(len(bin_sol)):
        flipped = flip_bit(current_hilltop, bit_index)
        if flipped:
            neighbours.append(flipped)
    return neighbours


def find_best_neighbour(neighbours, searching_area):
    quality = 0
    best = '0' * len(searching_area.list)
    for full_intel in generate_neighbours_valid_intel(neighbours, searching_area):
        neighbour, intel = full_intel
        if intel['quality'] > quality:
            quality = intel['quality']
            best = neighbour
    return best


def generate_neighbours_valid_intel(neighbours, searching_area):
    for neighbour in neighbours:
        intel = neighbour_intel(binary_solution=neighbour, searching_area=searching_area)
        if intel:
            yield neighbour, intel


def neighbour_intel(binary_solution, searching_area):
    weight, quality = 0, 0
    for bit_index in range(len(searching_area.list)):
        weight += searching_area.list[bit_index].weight * int(binary_solution[bit_index])
        quality += searching_area.list[bit_index].value * int(binary_solution[bit_index])
        if weight > searching_area.max_weight:
            return None
    return {
        'weight': weight,
        'quality': quality,
    }


if __name__ == '__main__':
    start_time = time.time()
    given_runtimes, file_rel = int(sys.argv[1]), sys.argv[2]
    solutions = []
    all_objects, max_weight = load_data_to_instance(file_path='/'.join((base_path, file_rel)))
    hypothesis_bag = HypothesisBag(all_objects, max_weight)
    time2 = time.time()
    while given_runtimes:
        # print('\nRun {}\n'.format(given_runtimes))
        bin_sol = generate_binary_solution(len(hypothesis_bag.list))
        if neighbour_intel(binary_solution=bin_sol, searching_area=hypothesis_bag) is None:
            continue
        given_runtimes -= 1
        sol = sahc(
            current_hilltop=bin_sol,
            searching_area=hypothesis_bag,
        )
        solutions.append(sol)
    time3 = time.time()

    # for sol in solutions:
        # print(neighbour_intel(sol, hypothesis_bag))
    best_sol = find_best_neighbour(neighbours=solutions, searching_area=hypothesis_bag)
    print(best_sol, neighbour_intel(best_sol, hypothesis_bag))
    print('\n')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- {} seconds ---".format(time3 - time2))
