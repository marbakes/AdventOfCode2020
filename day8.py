import re

def readrules(rules):
    with open(rules, 'r') as reader:
        return [re.sub('\n', '', x) for x in reader.readlines()]


def accumulator(inst):
    acc = 0
    i = 0
    del_dict = {
        '+': 1,
        '-': -1
    }

    while i < len(inst):

        if "*" in inst[i]:

            return None

        else:

            if "jmp" in inst[i]:

                j = del_dict[re.findall('\+|\-', inst[i])[0]] * int(re.split('jmp ', inst[i])[1][1:])

            else:

                j = 1

                if "acc" in inst[i]:

                    acc += del_dict[re.findall('\+|\-', inst[i])[0]] * int(re.split('acc ', inst[i])[1][1:])

        
        inst[i] = "*" + inst[i]

        i = i + j

    return acc

def fix_acc(instructions):
    orig_inst = readrules(instructions)

    for x in [('nop', 'jmp'), ('jmp', 'nop')]:

        for i in [j for i, j in zip(orig_inst, range(len(orig_inst))) if len(re.findall(x[0], i)) == 1]:
            inst = orig_inst.copy()
            inst[i] = inst[i].replace(x[0], x[1])
            try: 
                return float(accumulator(inst))
            except:
                pass
        
print(fix_acc('inputs/08/test_a.txt'))
print(fix_acc('inputs/08/input_a.txt'))