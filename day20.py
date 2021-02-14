def parse_tile_edges(file_name):

    with open(file_name, 'r') as reader:

        lines = [i.strip() for i in reader.readlines()]

    return {int(lines[i].replace("Tile ","").replace(":","")): [
        lines[i + 1],
        ''.join([lines[j][0] for j in range(i + 1, i + 11)]),
        lines[i + 10][::-1],
        ''.join([lines[j][9] for j in range(i + 1, i + 11)])[::-1]
    ] for i in range(0, len(lines), 12)}



def four_corners(file_name):

    edge_dict = parse_tile_edges(file_name)
    corner_prod = 1

    edges = [e for v in edge_dict.values() for e in v]
    edges.extend([e[::-1] for e in edges if e[:-1] not in edges])

    for k, v in edge_dict.items():

        if sum([edges.count(e) for e in v]) == 6:

            corner_prod *= k

    return corner_prod

print(four_corners('inputs/20/test_a.txt'))
print(four_corners('inputs/20/input.txt'))

def parse_tiles(file_name):

    with open(file_name, 'r') as reader:

        lines = [i.strip() for i in reader.readlines()]

    return {int(lines[i].replace("Tile ","").replace(":","")): lines[i + 1:i + 11] for i in range(0, len(lines), 12)}

def display_array(a):
    for l in a:
        print(l)
    print()

def mirror(tile):
    return [y[::-1] for y in tile]

def rotate(tile):
    return mirror([''.join([tile[y][x] for y in range(len(tile))]) for x in range(len(tile))])
    

def align(t1, t2, vert):

    if vert:

        return t1[-1] == t2[0]

    else:

        return rotate(t1)[-1] == rotate(t2)[0]


def tile_match(tile1, tile2, vert, const):

    for _ in range(2):

                if align(tile1, tile2, vert):

                    break

                else:

                    for _ in range(4):

                        if align(tile1, tile2, vert):

                            break

                        else:

                            if not const:
                            
                                tile1 = rotate(tile1)

                            for _ in range(2):

                                if align(tile1, tile2, vert):

                                    break

                                else:

                                    for _ in range(4):

                                        if align(tile1, tile2, vert):

                                            break

                                        else:

                                            tile2 = rotate(tile2)
                                    
                                    if align(tile1, tile2, vert):
                                        break
                                    else:
                                        tile2 = mirror(tile2)

                    if align(tile1, tile2, vert):
                        
                        break

                    else:

                        if not const:

                            tile1 = mirror(tile1)

    return tile1, tile2


def seamap(file_name):

    edge_dict = parse_tile_edges(file_name)
    tiles = parse_tiles(file_name)

    edges = [e for v in edge_dict.values() for e in v]
    edges.extend([e[::-1] for e in edges if e[:-1] not in edges])

    for k, v in edge_dict.items():

        if sum([edges.count(e) for e in v]) == 6:

            t = k
            edges = edge_dict[t]
            del edge_dict[t]
            break
    
    s = 0

    seq = [t]

    while len(edge_dict.keys()) > 0:

        match = False

        for splus in [2, 1, 1, 1]:

            s = (s + splus) % 4

            for k, v in edge_dict.items():

                for j, e in enumerate(v):

                    if edges[s] in (e, e[::-1]):

                        match = True
                        s = j
                        t = k
                        seq.append(t)
                        edges = edge_dict[t]
                        del edge_dict[t]

                        break

                if match:
                    break

            if match:
                break

    arr = {}

    i = 0
    j = 0

    x_bot = 0
    y_bot = x_bot

    x_top = int(len(seq) ** 0.5) - 1
    y_top = x_top

    while len(seq) > 0:

        for i_delt_in, j_delt_in, i_delt_out, j_delt_out, x_bot_delt, x_top_delt, y_bot_delt, y_top_delt in zip(

            [1, 0, -1, 0],
            [0, 1, 0, -1],
            [-1, -1, 1, 1],
            [1, -1, -1, 1],
            [0, 0, 0, 1],
            [0, 0, -1, 0],
            [0, 0, 1, 0],
            [0, 0, -1, 0]

        ):

            while i <= x_top and i >= x_bot and j <= y_top and j >= y_bot:

                if len(seq) == 0:

                    break

                try:

                    arr[j][i] = seq[0]

                except:

                    arr[j] = {i: seq[0]}
                
                seq.pop(0)

                i += i_delt_in
                j += j_delt_in

            i += i_delt_out
            j += j_delt_out

            x_bot += x_bot_delt
            x_top += x_top_delt
            y_bot += y_bot_delt
            y_top += y_top_delt

        if len(seq) == 0:
            break

    seq = list(arr.keys())
    seq.sort()


    for i in range(1):

        for m in range(len(seq)):
            
            c = arr[m][m]

            try:

                r = arr[m][m + 1]
                d = arr[m + 1][m]

                tiles[c], tiles[r] = tile_match(tiles[c], tiles[r], False, False)

                tiles[c], tiles[d] = tile_match(tiles[c], tiles[d], True, False)

                if not align(tiles[c], tiles[r], False) or not align(tiles[c], tiles[d], True):

                    tiles[c] = mirror(tiles[c])
                    tiles[d] = mirror(tiles[d])
                    tiles[c], tiles[r] = tile_match(tiles[c], tiles[r], False, False)

                for x in range(m + 1, len(seq) - 1):

                    c = arr[m][x]
                    r = arr[m][x + 1]
                    tiles[c], tiles[r] = tile_match(tiles[c], tiles[r], False, True)

                for y in range(m + 1, len(seq) - 1):

                    c = arr[y][m]
                    d = arr[y + 1][m]
                    tiles[c], tiles[d] = tile_match(tiles[c], tiles[d], True, True)

            except:

                c = arr[m - 1][m]
                d = arr[m][m]
                tiles[c], tiles[d] = tile_match(tiles[c], tiles[d], True, True)

    tiles = {k: [r[1:-1] for r in tiles[k][1:-1]] for k in tiles.keys()}

    w = int([len(i) for i in tiles.values()][0])
    
    s_map = []

    for y in seq:
        
        s_map.extend([''.join([tiles[arr[y][x]][i] for x in seq]) for i in range(w)])

    return s_map


def sea_monsters(file_name):

    s_map = seamap(file_name)

    with open('inputs/20/seamonster.txt', 'r') as reader:

        seamonster = [i.strip('\n') for i in reader.readlines()]

    for _ in range(2):

        for _ in range(4):

            m = 0

            for y in range(0, len(s_map) -  len(seamonster) - 1):

                for x in range(0, len(s_map) - len(seamonster[0]) - 1):

                    n = 0

                    region = [i[x:x + len(seamonster[0])] for i in s_map[y:y + len(seamonster)]]

                    for ry in range(0, len(seamonster)):
                        
                        for rx in range(0, len(seamonster[0])):

                            if region[ry][rx] == '#' and seamonster[ry][rx] == '#':

                                n = n + 1

                    if n == 15:

                        m += 1

                        for ry in range(0, len(seamonster)):
                            
                            for rx in range(0, len(seamonster[0])):

                                if seamonster[ry][rx] == '#':

                                    s_map[y + ry] = s_map[y + ry][0:x + rx] + '0' + s_map[y + ry][1 + x + rx:]

            if m > 0:

                return sum([r.count('#') for r in s_map])
            
            s_map = rotate(s_map)

        s_map = mirror(s_map)

    return sum([r.count('#') for r in s_map])

print(sea_monsters('inputs/20/test_a.txt'))
print(sea_monsters('inputs/20/input.txt'))