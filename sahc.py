'''
5. STEEPEST ASCENT HILL-CLIMBING(SAHC)
    1.Se selecteaza un punct aleator c(current hilltop) in spatiul de cautare.
    2.Se determinatoate punctele x din vecinatatea lui c: x apartine lui N(c)
    3.Daca oricare x apartine N(c) are un fitness mai bun decat c atunci c=x , unde x are cea mai buna valoare eval(x).
    4.Daca nici un punct x apartine N(c) nu are un fitness mai bun decat c, se salveaza si se trece la pasul 1.
    Altfel, se trece la pasul 2 cu noul c.
    5.Dupa un numar maxim de evaluari, se returneaza cel mai bun c(hilltop).
'''
from utils import get_quality, is_valid


def sahc(current_hilltop, searching_area, iteration=0):
    neighbours = get_neighbours(current_hilltop)
    best = get_best_solution(neighbours, searching_area)

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


def get_neighbours(current_hilltop):
    neighbours = []
    for bit_index in range(len(current_hilltop)):
        flipped = flip_bit(current_hilltop, bit_index)
        if flipped:
            neighbours.append(flipped)
    return neighbours


def get_best_solution(neighbours, searching_area):
    quality = 0
    best = '0' * searching_area.total_objects
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


def get_better_solution(solution1, solution2, searching_area):
    quality1 = get_quality(solution1, searching_area)
    quality2 = get_quality(solution2, searching_area)
    if quality1 > quality2:
        return solution1
    return solution2
