import re

def readseq(file_name):
    with open(file_name, 'r') as reader:
       return [int(i) for i in re.split(",",[i.strip() for i in reader.readlines()][0])]

def memory_game(file_name, endpoint):
    
    l = readseq(file_name)

    n_dict = {}

    for i, n in zip(range(len(l)), l):

        n_dict[n] = [i]

    last  = l[-1]

    for i in range(len(l), endpoint):

        if len(n_dict[last]) == 1:

            n = 0

        else:

            n = n_dict[last][-1] - n_dict[last][-2]

        last = n

        if last in n_dict.keys():

            n_dict[last].append(i)
        
        else:
            n_dict[last] = [i]

    for k, v in n_dict.items():

        if v[-1] == endpoint - 1:

            return k

for c, v in zip(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    [1, 10, 27, 78, 438, 1836, 436]
):
    print(memory_game(f'inputs/15/test_{c}.txt', 2020) == v)

print(memory_game('inputs/15/input.txt', 30000000))

