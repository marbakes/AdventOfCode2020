import re
def parse_ingredients(file_name):

    lines = {}

    with open(file_name, 'r') as reader:

        for i, l in enumerate(reader.readlines()):

            lines[i] = {
                'ingredients': re.split(' ', re.split("contains", l.strip())[0])[:-1],
                'allergens': [re.sub(' ', '', x) for x in re.split(',', re.sub("\)", "", re.split("contains", l.strip())[1]))]
            }

    return lines


def safe_foods(file_name):

    ing_dict = parse_ingredients(file_name)

    allergens = set([x for v in ing_dict.values() for x in v['allergens']])
    ingredients = [x for v in ing_dict.values() for x in v['ingredients']]

    potential_allergens = []

    for a in allergens:

        potential_allergens.extend(set.intersection(*[set(x) for x in [v['ingredients'] for v in ing_dict.values() if a in v['allergens']]]))

    potential_allergens = list(set(potential_allergens))

    return len([x for x in ingredients if x not in potential_allergens])

print(safe_foods('inputs/21/test_a.txt'))
print(safe_foods('inputs/21/input.txt'))


def isolate_allergens(file_name):

    
    ing_dict = parse_ingredients(file_name)
    all_dict = {}

    allergens = list(set([x for v in ing_dict.values() for x in v['allergens']]))
    alpha = allergens.copy()
    alpha.sort()

    while len(allergens) > 0:

        for a in allergens:

            potential_allergens = set.intersection(*[set(x) for x in [v['ingredients'] for v in ing_dict.values() if a in v['allergens']]])

            if len(potential_allergens) == 1:
                all_dict[a] = ''.join(potential_allergens)
                allergens.remove(a)

                for v in ing_dict.values():
                    if all_dict[a] in v['ingredients']:
                        v['ingredients'].remove(all_dict[a])

    return ",".join([all_dict[a] for a in alpha])



print(isolate_allergens('inputs/21/test_a.txt'))
print(isolate_allergens('inputs/21/input.txt'))