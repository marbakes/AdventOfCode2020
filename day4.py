import re

def batchdocs(batch):
    with open(batch, 'r') as reader:
        return re.split('\n\n', reader.read())


# for x in [
#     'pid:000000001',
#     'pid:0123456789',
#     'pid:860033327',
#     'pid:028048884'
# ]:
#     print(x, re.findall('pid:[0-9]{9}', x))

def verify(batch):

    reqfields = {
            'byr': 'byr:(19[2-9][0-9]|200[0-2])', #- four digits; at least 1920 and at most 2002
            'iyr': 'iyr:(201[0-9]|2020)', #- four digits; at least 2010 and at most 2020
            'eyr': 'eyr:(202[0-9]|2030)', #- four digits; at least 2020 and at most 2030
            'hgt': 'hgt:(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))', #- a number followed by either cm or in:
                        #If cm, the number must be at least 150 and at most 193.
                        #If in, the number must be at least 59 and at most 76.
            'hcl': 'hcl:#([0-9]|[a-f]){6}', #- a # followed by exactly six characters 0-9 or a-f
            'ecl': 'ecl:(amb|blu|brn|gry|grn|hzl|oth)', #- exactly one of: amb blu brn gry grn hzl oth
            'pid': 'pid:[0-9]{9}(\s|\Z)' #- a nine-digit number, including leading zeroes
    }

    validcount = 0

    for doc in batchdocs(batch):

        valid = True

        for fieldname in reqfields.keys():

            if len(re.findall(reqfields[fieldname],doc)) == 0:

                valid = False

        if valid:

            validcount += 1

    return validcount


print('All valid', verify('inputs/04/test_c.txt'))
print('None valid', verify('inputs/04/test_b.txt'))
print('Input: ', verify('inputs/04/input_a.txt'))