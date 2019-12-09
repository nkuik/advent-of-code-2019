import csv
import math

from typing import Tuple, List


class Point:
    def __init__(self, x, y, distance_traveled=None):
        self._x = x
        self._y = y
        self._distance_traveled = distance_traveled
        self._coordinates = (x, y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def distance_traveled(self):
        return self._distance_traveled

    def __str__(self):
        return f'{self.coordinates}'

    def __eq__(self, other_point):
        return self.coordinates == other_point.coordinates

    def __hash__(self):
        return hash(str(self))


class Line:

    def __init__(self, points=None):
        if points is None:
            self.points = []
        else:
            self.points = points


    def add_point(self, point: Point):
        self.points.append(point)

    @property
    def all_coordinates(self):
        return [point for point in self.points]

    @property
    def point_with_shortest_distance(self):
        return sorted(self.points, key=lambda x: x.distance_traveled)[0]


def calculate_true_distance(coordinates: Tuple[int, int]) -> int:
    return math.sqrt((coordinates[0] ** 2) + (coordinates[1] ** 2))


def draw_line(line_str: str,
              starting_point: Point,
              distance_traveled: int) -> Tuple[Line, Tuple[int,int], int]:
    new_line = Line()
    direction = line_str[:1]
    length = int(line_str.partition(direction)[2])

    move_from = 0
    if direction in ['R', 'L']:
        move_from = starting_point.x
    else:
        move_from = starting_point.y

    last_point = None
    for _ in range(length):
        distance_traveled += 1
        if direction == 'R':
            move_from += 1
            last_point = Point(move_from, starting_point.y, distance_traveled)
        elif direction == 'L':
            move_from -= 1
            last_point = Point(move_from, starting_point.y, distance_traveled)
        elif direction == 'U':
            move_from += 1
            last_point = Point(starting_point.x, move_from, distance_traveled)
        else:
            move_from -= 1
            last_point = Point(starting_point.x, move_from, distance_traveled)
        new_line.add_point(last_point)

    return new_line, last_point, distance_traveled


def draw_path(all_lines: List) -> List[Tuple[int, int]]:
    entire_path = []
    starting_point = Point(0, 0)
    distance_traveled = 0
    for line in all_lines:
        drawn_line, starting_point, distance_traveled = draw_line(line, starting_point, distance_traveled)
        entire_path += drawn_line.points

    return entire_path


paths = []
with open('path_input.csv') as csvfile:
    inputs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for path in inputs:
        paths.append(path)


drawn_paths = []
for path in paths:
    drawn_paths.append(draw_path(path))


first_path = Line()
for point in drawn_paths[0]:
    first_path.add_point(point)


second_path = Line()
for point in drawn_paths[1]:
    second_path.add_point(point)


intersections = Line(list(set(first_path.points) & set(second_path.points)))

first_intersections = [point for point in first_path.points if point in intersections.points]
second_intersections = [point for point in second_path.points if point in intersections.points]

matches = []

for point_a in first_intersections:
    for point_b in second_intersections:
        if point_a == point_b:
            matches.append((point_a, point_b))

shortest_distance = float('inf')
winning_pair = None
for point_pair in matches:
    total_distance = point_pair[0].distance_traveled + point_pair[1].distance_traveled
    if (total_distance) < shortest_distance:
        shortest_distance = total_distance
        winning_pair = point_pair


print(f'Shortest distance is {shortest_distance}')
