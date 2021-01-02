
def bus_schedule(file_name):
    with open(file_name, 'r') as reader:
        s = [i.strip() for i in reader.readlines()]
        t = int(s[0])
        b = [int(i) for i in s[1].split(",") if i != 'x']

    return t, b

def next_bus(file_name):

    t, b = bus_schedule(file_name)

    i = 0

    while t > 0:
        for bus in b:
            if (t + i) % bus == 0:
                return i * bus

        i += 1

def buses_only(file_name):

    with open(file_name, 'r') as reader:
        s = [i.strip() for i in reader.readlines()][1].split(',')

    buses_dict = {}
    j = 0 

    for i in s:
        try:
            buses_dict[int(i)] = j
        except:
            pass

        j += 1

    return buses_dict

def bus_alignment(file_name):

    buses_dict = buses_only(file_name)

    for k, v in buses_dict.items():
        if v == 0:
            i = k
            break

    j = 1

    align_keys = []

    while i >= 0:

        for k, v in buses_dict.items():

            aligned = (i + v) % k == 0

            if aligned:

                if k not in align_keys:

                    align_keys.append(k)

                    j *= k

            else:

                break

        if aligned:

            return i

        i += j

print(bus_alignment('inputs/13/input.txt'))