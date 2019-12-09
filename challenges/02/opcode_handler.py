import csv
import copy
from typing import List, Tuple


def morpher(original_list: List[int], index: int) -> Tuple[List[str], int]:
    first = original_list[index + 1]
    second = original_list[index + 2]
    third = original_list[index + 3]
    new_index = index + 4
    if original_list[index] is 1:
        original_list[third] = original_list[first] + original_list[second]
    else:
        original_list[third] = original_list[first] * original_list[second]
    return original_list, new_index


def handle_input(input_list: List[str], int_to_match) -> str:
    original_list = [int(str_num) for str_num in input_list]
    list_copy = copy.deepcopy(original_list)

    list_index = 0
    while original_list[list_index] is not 99:
        list_copy, list_index = morpher(list_copy, list_index)
        if list_copy[0] == int_to_match:
            print('Found!')
            print(f'{list_copy[list_index - 4]}, {list_copy[list_index - 3]}, {list_copy[list_index - 2]}, {list_copy[list_index - 1]}')
            return 0
        list_copy = original_list
    return 1


inputs_list = []
with open('puzzle_input.csv') as csvfile:
    inputs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in inputs:
        inputs_list += row


checked = 0
for i in range(100):
    for j in range(100):
        copy_list = copy.deepcopy(inputs_list)
        copy_list[1] = str(i)
        copy_list[2] = str(j)
        if handle_input(copy_list, 19690720) is 0:
            print(f'noun is {i}')
            print(f'verb is {j}')
