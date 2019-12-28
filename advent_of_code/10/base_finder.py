import csv
import math

from typing import List, Tuple


input_file = 'test_input.csv'

asteroid_region = []

with open(input_file, 'r') as csvfile:
    inputs = csv.reader(csvfile, delimiter='\t')
    for row in inputs:
        asteroid_region.append(row[0])

asteroids = []

y_total = 0
x_total = 0

for y, row in enumerate(asteroid_region):
    for x, possible_asteroid in enumerate(row):
        if possible_asteroid == '#':
            asteroids.append((x, y))
        x_total = x
    y_total = y

diameter = (2 * y_total) + (2 * x_total)
corners = [(0, 0), (x_total, 0), (0, y_total), (x_total, y_total)]
possible_slopes = []

y_middle_index = int(math.floor(y_total / 2))
x_middle_index = int(math.floor(x_total / 2))


def find_lowest_common_denominator(input_num: int) -> int:
    all_denominators = []
    for i in range (2, input_num + 1):
        if input_num % i is 0:
            all_denominators.append(i)
    return all_denominators[0]

print(find_lowest_common_denominator(14))


def find_distance_between_points(point_a: Tuple, point_b: Tuple) -> float:
    return math.sqrt(((point_a[0] - point_b[0]) ** 2) + ((point_a[1] - point_b[1]) ** 2))


def point_is_on_line(startpoint: Tuple, endpoint: Tuple, point_in_question: Tuple) -> bool:
    return (
        (find_distance_between_points(startpoint, point_in_question) + find_distance_between_points(point_in_question, endpoint)) == find_distance_between_points(startpoint, endpoint)
    )


def find_points_on_same_path(origin: List[Tuple], 
                             points: List[Tuple], 
                             endpoints: List[Tuple]) -> List[List]:
    result = []
    result.append([point for point in points if point[0] == origin[0]
                   and point[1] < origin[1]])
    result.append([point for point in points if point[0] == origin[0]
                   and point[1] > origin[1]])
    result.append([point for point in points if point[1] == origin[1]
                   and point[1] < origin[1]])
    result.append([point for point in points if point[1] == origin[1]
                   and point[1] > origin[1]])
    result = [same_axis for same_axis in result if same_axis]
    for endpoint in endpoints:
        endpoint_path = []
        for point in points:
            if (point is origin or point is endpoint
                or point in result[0]):
                continue
            # if condition that they are on the same path
            if point_is_on_line(origin, endpoint, point):
                endpoint_path.append(point)
        if endpoint in points:
            endpoint_path.append(endpoint)
        result.append(endpoint_path)
    return result

endpoints = {}
for asteroid in asteroids:
    path_endpoints = []
    x_tops = [0, x_total]
    y_sides = [0, y_total]
    for x in range(0, (x_total + 1)):
        for y in range(0, (y_total + 1)):
            path_endpoints.append((x, y))
    edges = [pair for pair in path_endpoints 
             if pair[0] in x_tops or pair[1] in y_sides
             and pair != asteroid]
    if asteroid[1] == 0:
        # do not take top row
        edges = [edge for edge in edges if edge[1] != 0]
    if asteroid[0] == x_total:
        # do not take right side
        edges = [edge for edge in edges if edge[0] != x_total]
    if asteroid[0] == 0:
        # do not take left side
        edges = [edge for edge in edges if edge[0] != 0]
    if asteroid[1] == y_total:
        # do not take bottom
        edges = [edge for edge in edges if edge[1] != y_total]

    for corner in corners:
        if corner not in edges:
            edges.append(corner)
    if asteroid in corners:
        edges.remove(asteroid)
    endpoints[asteroid] = edges

most_seen = float('-inf')
point_with_most_seen = None
for asteroid, endpoints in endpoints.items():
    asteroids_seen = find_points_on_same_path(asteroid, asteroids, endpoints)
    if len(asteroids_seen) > most_seen:
        most_seen = len(asteroids_seen)
        point_with_most_seen = asteroid

print(most_seen)
print(point_with_most_seen)