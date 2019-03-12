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
from models import HypothesisBag
import sys
import time


def sahc(current_hilltop, searching_area, iteration=0):
    neighbours = get_neighbours(current_hilltop)
    best = find_best_neighbour(neighbours, searching_area)

    current_quality = get_quality(current_hilltop, searching_area)
    best_quality = get_quality(best, searching_area)
    # print('{} <-- current hilltop with {}'.format(current_hilltop, current_quality))
    # for nei in neighbours:
    #     print('{} with quality: {}, with weight: {}'.format(nei, get_quality(nei, searching_area), get_weight(nei, searching_area)))
    # print('\n')
    # print(best)
    # print('COMPARE best: {}      WITH     current: {}'.format(best_quality, current_quality))
    # print('\n\n')

    if best_quality > current_quality:
        return sahc(best, searching_area, iteration + 1)
    return current_hilltop, iteration


def flip_bit(base2, bit_index):
    if base2[bit_index] == '0':
        bin_nr = '{}1{}'.format(base2[:bit_index], base2[bit_index+1:])
    else:
        return None
    return bin_nr


def solution_to_valid(binary_solution, searching_area):
    if is_valid(binary_solution, searching_area):
        return binary_solution
    for index in range(len(binary_solution)):
        if binary_solution[index] == '1':
            binary_solution = '{}0{}'.format(binary_solution[:index], binary_solution[index + 1:])
            if is_valid(binary_solution, searching_area):
                return binary_solution


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
    for neighbour in generate_valid_neighbours(neighbours, searching_area):
        neigh_quality = get_quality(neighbour, searching_area)
        if neigh_quality > quality:
            quality = neigh_quality
            best = neighbour
    return best


def generate_valid_neighbours(neighbours, searching_area):
    for neighbour in neighbours:
        if is_valid(neighbour, searching_area):
            yield neighbour


def get_weight(binary_solution, searching_area):
    weight = 0
    for bit_index in range(len(searching_area.list)):
        weight += searching_area.list[bit_index].weight * int(binary_solution[bit_index])
    return weight


def get_quality(binary_solution, searching_area):
    quality = 0
    for bit_index in range(len(searching_area.list)):
        quality += searching_area.list[bit_index].value * int(binary_solution[bit_index])
    return quality


def is_valid(binary_solution, searching_area):
    weight = get_weight(binary_solution, searching_area)
    if weight <= searching_area.max_weight:
        return True
    return False


if __name__ == '__main__':
    start_time = time.time()
    iteration_limit, file_rel = int(sys.argv[1]), sys.argv[2]
    solutions = []
    all_objects, max_weight = load_data_to_instance(file_path='/'.join((base_path, file_rel)))
    hypothesis_bag = HypothesisBag(all_objects, max_weight)





    time2 = time.time()
    iteration_count = 0
    while iteration_count < iteration_limit:
        bin_sol = generate_binary_solution(len(hypothesis_bag.list))
        bin_sol = solution_to_valid(bin_sol, hypothesis_bag)
        sol, iteration = sahc(
            current_hilltop=bin_sol,
            searching_area=hypothesis_bag,
        )
        iteration_count += iteration

        solutions.append(sol)
    print(get_quality(find_best_neighbour(neighbours=solutions, searching_area=hypothesis_bag), hypothesis_bag))

    time3 = time.time()

    # for sol in solutions:
        # print(neighbour_intel(sol, hypothesis_bag))
    best_sol = find_best_neighbour(neighbours=solutions, searching_area=hypothesis_bag)
    print(best_sol, get_quality(best_sol, hypothesis_bag), get_weight(best_sol, hypothesis_bag))
    print('\n')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- {} seconds ---".format(time3 - time2))
