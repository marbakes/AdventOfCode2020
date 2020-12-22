def directions(file_name):
    with open(file_name, 'r') as reader:
        return  [i.strip() for i in reader.readlines()]


def navigate(file_name):
    ship_x = 0
    ship_y = 0
    x = 10
    y = 1
    
    faces_dict = {
        'N' : {
            'x': 0,
            'y': 1
        },
        'E': {
            'x': 1,
            'y': 0
        },
        'S': {
            'x': 0,
            'y': -1
        },
        'W': {
            'x': -1,
            'y': 0
        }
    }

    for action in directions(file_name):
        
        d = action[0]
        i = int(action[1:])
        
        if d in faces_dict.keys():

            x += i * faces_dict[d]['x']
            y += i * faces_dict[d]['y']

        elif d == 'F':

            ship_x += i * x
            ship_y += i * y

        elif d == 'L':
      
            for i in range(1, int(i / 90) + 1):
                x, y = (-y, x)

        elif d == 'R':

            for i in range(1, int(i / 90) + 1):
                x, y = (y, -x)

    return abs(ship_x) + abs(ship_y)

print(navigate('inputs/12/test_a.txt'))
print(navigate('inputs/12/input_a.txt'))