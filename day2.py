import re

def password_verify(entries):

    import re

    with open(entries, 'r') as reader:

        entries_list = [i.strip() for i in reader.readlines()]

    valids = 0

    for entry in entries_list:

        bottom = int(re.findall('\d+-', entry)[0][:-1])
        top = int(re.findall('-\d+', entry)[0][1:])

        letter = re.findall('[a-z]', entry)[0]

        count = len(re.findall(letter, entry)) - 1

        if count >= bottom and count <= top:
            valids += 1

        else:
            pass

    return valids

def password_verify_new(entries):

    with open(entries, 'r') as reader:

        entries_list = [i.strip() for i in reader.readlines()]

    valids = 0

    for entry in entries_list:

        bottom = int(re.findall('\d+-', entry)[0][:-1])
        top = int(re.findall('-\d+', entry)[0][1:])

        letter = re.findall('[a-z]', entry)[0]

        password = re.findall(': [a-z]+', entry)[0][2:]

        if [password[bottom - 1], password[top -1]].count(letter) == 1:

            valids +=1

        else:
            pass

    return valids



print(password_verify_new('inputs/02/test_a.txt'))
print(password_verify_new('inputs/02/input_a.txt'))


