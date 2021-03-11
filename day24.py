import re

def parse_directions(file_name):
    with open(file_name) as reader:
        lines = [re.findall('se|sw|ne|nw|w|e', x.strip()) for x in reader.readlines()]

    return lines

hex_dict = {
    'e' : {
        'x': 2,
        'y': 0
    },
    'se' : {
        'x': 1,
        'y': 1
    },
    'sw' : {
        'x': -1,
        'y': 1
    },
    'w' : {
        'x': -2,
        'y': 0
    },
    'nw' : {
        'x': -1,
        'y': -1
    },
    'ne' : {
        'x': 1,
        'y': -1
    },
}

def pad_tiles(tile_dict):

    new_dict = {k: v for (k,v) in tile_dict.items()}
    
    for k in tile_dict.keys():

        for d in hex_dict.values():

            pad_coord = (k[0] + d['x'], k[1] + d['y'])

            if pad_coord not in new_dict.keys():

                new_dict[pad_coord] = 0

    return new_dict

def my_neighbors(tile_dict, coord):

    count = 0

    for d in hex_dict.values():

            pad_coord = (coord[0] + d['x'], coord[1] + d['y'])

            try:

                if tile_dict[pad_coord] > 0:

                    count += 1

            except:

                pass

    return count

def tile_flips(file_name):

    directions = parse_directions(file_name)

    tiles = []

    for line in directions:
        x = 0
        y = 0
        for l in line:
            
            x += hex_dict[l]['x']
            y += hex_dict[l]['y']

        tiles.append((x,y))

    tile_dict = {t:(tiles.count(t) % 2) for t in set(tiles)}

    print(sum(tile_dict.values()))

    for _ in range(1, 101, 1):

        new_dict = pad_tiles(tile_dict)

        for k in new_dict.keys():

            neighbors = my_neighbors(tile_dict, k)

            try:
                
                if tile_dict[k] > 0 and (neighbors == 0 or neighbors > 2):

                    new_dict[k] = 0

                elif tile_dict[k] == 0 and neighbors == 2:

                    new_dict[k] = 1

            except:

                if neighbors == 2:

                    new_dict[k] = 1


        tile_dict = {k:v for k,v in new_dict.items()}

    return sum(tile_dict.values())

print(tile_flips('inputs/24/test_a.txt'))
print(tile_flips('inputs/24/input.txt'))