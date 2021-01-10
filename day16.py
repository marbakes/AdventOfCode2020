import re

def parse_tickets(file_name):

    with open(file_name, 'r') as reader:

        lines = [i.strip() for i in reader.readlines()]

    a = {i.split(': ')[0]: [tuple([int(k) for k in j.split('-')]) for j in i.split(': ')[1].split(' or ')] for i in lines[0:lines.index('')]}

    b = tuple([int(i) for i in lines[lines.index('') + 2].split(',')])

    c = [tuple([int(i) for i in j.split(',')]) for j in lines[lines.index('') + 5:]]

    return a, b, c


def ticket_validate(file_name, new_mode):

    rules, mytic, tics = parse_tickets(file_name)

    error_rate = 0

    p_dict = {i:list(rules.keys()) for i in range(len(rules.keys()))}

    mytic_dict = {}

    for t in tics:

        for i, n in enumerate(t):

            n_slots = []

            for k, v in rules.items():
                
                n_slots.extend([k for r in v  if n in range(r[0], r[1] + 1)])

            if len(n_slots) > 0:

                p_dict[i] = [x for x in p_dict[i] if x in n_slots]

            else:

                error_rate += n

    if new_mode:

        dep_prod = 1

        while len(p_dict.keys()) != len(mytic_dict.keys()):

            for k, v in p_dict.items():

                if len(v) == 1:

                    mytic_dict[v[0]] = mytic[k]

                    for x in p_dict.values():

                        if x != v and v[0] in x:

                            x.remove(v[0])

        for k, v in mytic_dict.items():

            if 'departure' in k:
                
                dep_prod *= v

        return dep_prod

    else:

        return error_rate


print(ticket_validate('inputs/16/input.txt', False))
print(ticket_validate('inputs/16/input.txt', True))