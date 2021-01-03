import re
def readlines(file_name):
    with open(file_name, 'r') as reader:
       return [i.strip() for i in reader.readlines()]


def bitmask(mask, value):
   
    return int(''.join([i if j == 'X' else j for i, j in zip(f'{value:036b}', mask)]), 2)

def mad(mask, address):

    new_address = ''
   
    for i, j in zip(f'{address:036b}', mask):

# If the bitmask bit is 0, the corresponding memory address bit is unchanged.
        if j == '0':
            new_address += i
# If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
        elif j == '1':
            new_address += '1'
# If the bitmask bit is X, the corresponding memory address bit is floating.
        else:
            new_address += 'X'

    substr = re.split("X", new_address)

    address_list = [substr[0]]

    for s in substr[1:]:

        for i in range(len(address_list)):

            address_list.append(address_list[i] + '0' + s)
            address_list[i] += ('1' + s)

    return address_list


def docking(file_name, new_version):

    p = readlines(file_name)

    mem = {

    }

    for l in p:

        if 'mask' in l:

            m = l[7:]

        else:

            a, v = [int(i) for i in re.split("\D", l) if i != '']

            if new_version:

                for a in mad(m, a):
                    mem[a] = v

            else:

                mem[a] = bitmask(m, v)

    return sum([i for i in mem.values()])


print(docking('inputs/14/test_a.txt', False))
print(docking('inputs/14/input.txt', False))

print(docking('inputs/14/test_b.txt', True))
print(docking('inputs/14/input.txt', True))