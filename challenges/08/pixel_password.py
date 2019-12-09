import csv


pixel_width = 25
pixel_height = 6

pixel_string = ''
with open('puzzle_input.csv') as csvfile:
    inputs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in inputs:
        pixel_string = row[0]

number_of_pixels = int(len(pixel_string) / (pixel_width * pixel_height))

pixel_dict = {}
for i in range(0, number_of_pixels):
    pixel_list = []
    for j in range(0, pixel_height):
        pixel_list.append(pixel_string[:pixel_width])
        pixel_string = pixel_string[pixel_width:]
    pixel_dict[i] = pixel_list


fewest = float('inf')
pixel_with_fewest = None
for key, value in pixel_dict.items():
    number_of_zeroes = 0
    for pixel_row in value:
        number_of_zeroes += pixel_row.count('0')
    if number_of_zeroes < fewest:
        pixel_with_fewest = value
        fewest = number_of_zeroes

number_of_ones = 0
number_of_twos = 0

for pixel_row in pixel_with_fewest:
    number_of_ones += pixel_row.count('1')
    number_of_twos += pixel_row.count('2')

assert pixel_string == ''

print(f'Number of ones is {number_of_ones}')
print(f'Number of twos is {number_of_twos}')
print(f'Multiplied it is {number_of_ones * number_of_twos}')