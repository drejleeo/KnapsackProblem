import random


from utils import generate_binary_solution, is_valid


def genetik(population_size, number_of_generations, crossover_probability, mutation_probability, searching_area):

    # initialise population with random candidate solutions
    for individual in population_size:
        individual = generate_binary_solution(searching_area.total_objects)
        individual = solution_to_valid(individual, searching_area)

    # evaluate each candidate

    # repeat until (number_of_generations runs out)
    for generation in range(number_of_generations):
        # select parents

        # crossover: recombine pairs of parents

        # mutate the resulting offspring

        # evaluate new candidates

        # select individuals for the next generation

    pass


def probability_list(population):



def roulette_wheel():


def solution_to_valid(binary_solution, searching_area):
    if is_valid(binary_solution, searching_area):
        return binary_solution
    else:
        objects_in_sack = [
            index for index in range(binary_solution) if binary_solution[index] == '1'
        ]
        while not is_valid(binary_solution, searching_area):
            rand_obj = random.choice(objects_in_sack)
            binary_solution = flip_bit(binary_solution, rand_obj)
            objects_in_sack.remove(rand_obj)


def flip_bit(binary, bit_index):
    return '{}0{}'.format(binary[:bit_index], binary[bit_index + 1:])


if __name__ == '__main__':
    print()
