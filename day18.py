import re

def parse_lines(file_name):

    with open(file_name, 'r') as reader:

        return [i.strip() for i in reader.readlines()]


def eval_string(s):

    while '+' in s or '*' in s:

        try:

            opspan = re.search('\+|\*', s).span()

            a = re.search('\d+', s[:opspan[0]]).group()

            b = re.search('\d+' ,s[opspan[1]:]).group()

            op = s[opspan[0]]
            
            if op == '*':

                c = int(a) * int(b)
            
            if op == '+':

                c = int(a) + int(b)

            s = s.replace(f"{a} {op} {b}", f"{c}", 1)

        except:
            
            return s

    return s


def eval_string_alt(s):

    for operator in ('+', '*'):

        while operator in s:

            try:

                opspan = re.search(re.escape(operator), s).span()

                a = re.search('\d+', s[:opspan[0]][::-1]).group()[::-1]

                b = re.search('\d+' ,s[opspan[1]:]).group()

                op = s[opspan[0]]
                
                if op == '*':

                    c = int(a) * int(b)
                
                elif op == '+':

                    c = int(a) + int(b)

                s = s.replace(f"{a} {op} {b}", f"{c}", 1)

            except:
                
                return s

    return s

def hw_answers(file_name):

    a = 0

    for l in parse_lines(file_name):

        q = l

        while '(' in l or ')' in l:

            s = re.search('\([^\(\)]+\)', l).group()

            l = l.replace(s, eval_string_alt(s[1:-1]))

        a += int(eval_string_alt(l))

    return a

print(hw_answers('inputs/18/test_a.txt'))
print(hw_answers('inputs/18/input.txt'))


