'''
5. STEEPEST ASCENT HILL-CLIMBING(SAHC)
    1.Se selecteaza un punct aleator c(current hilltop) in spatiul de cautare.
    2.Se determinatoate punctele x din vecinatatea lui c: x apartine lui N(c)
    3.Daca oricare x apartine N(c) are un fitness mai bun decat c atunci c=x , unde x are cea mai buna valoare eval(x).
    4.Daca nici un punct x apartine N(c) nu are un fitness mai bun decat c, se salveaza si se trece la pasul 1.
    Altfel, se trece la pasul 2 cu noul c.
    5.Dupa un numar maxim de evaluari, se returneaza cel mai bun c(hilltop).
'''
from utils import load_data, base_path, generate_binary_solution
from models import Nugat, Knapsack, Solution
import sys


def sahc(total_objects, default_sack, given_runtimes):
    for run in range(given_runtimes):
        sol = generate_binary_solution(total_objects)
        neighbourhood = [
            Solution(
                binary_solution=flip_bit(sol, bit),
                default_sack=default_sack
            ) for bit in range(total_objects)
        ]






def flip_bit(bin_nr, bit):
    if bin_nr[bit] == '0':
        bin_nr = '{}1{}'.format(bin_nr[:bit], bin_nr[bit+1:])
    elif bin_nr[bit] == '1':
        bin_nr = '{}0{}'.format(bin_nr[:bit], bin_nr[bit+1:])
    return bin_nr


if __name__ == '__main__':
    given_runtimes, file_rel = int(sys.argv[1]), sys.argv[2]
    total_objects, default_sack, limit = load_data(file_path='/'.join((base_path, file_rel)))
