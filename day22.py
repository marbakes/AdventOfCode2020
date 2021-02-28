def parse_hands(file_name):
    with open(file_name, 'r') as reader:
        seq = [i.strip() for i in reader.readlines()]

    return [int(i) for i in seq[1:seq.index('')]], [int(i) for i in seq[seq.index('') + 2:]]

def final_score(hand):

    return sum([(len(hand) - i) * c for i,c in enumerate(hand)])

def play_cards(hands, recursive):

    p1, p2 = hands

    hands_dict = {
        'p1': [],
        'p2': []
    }

    while len(p1) > 0 and len(p2) > 0:

        if p1 in hands_dict['p1'] and p2 in hands_dict['p2']:

            return 1

        else:

            hands_dict['p1'].append(p1.copy())
            hands_dict['p2'].append(p2.copy())

        wins = [p1[0], p2[0]]

        for p in p1, p2:
            p.pop(0)

        if recursive and wins[0] <= len(p1) and wins[1] <= len(p2):

            if play_cards([p1.copy()[:wins[0]], p2.copy()[:wins[1]]], True) == 1:

                p1.extend(wins)

            else:

                p2.extend(wins[::-1])

        else:

            if wins[0] > wins[1]:

                p1.extend(wins)

            else:

                p2.extend(wins[::-1])

    for p, i in  zip([p1, p2], [1, 2]):
        if len(p) > 0:
            print(final_score(p))
            return i

print(play_cards(parse_hands('inputs/22/test_a.txt'), True))
print()
print(play_cards(parse_hands('inputs/22/input.txt'), True))