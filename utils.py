from models import Object, HypothesisBag
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


def load_data_to_instance(file_path):

    with open(file_path, 'r') as file:
        total_number = int(file.readline())

        objects_list = []
        for index in range(total_number):

            parsed = list(map(int, file.readline().split()))
            obj = Object(value=parsed[1], weight=parsed[2])

            objects_list.append(obj)

        weight_limit = int(file.readline())

    return objects_list, weight_limit


def output_excel(nr_of_objects, default_sack, given_runtimes, solutions):
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d_%H-%M-%f")

    workbook = xlsxwriter.Workbook('.'.join((str(current_date), 'xlsx')))
    worksheet = workbook.add_worksheet()

    # Prepare headers
    worksheet.set_column(0, 0, 38)
    cell_format = workbook.add_format({'bold': True, 'color': '#03293A'})

    for index in range(nr_of_objects):
        worksheet.write(index + 1, 0, '{}. {}'.format(index + 1, default_sack.list_of_objects[index]), cell_format)
    worksheet.write(nr_of_objects + 1, 0, 'Total weight', cell_format)
    worksheet.write(nr_of_objects + 2, 0, 'Quality', cell_format)
    worksheet.write(nr_of_objects + 3, 0, 'Greatest quality', cell_format)
    for index in range(given_runtimes):
        worksheet.write(0, index + 1, 'Run {}'.format(index + 1), cell_format)

    # Mark used objects for the solution
    for run_nr in range(given_runtimes):
        binary_sol = solutions[run_nr].binary_solution
        for bit_index in range(len(binary_sol)):
            if binary_sol[bit_index] == '1':
                worksheet.write(bit_index + 1, run_nr + 1, 'x')

    # Write total weight and value to file
    for index in range(given_runtimes):
        worksheet.write(nr_of_objects + 1, index + 1, solutions[index].weight)
        worksheet.write(nr_of_objects + 2, index + 1, solutions[index].quality)

    MAX = max([sol.quality for sol in solutions])

    cell_format = workbook.add_format({'align': 'center'})
    worksheet.merge_range(nr_of_objects + 3, 1, nr_of_objects + 3, given_runtimes, MAX, cell_format)

    workbook.close()
