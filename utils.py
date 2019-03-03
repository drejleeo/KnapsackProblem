from models import Nugat, Knapsack
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
import os
from datetime import datetime

base_path = os.getcwd()


def load_data(file_path):
    sack = Knapsack()

    with open(file_path, 'r') as file:
        total_number = int(file.readline())
        for index in range(total_number):

            parsed = list(map(int, file.readline().split()))
            obj = Nugat(value=parsed[1], weight=parsed[2])

            sack.put_in_knapsack(obj)

        weight_limit = int(file.readline())

    return total_number, sack, weight_limit


def output_excel(nr_of_objects, objects,  given_runtimes, solutions):
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d_%H-%M-%f")

    workbook = xlsxwriter.Workbook('.'.join((str(current_date), 'xlsx')))
    worksheet = workbook.add_worksheet()

    worksheet.set_column(0, 0, 38)
    cell_format = workbook.add_format({'bold': True})

    for index in range(nr_of_objects):
        worksheet.write(index + 1, 0, '{}. {}'.format(index + 1, objects.list_o[index]), cell_format)
    worksheet.write(nr_of_objects + 1, 0, 'Total weight', cell_format)
    worksheet.write(nr_of_objects + 2, 0, 'Total value', cell_format)
    worksheet.write(nr_of_objects + 3, 0, 'Greatest quality', cell_format)
    for index in range(given_runtimes):
        worksheet.write(0, index + 1, 'Run {}'.format(index + 1), cell_format)

    for run_nr in range(given_runtimes):
        binary_sol = solutions[run_nr][0]
        index = len(binary_sol) - 1

        while index >= 0:
            if binary_sol[index] == '1':
                worksheet.write(index + 1, run_nr + 1, 'x')
            index -= 1

    for index in range(given_runtimes):
        worksheet.write(nr_of_objects + 1, index + 1, solutions[index][2])
        worksheet.write(nr_of_objects + 2, index + 1, solutions[index][1])

    # cell = xl_rowcol_to_cell(nr_of_objects + 3, given_runtimes + 1)
    MAX = max([sol[1] for sol in solutions])

    cell_format = workbook.add_format({'align': 'center'})
    worksheet.merge_range(nr_of_objects + 3, 1, nr_of_objects + 3, given_runtimes, MAX, cell_format)


    workbook.close()
