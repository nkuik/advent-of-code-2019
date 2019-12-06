import csv
import math

from typing import Tuple, List
# DONE: Find points where paths cross
# TODO: Calculate shortest distance between them


def draw_line(line: str, starting_coords: Tuple[int, int]) -> Tuple[List[Tuple[int,int]], Tuple[int,int]]:
    direction = line[:1]
    length = int(line.partition(direction)[2])

    move_from = 0
    if direction in ['R', 'L']:
        move_from = starting_coords[0]
    else:
        move_from = starting_coords[1]

    path_coords = []
    new_coords = None
    for _ in range(length):
        if direction == 'R':
            move_from += 1
            new_coords = (move_from, starting_coords[1])
        elif direction == 'L':
            move_from -= 1
            new_coords = (move_from, starting_coords[1])
        elif direction == 'U':
            move_from += 1
            new_coords = (starting_coords[0], move_from)
        else:
            move_from -= 1
            new_coords = (starting_coords[0], move_from)
        path_coords.append(new_coords)

    return path_coords, new_coords


def draw_path(all_lines: List) -> List[Tuple[int, int]]:
    entire_path = []
    starting_point = (0, 0)
    for line in all_lines:
        line_coords, starting_point = draw_line(line, starting_point)
        entire_path += line_coords
    
    return entire_path


paths = []
with open('path_input.csv') as csvfile:
    inputs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for path in inputs:
        paths.append(path)


drawn_paths = {}
path_number = 1
for path in paths:
    drawn_paths[path_number] = draw_path(path)
    path_number += 1


def calculate_true_distance(coordinates: Tuple[int, int]) -> int:
    return math.sqrt((coordinates[0] ** 2) + (coordinates[1] ** 2))


intersections = list(set(drawn_paths[1]) & set(drawn_paths[2]))

shortest_path = float('inf')
closest_coordinates = None
for intersection in intersections:
    true_distance = calculate_true_distance(intersection)
    manhattan_distance = abs(intersection[0]) + abs(intersection[1])
    if manhattan_distance < shortest_path:
        shortest_path = manhattan_distance
        closest_coordinates = intersection

print(f'Shortest distance is {shortest_path}')
print(f'Closest coordinate pair is {closest_coordinates}')