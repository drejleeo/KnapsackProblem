from utils import get_hypothesis_from_file_input, base_path, \
    get_weight

if __name__ == '__main__':
    hypothesis = get_hypothesis_from_file_input(
        file_path='/'.join((base_path, 'input_files/input20.txt'))
    )
    hypothesis_sorted = sorted(
        hypothesis.list, key=lambda x: x.weight, reverse=False
    )

    greedy_weight, greedy_q = 0, 0
    index = 0
    used_objects = []
    while greedy_weight + hypothesis_sorted[index].weight < hypothesis.max_weight:
        greedy_weight += hypothesis_sorted[index].weight
        greedy_q += hypothesis_sorted[index].value
        used_objects.append(hypothesis_sorted[index])
        index += 1
    for obj in used_objects:
        print(obj)
    print(greedy_weight, greedy_q)
