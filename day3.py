def treecrash(map, vx, vy):

    with open(map, 'r') as reader:

        map_list = [i.strip() for i in reader.readlines()]

    px = 0
    py = 0
    trees = 0

    while py < len(map_list):

        if map_list[py][px] == '#':

            trees +=1

        px = (px + vx) % (len(map_list[0]))
        py = py + vy

    return trees



print(treecrash('inputs/03/test_a.txt', 3, 1))
print(treecrash('inputs/03/input_a.txt', 3, 1))

def slopes(map):

    n = 1

    for slope in [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]:
        n = n * treecrash(map, slope[0], slope[1])

    return n

print(slopes('inputs/03/test_a.txt'))
print(slopes('inputs/03/input_a.txt'))