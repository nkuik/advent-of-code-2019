import csv
import copy

from typing import Dict, List

pixel_width = 25
pixel_height = 6

pixel_string = ''
with open('puzzle_input.csv') as csvfile:
    inputs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in inputs:
        pixel_string = row[0]

number_of_pixels = int(len(pixel_string) / (pixel_width * pixel_height))

pixel_string_copy = copy.deepcopy(pixel_string)               

def create_pixel_dict(num_of_pixels: int, 
                      pixel_height: int, 
                      pixel_width: int, 
                      pixel_string: str) -> List:
   
    pixel_dict = {}
    for i in range(0, num_of_pixels):
        pixel_list = []
        for _ in range(0, pixel_height):
            str_to_list = list(pixel_string[:pixel_width])
            pixel_list.append(str_to_list)
            pixel_string = pixel_string[pixel_width:]
        pixel_dict[i] = pixel_list
    assert pixel_string == ''
    return pixel_dict

def create_final_pixel(row_height: int, 
                       row_length: int, 
                       pixel_dict: Dict) -> List[List]:
    final_pixel = []

    for i in range(0, row_height):
        final_pixel.append([None for i in range(0, row_length)]) 

    for pixel_number, pixel_rows in pixel_dict.items():
        for row_index, pixel_row in enumerate(pixel_rows):
            for pixel_index, pixel in enumerate(pixel_row):
                final_pixel[row_index][pixel_index]
                if (final_pixel[row_index][pixel_index] is None
                    or final_pixel[row_index][pixel_index] == '2'):
                    final_pixel[row_index][pixel_index] = pixel
    
    return final_pixel

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i


pixel_dict = create_pixel_dict(number_of_pixels,
                               pixel_height,
                               pixel_width,
                               pixel_string_copy)


test_width = 2
test_height = 2

test_string = ''
with open('test_input.csv') as csvfile:
    inputs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in inputs:
        test_string = row[0]

test_pixel_num = int(len(test_string) / (test_width * test_height))

test_pixel_dict = create_pixel_dict(test_pixel_num,
                                    test_height,
                                    test_width,
                                    test_string)
test_final_pixel = create_final_pixel(test_height, test_width, test_pixel_dict)
print(f"Test pixel is {''.join(flatten(test_final_pixel))}")

final_pixel = create_final_pixel(pixel_height, pixel_width, pixel_dict)
final_message = ''
for pixel_row in final_pixel:
    final_message += f"{''.join(pixel_row)}\n".replace('0', ' ')
print(final_message)
print(f"Final pixel is {''.join(flatten(final_pixel))}")

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


print(f'Number of ones is {number_of_ones}')
print(f'Number of twos is {number_of_twos}')
print(f'Multiplied it is {number_of_ones * number_of_twos}')