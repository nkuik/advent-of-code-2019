import csv

from typing import Dict

orbits = []

with open('puzzle_input.csv', 'r') as csvfile:
    inputs = csv.reader(csvfile, delimiter='\t')
    for row in inputs:
        orbits += row


bidirectional_orbits = {}
indirect_orbits = {}
for orbit in orbits:
    origin = orbit.split(')')[0]
    orbiter = orbit.split(')')[1]

    if origin not in bidirectional_orbits:
        bidirectional_orbits[origin] = []
    if orbiter not in bidirectional_orbits:
        bidirectional_orbits[orbiter] = []

    bidirectional_orbits[origin].append(orbiter)
    bidirectional_orbits[orbiter].append(origin)

    indirect_orbits[orbiter] = origin


def find_all_orbits(orbit_dict: Dict, origin: str) -> int:
    if origin not in orbit_dict:
        return 0
    return 1 + find_all_orbits(orbit_dict, orbit_dict[origin])


total_orbits = 0
for planet in indirect_orbits.keys():
    total_orbits += find_all_orbits(indirect_orbits, planet)

# From: https://www.python.org/doc/essays/graphs/
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


shortest_path = find_shortest_path(bidirectional_orbits, 'YOU', 'SAN')


print(f'Total orbits is {total_orbits}')
