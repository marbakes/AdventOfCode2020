import re

def parse_lines(file_name):

    with open(file_name, 'r') as reader:

        lines = [i.strip() for i in reader.readlines()]

    return lines[0:lines.index('')], lines[lines.index('') + 1:]


def messages(file_name):

    rules, msgs = parse_lines(file_name)

    rules_dict = {r[0:r.index(':')] : " " + r[r.index(':') + 2:] + " " for r in rules}

    while re.findall('\d', rules_dict['0']) != []:

        for k, v in rules_dict.items():

            for n in set(re.findall('\d+', v)):
                
                    if re.findall("[a-z]", rules_dict[n]) != []:

                        rules_dict[k] = re.sub(" " + n + " ", " (" + rules_dict[n].replace("\"", "") + ") ", rules_dict[k])

    rule = rules_dict['0'].replace(" ", "")
    
    valid = 0

    for m in msgs:

        try:

            if re.search(rule, m).group() == m:
                
                valid += 1
                
            else:
                pass

        except:
            pass

    return valid



def messages_alt(file_name):

    rules, msgs = parse_lines(file_name)

    rules_dict = {r[0:r.index(':')] : " " + r[r.index(':') + 2:] + " " for r in rules}

    rules_dict['8'] = ' 42 | 42 8 '
    rules_dict['11'] = ' 42 31 | 42 11 31 '


    while (re.findall('\d', rules_dict['42']) != []) or (re.findall('\d', rules_dict['31']) != []):

        for k, v in rules_dict.items():

            if k in ('8', '11'):
                
                pass

            else:

                for n in set(re.findall('\d+', v)):
                    
                        if re.findall("[a-z]", rules_dict[n]) != []:

                            rules_dict[k] = re.sub(" " + n + " ", " (" + rules_dict[n].replace("\"", "") + ") ", rules_dict[k])

    rule_31, rule_42 = [rules_dict[x].replace(' ', '').replace("(", "(?:") for x in ('31', '42')]

    rule_0 = f"(({rule_42})+)(({rule_31})+)"
    
    valid = 0

    for m in msgs:

        try:

            if re.fullmatch(rule_0, m).group() == m:

                split = re.search(f"(({rule_42})+)", m).span()[1]

                if len(re.findall(rule_42, m[:split])) > len(re.findall(rule_31, m[split:])):

                    valid += 1

        except:

            pass

    return valid

print(messages('inputs/19/test_a.txt'))
print(messages('inputs/19/input.txt'))
print(messages('inputs/19/test_b.txt'))
print(messages_alt('inputs/19/test_b.txt'))
print(messages_alt('inputs/19/input.txt'))

