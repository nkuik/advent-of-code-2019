import csv
import math
import time
import functools

from collections import deque, namedtuple, OrderedDict
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


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s' % (elapsed, name))
        return result
    return clocked

# @functools.lru_cache()
class Vector:
    __slots__ = ('_x', '_y')

    def __init__(self, asteroid):
        self._x = asteroid.x
        self._y = asteroid.y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self._x, self._y)
        
    def __abs__(self):
        return math.hypot(self._x, self._y)
        
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self._x + other.x
        y = self._y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self._x * scalar, self._y * scalar)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def angle(self):
        return math.atan2(self._y, self._x)


def offset_point_by_origin(origin: Asteroid, point_to_offset: Asteroid) -> Asteroid:
    return Asteroid(x = point_to_offset.x - origin.x, y = point_to_offset.y - origin.y)

@clock
def find_best_asteroid(asteroids) -> Tuple[Asteroid, int]:
    most_seen = float('-inf')
    winning_asteroid = None
    for asteroid in asteroids:
        vectors = [Vector(offset_point_by_origin(asteroid, asteroid_to_compare)) for asteroid_to_compare in asteroids
                   if asteroid_to_compare is not asteroid]
        asteroids_seen = len(set([vector.angle() for vector in vectors]))
        if asteroids_seen > most_seen:
            most_seen = asteroids_seen
            winning_asteroid = asteroid
    return winning_asteroid, most_seen

winning_asteroid, most_seen = find_best_asteroid(asteroids)
print(f'Winning asteroid is: {winning_asteroid}')
print(f'Number of asteroids that can be seen: {most_seen}')

def vaporize_asteroids(base_location, asteroids) -> List[Tuple[Asteroid, Vector]]:
    od = OrderedDict()
    beginning_angle = -1.5707963267948966
    vectors = [(asteroid, Vector(offset_point_by_origin(base_location, asteroid))) 
               for asteroid in asteroids
               if asteroid is not base_location]
    vectors.sort(key=lambda x: x[1].angle())
    vector_queue = deque(vectors)
    vector_queue.rotate(-119)
    for vector in vector_queue:
        if not od.get(vector[1].angle()):
            od[vector[1].angle()] = [vector]
        else:
            od[vector[1].angle()].append(vector)
    
    vapo_order = []
    
    list_of_vectors = [value for key, value in od.items()]
    longest_vector = max(len(vector_list) for vector_list in list_of_vectors)

    for i in range (longest_vector):
        for vector_list in list_of_vectors:
            try:
                vapo_order.append(vector_list[i])
            except:
                pass

    return vapo_order

vapo_order = vaporize_asteroids(winning_asteroid, asteroids)

vapo_200 = vapo_order[199]

print(f'200 is {vapo_200}')
