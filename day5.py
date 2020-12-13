def read_entries(entries):
    with open(entries, 'r') as reader:
        return [x.strip() for x in reader.readlines()]

def boarding_pass(entries):

    seat_ids = []

    for bp in read_entries(entries):
        s = 0
        n = 127
        w = 0
        e = 7
        

        for p in bp:
            if p == 'F':
                n = int(n - (n-s) / 2 - 0.5)

            elif p == 'B':
                s = int(s + (n-s) / 2 + 0.5)

            elif p == 'L':
                e = int(e - (e-w) / 2 - 0.5)

            else:
                w = int(w + (e-w) / 2 + 0.5)

        seat_ids.append(s * 8 + w)

    # return max(seat_ids)

    for i in range(min(seat_ids), max(seat_ids)):
        if i not in seat_ids and (i-1) in seat_ids and (i+1) in seat_ids:
            return i

print(boarding_pass('inputs/05/input_a.txt'))