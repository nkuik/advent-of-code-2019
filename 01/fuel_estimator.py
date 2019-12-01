import csv
import math


def find_required_fuel(mass: int) -> int:
    required_fuel = math.floor(mass / 3) - 2
    if required_fuel <= 0:
        return 0
    return required_fuel + find_required_fuel(required_fuel)

fuel_measurements = []
with open('fuel_amounts.csv') as csvfile:
    fuelreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in fuelreader:
        fuel_measurements += row

fuel_measurements = [find_required_fuel(int(measurement))
                     for measurement in fuel_measurements]
final_sum = sum(fuel_measurements)

print(f'Fuel amount needed is: {final_sum}')
