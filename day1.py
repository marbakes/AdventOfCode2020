def sorted_entries(entries):
    with open(entries, 'r') as reader:
        entries_list = [int(i.strip()) for i in reader.readlines()]
    entries_list.sort()
    return entries_list


def expensereport(entries, checksum):
    
    entries_list = sorted_entries(entries)

    while len(entries_list) > 1: 

        c = entries_list[0] + entries_list[-1]
        
        if c == checksum:
            return entries_list[0] * entries_list[-1]

        elif c > checksum:
            entries_list.pop(-1)

        else:
            entries_list.pop(0)




print(expensereport('inputs/01/test_a.txt', 2020))

print(expensereport('inputs/01/input_a.txt', 2020))

def initialize_points(bisect, entries_list):

    if bisect * 2 < len(entries_list):
        s = 0
        m = bisect - 1
        l = bisect
    else:
        s = 0
        m = bisect - 2
        l = bisect - 1
    
    return s, m, l

def triexpensereport(entries, checksum):

    entries_list = sorted_entries(entries)

    for i in range(len(entries_list)):
        if entries_list[i] > checksum / 2:
            bisect = i
            break

    s, m, l = initialize_points(bisect, entries_list)

    while l < len(entries_list):
        while m > s:
            c = entries_list[s] + entries_list[m] + entries_list[l]

            if c == 2020:
                return entries_list[s] * entries_list[m] * entries_list[l]
            
            elif c < 2020:
                s += 1
            
            else:
                m -= 1

        entries_list.pop(l)
        s, m, l = initialize_points(bisect, entries_list)

print(triexpensereport('inputs/01/test_a.txt', 2020))
print(triexpensereport('inputs/01/input_a.txt', 2020))





