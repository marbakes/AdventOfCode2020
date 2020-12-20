import re

def sums(numbers):

    sums_list = []

    for i in range(len(numbers)):

        sums_list.extend([numbers[i] + n for n in numbers[i+1:]])

    return set(sums_list)

def x_mas(numbers, pre_length):
    
    with open(numbers, 'r') as reader:

        xmas = [int(re.sub('\n', '', x)) for x in reader.readlines()]

    for i in range(pre_length, len(xmas)):
        
        if xmas[i] not in sums(xmas[i - pre_length:i]):

            return xmas[i]


def x_mas_summer(numbers, pre_length):

    n = x_mas(numbers, pre_length)

    with open(numbers, 'r') as reader:

       xmas = [int(re.sub('\n', '', x)) for x in reader.readlines()]

    xs = n - 1

    i = 0
    j = i + 1

    while xs != n:

        while xs < n and j < len(xmas):

            xs = sum(xmas[i:j])

            if xs == n:

                return min(xmas[i:j]) + max(xmas[i:j])

            elif xs > n:

                xs = n - 1

                break

            j += 1

        i += 1

print(x_mas_summer('inputs/09/test_a.txt', 5))
print(x_mas_summer('inputs/09/input_a.txt', 25))



