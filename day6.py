import re
def batchdocs(batch, set_mode):
    with open(batch, 'r') as reader:
        if set_mode:
            return [re.sub('\n','', x) for x in re.split('\n\n', reader.read())]

        else:
            return [re.split('\n',x) for x in re.split('\n\n', reader.read())]
            
def customs_q(input):

    sum_q = 0
    for group in batchdocs(input, True):
        sum_q += len(set(group))

    return sum_q

print(customs_q('inputs/06/test_a.txt'))
print(customs_q('inputs/06/input_a.txt'))

def customs_q2(input):

    sum_q = 0
    for group, groupset in zip(batchdocs(input, False), [set(i) for i in batchdocs(input, True)]):
        if len(group)  == 1:
            sum_q += len(groupset)
        else:
            for char in groupset:
                all_answer = True
                for item in group:
                    if char not in item:
                        all_answer = False
                if all_answer:
                    sum_q += 1
    return sum_q

print(customs_q2('inputs/06/test_a.txt'))
print(customs_q2('inputs/06/input_a.txt'))