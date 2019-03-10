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
from models import Object, HypothesisBag
import sys


def sahc(current_hilltop, searching_area):

    neighbourhood = get_neighbourhood(current_hilltop)
    best = find_best_neighbour(neighbourhood, searching_area)

    print('{} <-- current hilltop: qw: {}'.format(current_hilltop, neighbour_intel(current_hilltop, searching_area)))
    for n in neighbourhood:
        print('{} with{}'.format(n, neighbour_intel(n, searching_area)))
    print('\n\n\n')
    print('\n\n Quality {} \n\n'.format(neighbour_intel(best, searching_area)['quality']))

    if best != current_hilltop:
        sahc(best, searching_area)
    else:
        return current_hilltop


def get_neighbourhood(current_hilltop):
    neighbourhood = [
        flip_bit(current_hilltop, bit_index) for bit_index in range(len(bin_sol))
    ]
    neighbourhood.insert(0, current_hilltop)
    return neighbourhood


def flip_bit(bin_nr, bit_index):
    if bin_nr[bit_index] == '0':
        bin_nr = '{}1{}'.format(bin_nr[:bit_index], bin_nr[bit_index+1:])
    elif bin_nr[bit_index] == '1':
        bin_nr = '{}0{}'.format(bin_nr[:bit_index], bin_nr[bit_index+1:])
    return bin_nr


def find_best_neighbour(neighbourhood, searching_area):
    best = neighbourhood[0]
    quality = neighbour_intel(best, searching_area)['weight']
    for full_intel in generate_valid_neighbours_intel(neighbourhood, searching_area):
        neighbour, intel = full_intel
        if intel['quality'] > quality:
            quality = intel['quality']
            best = neighbour
    return best


def generate_valid_neighbours_intel(neighbours, searching_area):
    for neighbour in neighbours:
        intel = neighbour_intel(binary_solution=neighbour, searching_area=searching_area)
        if intel['weight'] <= searching_area.max_weight:
            yield neighbour, intel


def neighbour_intel(binary_solution, searching_area):
    weight, quality = 0, 0
    for bit_index in range(len(searching_area.list)):
        weight += searching_area.list[bit_index].weight * int(binary_solution[bit_index])
        quality += searching_area.list[bit_index].value * int(binary_solution[bit_index])
    return {
        'weight': weight,
        'quality': quality,
    }


if __name__ == '__main__':
    given_runtimes, file_rel = int(sys.argv[1]), sys.argv[2]
    solutions = []
    all_objects, max_weight = load_data_to_instance(file_path='/'.join((base_path, file_rel)))
    hypothesis_bag = HypothesisBag(all_objects, max_weight)

    for run in range(given_runtimes):
        print('\n\nRun {}:\n\n'.format(run))
        bin_sol = generate_binary_solution(len(hypothesis_bag.list))
        sol = sahc(
            current_hilltop=bin_sol,
            searching_area=hypothesis_bag,
        )
        solutions.append(sol)
        print('\n\n\n\n')
    for sol in solutions:
        print(sol)
