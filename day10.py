def sorted_entries(entries):
    with open(entries, 'r') as reader:
        entries_list = [int(i.strip()) for i in reader.readlines()]
    entries_list.sort()
    return entries_list

def adapters_diffs(entries):
    adapters = sorted_entries(entries)
    adapters.append(adapters[-1] + 3)
    adapters.insert(0,0)
 
    diffs = [(adapters[i] - adapters[i - 1]) for i in range(1, len(adapters))]

    return diffs.count(1) * diffs.count(3)

def adapter_combos(entries):

    adapters = sorted_entries(entries)
    adapters.insert(0, 0)
    combos = {
        adapters[0]: 1
    }

    for a in adapters[1:]:
        combos[a] = 0

    for a in adapters:
        for n in (1, 2 ,3):
            if a + n in adapters:
                combos[a + n] += combos[a]

    return combos[adapters[-1]]

print(adapter_combos('inputs/10/test_a.txt'))
print(adapter_combos('inputs/10/test_b.txt'))
print(adapter_combos('inputs/10/input_a.txt'))