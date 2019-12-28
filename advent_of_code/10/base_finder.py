import csv
import math

from collections import namedtuple
from typing import List, Tuple


input_file = 'puzzle_input.csv'

asteroid_region = []

with open(input_file, 'r') as csvfile:
    inputs = csv.reader(csvfile, delimiter='\t')
    for row in inputs:
        asteroid_region.append(row[0])

asteroids = []

Asteroid = namedtuple('Asteroid', 'x y')
for y, row in enumerate(asteroid_region):
    for x, possible_asteroid in enumerate(row):
        if possible_asteroid == '#':
            asteroids.append(Asteroid(x=x, y=y))

class Vector:
    def __init__(self, asteroid):
        self.x = asteroid.x
        self.y = asteroid.y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
        
    def __abs__(self):
        return math.hypot(self.x, self.y)
        
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def angle(self):
        return math.atan2(self.y, self.x)


def offset_point_by_origin(origin: Asteroid, point_to_offset: Asteroid) -> Asteroid:
    return Asteroid(x = point_to_offset.x - origin.x, y = point_to_offset.y - origin.y)


most_seen = float('-inf')
winning_asteroid = None
for asteroid in asteroids:
    vectors = [Vector(offset_point_by_origin(asteroid, asteroid_to_compare)) for asteroid_to_compare in asteroids
               if asteroid_to_compare is not asteroid]
    asteroids_seen = len(set([vector.angle() for vector in vectors]))
    if asteroids_seen > most_seen:
        most_seen = asteroids_seen
        winning_asteroid = asteroid


print(f'Winning asteroid is: {winning_asteroid}')
print(f'Asteroids can be seen: {most_seen}')
