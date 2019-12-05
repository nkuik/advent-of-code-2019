import csv

from typing import Tuple, List
# TODO: Find points where paths cross
# TODO: Calculate shortest distance between them


def draw_line(line: str, starting_coords: Tuple[int, int]) -> Tuple[List[Tuple[int,int]], Tuple[int,int]]:
    direction = line[:1]
    length = int(line.partition(direction)[2])

    path_coords = []

    move_from = 0
    if direction == 'R' or direction == 'L':
        move_from = starting_coords[0]
    else:
        move_from = starting_coords[1]

    ending_coords = None
    for _ in range(length):
        new_coord = None
        if direction == 'R':
            move_from += 1
            path_coords += (move_from, starting_coords[1])
            ending_coords = (move_from, starting_coords[1])
        elif direction == 'L':
            move_from -= 1
            path_coords += (move_from, starting_coords[1])
            ending_coords = (move_from, starting_coords[1])
        elif direction == 'U':
            move_from += 1
            path_coords += (starting_coords[0], move_from)
            ending_coords = (starting_coords[0], move_from)
        else:
            move_from -= 1
            path_coords += (starting_coords[0], move_from)
            ending_coords = (starting_coords[0], move_from)

    return path_coords, ending_coords



def draw_path(all_lines: List) -> List[Tuple[int, int]]:
    entire_path = []
    starting_point = (0, 0)
    for line in all_lines:
        line_coords, starting_point = draw_line(line, starting_point)
        entire_path += line_coords


paths = []
with open('path_input.csv') as csvfile:
    inputs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for path in inputs:
        paths.append(path)

for path in paths:
    draw_path(path)

