from models import Object, Hypothesis
import xlsxwriter
import os
from datetime import datetime
from random import randint

base_path = os.getcwd()

def generate_binary_solution(nr_of_objects):
    superior_limit = 2 ** nr_of_objects
    random_solution = randint(0, superior_limit)
    binary = '{0:b}'.format(random_solution)
    binary_solution = (nr_of_objects - len(binary)) * '0' + binary
    return binary_solution


def is_valid(binary_solution, searching_area):
    weight = get_weight(binary_solution, searching_area)
    if weight <= searching_area.max_weight:
        return True
    return False


def solution_to_valid(binary_solution, searching_area):
    if is_valid(binary_solution, searching_area):
        return binary_solution
    for index in range(len(binary_solution)):
        if binary_solution[index] == '1':
            binary_solution = '{}0{}'.format(binary_solution[:index], binary_solution[index + 1:])
            if is_valid(binary_solution, searching_area):
                return binary_solution


def get_hypothesis_from_file_input(file_path):

    with open(file_path, 'r') as file:
        total_number = int(file.readline())

        objects_list = []
        for index in range(total_number):

            parsed = list(map(int, file.readline().split()))
            obj = Object(value=parsed[1], weight=parsed[2])

            objects_list.append(obj)

        weight_limit = int(file.readline())

    return Hypothesis(objects_list, weight_limit)


def get_hypothesis_from_user_input():
    length = int(input('Enter number of total objects: '))
    weight_limit = int(input('Sack weight limit: '))
    objs = []
    for inp in range(length):
        print('Object {}'.format(inp))
        value = int(input('\tObject value: '))
        weight = int(input('\tObject weight: '))
        obj = Object(value=value, weight=weight)
        objs.append(obj)
    hypothesis = Hypothesis(objs, weight_limit)
    return hypothesis


def get_weight(binary_solution, searching_area):
    weight = 0
    for bit_index in range(searching_area.total_objects):
        weight += searching_area.list[bit_index].weight * int(binary_solution[bit_index])
    return weight


def get_quality(binary_solution, searching_area):
    quality = 0
    for bit_index in range(searching_area.total_objects):
        quality += searching_area.list[bit_index].value * int(binary_solution[bit_index])
    return quality


def random_search(given_runtimes, searching_area):

    solutions = []
    while given_runtimes:
        bin_sol = generate_binary_solution(searching_area.total_objects)
        bin_sol = solution_to_valid(bin_sol, searching_area)
        solutions.append(bin_sol)
        given_runtimes -= 1
    return solutions


def output_excel(solutions, given_runtimes, searched_area):
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d_%H-%M-%f")

    workbook = xlsxwriter.Workbook('.'.join((str(current_date), 'xlsx')))
    worksheet = workbook.add_worksheet()

    # Prepare headers
    worksheet.set_column(0, 0, 38)
    cell_format = workbook.add_format({'bold': True, 'color': '#03293A'})

    for index in range(searched_area.total_objects):
        worksheet.write(index + 1, 0, '{}. {}'.format(index + 1, searched_area.list[index]), cell_format)
    worksheet.write(searched_area.total_objects + 1, 0, 'Total weight', cell_format)
    worksheet.write(searched_area.total_objects + 2, 0, 'Quality', cell_format)
    worksheet.write(searched_area.total_objects + 3, 0, 'Greatest quality', cell_format)
    for index in range(given_runtimes):
        worksheet.write(0, index + 1, 'Run {}'.format(index + 1), cell_format)

    # Mark used objects for the solution
    for run_nr in range(given_runtimes):
        binary_sol = solutions[run_nr]
        for bit_index in range(searched_area.total_objects):
            if binary_sol[bit_index] == '1':
                worksheet.write(bit_index + 1, run_nr + 1, 'x')

    # Write total weight and value to file
    for index in range(given_runtimes):
        worksheet.write(searched_area.total_objects + 1, index + 1, get_weight(solutions[index], searched_area))
        worksheet.write(searched_area.total_objects + 2, index + 1, get_quality(solutions[index], searched_area))

    MAX = max([get_quality(sol, searched_area) for sol in solutions])

    cell_format = workbook.add_format({'align': 'center'})
    worksheet.merge_range(
        first_row=searched_area.total_objects + 3,
        first_col=1,
        last_row=searched_area.total_objects + 3,
        last_col=given_runtimes,
        data=MAX,
        cell_format=cell_format
    )

    workbook.close()
