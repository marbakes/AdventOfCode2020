import time
def crab_cups(file_name, new_mode):

    with open(file_name, 'r') as reader:

        cups = [int(i) for i in[i.strip() for i in reader.readlines()][0]]
    
    m = max(cups)

    if new_mode:

        cups.extend(range(m + 1, 1000001))

        m = max(cups)

        n = 10000000
    
    else:

        n = 100

    l = len(cups)

    i = 0

    for _ in range(n):
        
        c = cups[i % l]

        p = []

        i_a = (i + 1) % l

        for j in range(3):

            if i_a < l - j:

                pop_index = i_a

            else:

                pop_index = 0

            p.append(cups.pop(pop_index))

        if c > 1:

            d = c - 1

        else:

            d = m

        while d in [c] + p:

            d -= 1

            if d < 1:
                
                d = m

        

        d_index = cups.index(d)

        

        for j in range(3):

            cups.insert(d_index + j + 1, p[j])

        

        i = cups.index(c) + 1


    if new_mode:
        return cups[(cups.index(1) + 1) % l] * cups[(cups.index(1) + 2) % l]
    else:
        while cups.index(1) != 0:
            first = cups[0]
            cups.pop(0)
            cups.append(first)       

        return ''.join([str(x) for x in cups[1:]])


print(crab_cups('inputs/23/test_a.txt', False))
print(crab_cups('inputs/23/input.txt',False))


def crab_cups_new(file_name, new_mode):

    with open(file_name, 'r') as reader:

        cups_list = [int(i) for i in[i.strip() for i in reader.readlines()][0]]
    
    m = max(cups_list)

    if new_mode:

        cups_list.extend(range(m + 1, 1000001))

        m = max(cups_list)

        n = 10000000
    
    else:

        n = 100
    
    l = len(cups_list)

    cups = {}

    for i in range(m):

        cups[cups_list[i]] = {
            -1: cups_list[(i - 1) % l],
            1: cups_list[(i + 1) % l]
        }

    c = cups_list[0]

    for _ in range(n):

        left = c

        p = []

        for _ in range(3):
            p.append(cups[left][1])
            left = p[-1]


        if c > 1:

            d = c - 1

        else:

            d = m

        while d in [c] + p:

            d -= 1

            if d < 1:
                
                d = m

        cups[c][1] = cups[p[-1]][1]
        cups[cups[d][1]][-1] = p[-1]
        cups[p[-1]][1] = cups[d][1]
        cups[d][1] = p[0]
        cups[p[0]][-1] = d

        c = cups[c][1]


    if new_mode:

        a = cups[1][1]
        b = cups[cups[1][1]][1]
        return a * b

    else:

        left = 1
        s = []
        for _ in range(l - 1):
            s.append(cups[left][1])
            left = s[-1]



        return ''.join([str(x) for x in s])

print(crab_cups_new('inputs/23/test_a.txt', True))
print(crab_cups_new('inputs/23/input.txt', True))

