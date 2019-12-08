import csv

from collections import deque
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
def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)


def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i


shortest_path = find_shortest_path(bidirectional_orbits, '8NZ', 'J2F')
shortest_path = list(flatten(shortest_path))
number_orbital_transers = (len(shortest_path) - 1)

print(f'Number of orbital transfers is {number_orbital_transers}')
