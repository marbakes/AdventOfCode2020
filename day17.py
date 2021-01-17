def parse_grid(file_name):

    with open(file_name, 'r') as reader:

        return [i.strip() for i in reader.readlines()]

def my_neighbors(x, y, z, cubes_dict):

    n = 0

    for z_p in [i for i in range(z - 1, z + 2) if i in range(min(cubes_dict.keys()), max(cubes_dict.keys()) + 1)]:
            for y_p in [i for i in range(y - 1, y + 2) if i in range(0, len(cubes_dict[z]))]:
                    for x_p in [i for i in range(x - 1, x + 2) if i in range(0, len(cubes_dict[z][y]))]:

                            if cubes_dict[z_p][y_p][x_p] == '#' and (x_p, y_p, z_p) != (x, y, z):

                                n += 1

    return n

def conway_cubes(file_name, iterations):

    cubes_dict = {
        0: parse_grid(file_name)
    }

    for i in range(iterations):

        for z in cubes_dict.keys():
            for y in range(len(cubes_dict[z])):

                cubes_dict[z][y] = '.' + cubes_dict[z][y] + '.'

        for z in cubes_dict.keys():

            cubes_dict[z].insert(0, cubes_dict[0][0].replace('#', '.'))
            cubes_dict[z].append(cubes_dict[z][0])


        for k in [min(cubes_dict.keys()) - 1, max(cubes_dict.keys()) + 1]:

            cubes_dict[k] = [i.replace("#", '.') for i in cubes_dict[0]]

        new_cubes_dict = {k:[i for i in v] for k, v in cubes_dict.items()}

        for z in cubes_dict.keys():
            for y in range(len(cubes_dict[z])):
                for x in range(len(cubes_dict[z][y])):

                    n = my_neighbors(x, y, z, cubes_dict)

                    if cubes_dict[z][y][x] == '#' and n not in (2, 3):
                            
                            new_cubes_dict[z][y] = new_cubes_dict[z][y][0:x] + '.' + new_cubes_dict[z][y][x + 1:]

                    elif n == 3:
                            
                            new_cubes_dict[z][y] = new_cubes_dict[z][y][0:x] + '#' + new_cubes_dict[z][y][x + 1:]

        cubes_dict = {k:[i for i in v] for k, v in new_cubes_dict.items()}

    sum_active = 0
    for v in cubes_dict.values():

        for y in v:
            sum_active += y.count('#')

    return sum_active


print(conway_cubes('inputs/17/test_a.txt', 6))
print(conway_cubes('inputs/17/input.txt', 6))


def my_hyperneighbors(x, y, z, w, cubes_dict):

    n = 0

    for w_p in [i for i in range(w - 1, w + 2) if i in range(min(cubes_dict.keys()), max(cubes_dict.keys()) + 1)]:
        for z_p in [i for i in range(z - 1, z + 2) if i in range(min(cubes_dict[w].keys()), max(cubes_dict[w].keys()) + 1)]:
                for y_p in [i for i in range(y - 1, y + 2) if i in range(0, len(cubes_dict[w][z]))]:
                        for x_p in [i for i in range(x - 1, x + 2) if i in range(0, len(cubes_dict[w][z][y]))]:

                                if cubes_dict[w_p][z_p][y_p][x_p] == '#' and (x_p, y_p, z_p, w_p) != (x, y, z, w):

                                    n += 1

    return n


def conway_hypercubes(file_name, iterations):

    cubes_dict = {
        0: {
            0: parse_grid(file_name)
        }
    }

    for i in range(iterations):
        
        for w in cubes_dict.keys():
            for z in cubes_dict[w].keys():
                for y in range(len(cubes_dict[w][z])):

                    cubes_dict[w][z][y] = '.' + cubes_dict[w][z][y] + '.'

        for w in cubes_dict.keys():
            for z in cubes_dict[w].keys():

                cubes_dict[w][z].insert(0, cubes_dict[0][0][0].replace('#', '.'))
                cubes_dict[w][z].append(cubes_dict[w][z][0])

        for w in cubes_dict.keys():
            for k in [min(cubes_dict[w].keys()) - 1, max(cubes_dict[w].keys()) + 1]:

                cubes_dict[w][k] = [i.replace("#", '.') for i in cubes_dict[w][0]]

        for w in [min(cubes_dict.keys()) - 1, max(cubes_dict.keys()) + 1]:
            cubes_dict[w] = {k: [i.replace("#", '.') for i in v] for k, v in cubes_dict[0].items()}

        new_cubes_dict = {w:{k:[i for i in v] for k, v in cubes_dict[w].items()} for w in cubes_dict.keys()}

        for w in cubes_dict.keys():
            for z in cubes_dict[w].keys():
                for y in range(len(cubes_dict[w][z])):
                    for x in range(len(cubes_dict[w][z][y])):

                        n = my_hyperneighbors(x, y, z, w, cubes_dict)

                        if cubes_dict[w][z][y][x] == '#' and n not in (2, 3):
                                
                                new_cubes_dict[w][z][y] = new_cubes_dict[w][z][y][0:x] + '.' + new_cubes_dict[w][z][y][x + 1:]
                                
                        elif n == 3:
                                
                                new_cubes_dict[w][z][y] = new_cubes_dict[w][z][y][0:x] + '#' + new_cubes_dict[w][z][y][x + 1:]

        cubes_dict = {w:{k:[i for i in v] for k, v in new_cubes_dict[w].items()} for w in cubes_dict.keys()}


    sum_active = 0
    for v in cubes_dict.values():
        for z in v.values():
            for y in z:
                sum_active += y.count('#')

    return sum_active

print(conway_hypercubes('inputs/17/test_a.txt', 6))
print(conway_hypercubes('inputs/17/input.txt', 6))