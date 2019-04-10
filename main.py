from genetic_algorithm.genetic import genetik
from utils import get_hypothesis_from_file_input, base_path, generate_binary_solution, \
    get_hypothesis_from_user_input, solution_to_valid, get_weight, get_quality, \
    output_excel, random_search
from sahc import sahc
import time
import datetime
import xlsxwriter


class App(object):

    def __init__(self, hypothesis=None):
        self._hypothesis = hypothesis
        self._load_token = False

    @property
    def hypothesis(self):
        return self._hypothesis

    @hypothesis.setter
    def hypothesis(self, new):
        self._hypothesis = new

    @staticmethod
    def print_menu_options():
        print('\n======================================')
        print('0. Program input')
        print('1. File input')
        print('2. SAHC')
        print('3. Random search')
        print('4. Genetic algorithm')
        print('Ctrl+C to terminate\n')

    def option_user_input(self):
        try:
            self.hypothesis = get_hypothesis_from_user_input()
        except ValueError:
            print('Incorrect input.')
            return
        self.load_token = True

    def option_file_input(self):
        file_rel = input('Enter file relative path: ')
        self._hypothesis = get_hypothesis_from_file_input(
            file_path='/'.join((base_path, file_rel))
        )
        self._load_token = True

    def option_start_sahc(self):
        iteration_limit = int(input('Enter iteration_limit for algorithm: '))
        quality_sum = 0
        best = '0' * self._hypothesis.total_objects
        solutions = []
        total_found_solutions = 0

        iteration_count = 0

        current_date = datetime.datetime.now()
        current_date = current_date.strftime("%Y-%m-%d_%H-%M-%f")

        start_time = time.time()
        while iteration_count < iteration_limit:

            bin_sol = generate_binary_solution(self._hypothesis.total_objects)
            bin_sol = solution_to_valid(bin_sol, self._hypothesis)
            sol, iteration = sahc(
                current_hilltop=bin_sol,
                searching_area=self._hypothesis,
            )
            solutions.append(sol)
            iteration_count += iteration
            total_found_solutions += 1

            if get_quality(sol, self._hypothesis) > get_quality(best, self._hypothesis):
                best = sol

            quality_sum += get_quality(sol, self._hypothesis)
        print("--- {} seconds ---".format(time.time() - start_time))
        print("Total found solutions: {}".format(total_found_solutions))
        avg = quality_sum / total_found_solutions

        print('Average: {}, Best quality: {}, solution: {}'.format(avg, get_quality(best, self._hypothesis), 'best'))
        for sol in solutions:
            print('Quality: {}, Weight: {}'.format(
                get_quality(sol, self._hypothesis), get_weight(sol, self._hypothesis))
            )

    def option_start_rand(self):
        given_runtimes = int(input('Choose the number of solutions wanted: '))
        solutions = random_search(
            given_runtimes=given_runtimes,
            searching_area=self._hypothesis
        )
        output_excel(
            solutions=solutions,
            given_runtimes=given_runtimes,
            searched_area=self._hypothesis
        )

    def option_genetic_al(self):
        ps = int(input("Population size: "))
        ng = int(input("Number of generations: "))
        cp = int(input("Crossover probability: "))
        mp = int(input("Mutation probability: "))

        prototype = genetik(
            population_size=ps,
            number_of_generations=ng,
            crossover_probability=cp,
            mutation_probability=mp,
        )
        print(prototype)

    def run(self):

        map_options = {
            0: self.option_user_input,
            1: self.option_file_input,
            2: self.option_start_sahc,
            3: self.option_start_rand,
            4: self.option_genetic_al,
        }

        while True:
            self.print_menu_options()
            option = input('Enter option: ')
            if option.isdigit() is False:
                print('Incorrect option.')
                continue

            option = int(option)
            if option not in map_options.keys():
                print('Option not in range.')
                continue

            if option == 0 or option == 1 or self._load_token:
                map_options[option]()
            else: print('Option not available. Make sure you entered data or option exists')


if __name__ == '__main__':
    app = App()
    app.run()
