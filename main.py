from utils import load_data_to_instance, base_path


def print_menu():
    print('0. Program input')
    print('1. File input')
    print('2. SAHC\n')
    print('Ctrl + C to terminate\n\n')


if __name__ == '__main__':

    load_token = False
    while True:
        print_menu()
        option = int(input('Enter option: '))
        if option == 0:
            # load_token = True
            pass
        elif option == 1:
            file_rel = input('Enter file relative path: ')
            hypothesis_bag = load_data_to_instance(
                file_path='/'.join((base_path, file_rel))
            )
            # load_token = True
        elif option == 2:
            iteration_limit = input('Enter iteration_limit for algorithm: ')

    solutions = []



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


    # for sol in solutions:
        # print(neighbour_intel(sol, hypothesis_bag))
    best_sol = find_best_neighbour(neighbours=solutions, searching_area=hypothesis_bag)
    print(best_sol, get_quality(best_sol, hypothesis_bag), get_weight(best_sol, hypothesis_bag))
    print('\n')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- {} seconds ---".format(time3 - time2))
