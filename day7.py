import re

def readrules(rules):
    with open(rules, 'r') as reader:
        return [re.sub('\n', '', x) for x in reader.readlines()]


def bagsdict(rules):
    bags_dict = {}
    for rule in readrules(rules):
        colors = ['_'.join(re.split(' ', x)[-3:-1]) for x in re.split('bags|bag', rule)][:-1]
        bags_dict[colors[0]] = []
        for color in colors[1:]:
            if color != 'no_other':
                bags_dict[colors[0]].append(color)
    return bags_dict


def bag_parents(rules, my_color):
    bags_dict = bagsdict(rules)
    parents = []
    climb = True
    prev_parents_len = 0
    while climb == True:
 
        if len(parents) == 0:
            children = [my_color]

        else:
            children = parents

        for color in children:

            for k,v in zip(bags_dict.keys(), bags_dict.values()):

                if color in v and k not in parents:
                    parents.append(k)
            
        if len(parents) > prev_parents_len:
            prev_parents_len = len(parents)

        else:
            climb = False
            return len(set(parents))

print(bag_parents('inputs/07/test_a.txt', 'shiny_gold'))
print(bag_parents('inputs/07/input_a.txt', 'shiny_gold'))


def bag_children(rules, my_color):
    scores = {}
    rules_list = readrules(rules)

    while my_color not in scores.keys():

        for rule in rules_list:

            if len(re.findall('no', rule)) > 0:

                scores[re.sub(' ', '_', re.split(' bag| bags', rule)[0])] = 0

            else:

                colors = ['_'.join(re.split(' ', x)[-3:-1]) for x in re.split('bags|bag', rule)][:-1]

                # try/ except parent score, add to scores
                try:
                    scores[colors[0]] = sum([int(re.findall('\d', re.split(re.sub('_',' ', x), rule)[0])[-1]) * (scores[x] + 1) for x in colors[1:]])

                except:
                    pass

    return scores[my_color]


print(bag_children('inputs/07/test_a.txt', 'shiny_gold'))
print(bag_children('inputs/07/input_a.txt', 'shiny_gold'))
