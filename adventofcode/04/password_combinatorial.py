input = '246540-787419'

password_parts = input.split('-')
first_part = password_parts[0]
second_part = password_parts[1]

def is_not_decreasing(num_str: str) -> bool:
    comparisons = []
    for i in range(len(num_str) - 1):
        comparisons.append(num_str[i] <= num_str[i + 1])
    return all(comparisons)


def has_double(num_str: str) -> bool:
    count = {}
    for number in num_str:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    over_two = any((val > 2 for val in count.values()))
    at_least_one = any((val == 2 for val in count.values()))
    if over_two and not at_least_one:
        return False
    if at_least_one:
        return True
    return False


checked_nums = {}
for num in range(int(first_part), int(second_part)):
    if num not in checked_nums:
        if all((is_not_decreasing(str(num)),
                has_double(str(num)))):
            checked_nums[num] = True
        else:
            checked_nums[num] = False


print(f'{sum(value is True for value in checked_nums.values())}')
