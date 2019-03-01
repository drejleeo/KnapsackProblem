from models import Nugat, Knapsack
import xlsxwriter
import os

base_path = os.getcwd()

def load_data(file_path):
    sack = Knapsack()

    with open(file_path, 'r') as file:
        total_number = int(file.readline())
        for index in range(total_number):

            parsed = list(map(int, file.readline().split()))
            object = Nugat(value=parsed[1], weight=parsed[2])

            sack.put_in_knapsack(object)

        weight_limit = int(file.readline())

    return (total_number, sack, weight_limit)

def output_excel():
    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet = workbook.add_worksheet()

