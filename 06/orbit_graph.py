import csv

from typing import Dict

orbits = []

with open('puzzle_input.csv', 'r') as csvfile:
    inputs = csv.reader(csvfile, delimiter='\t')
    for row in inputs:
        orbits += row


direct_orbits = {}
indirect_orbits = {}
for orbit in orbits:
    origin = orbit.split(')')[0]
    orbiter = orbit.split(')')[1]
    if origin not in direct_orbits:
        direct_orbits[origin] = []
    direct_orbits[origin].append(orbiter)
    indirect_orbits[orbiter] = origin


def find_all_orbits(orbit_dict: Dict, origin: str) -> int:
    if origin not in orbit_dict:
        return 0
    return 1 + find_all_orbits(orbit_dict, orbit_dict[origin])


total_orbits = 0
for planet in indirect_orbits.keys():
    total_orbits += find_all_orbits(indirect_orbits, planet)


print(f'Total orbits is {total_orbits}')
