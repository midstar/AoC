import argparse

def is_possible(field, groups):
    f = field.split()[0].split('.')
    f = [i for i in f if i != '']
    if len(f) == len (groups):
        for i in range(0, len(f)):
            if len(f[i]) != groups[i]:
                return False
        return True
    return False

def remaining(field, groups):
    field_first = field
    field_last = ''

    if '?' in field:
        i = field.index('?')
        while i > 0 and field[i - 1] == '#':
            i -= 1
        field_first = field[:i]
        field_last = field[i:]

    h = field_first.replace('.', ' ').split()
    if len(h) > len(groups):
        return (None, None) # Invalid
    for i in range(0, len(h)):
        if len(h[i]) != groups[i]:
            return (None, None) # Invalid
    
    groups_first = groups[:len(h)]
    groups_last = groups[len(h):]

    # Validity check - enough space
    if (sum(groups_last) + len(groups_last) - 1) > len(field_last):
        return (None, None) # Invalid

    # Validity check - remaining sum
    if (sum(groups_last) < field_last.count('#')):
        return (None, None) # Invalid

    return (field_last, groups_last)

# Storage of results key = (field, tuple(groups)) value = count
storage = {}

def possibilities(field, groups):
    if '?' not in field:
        if is_possible(field, groups):
            return 1
        else:
            return 0
    
    key = (field, tuple(groups))
    if key in storage:
        return storage[key]

    field, groups = remaining(field, groups)
    if field == None:
        return 0

    count = 0
    count += possibilities(field.replace('?','.',1), groups)
    count += possibilities(field.replace('?','#',1), groups)

    storage[key] = count

    return count



def possibilities_fast(field, groups):
    field_l = field.replace('.',' ').split()
    if len(field_l) == 0:
        return 1
    if len(field_l) == 1:
        return possibilities(field, groups)
    
    result = 0
    f = field_l.pop(0)
    for j in range(0, len(groups) + 1):
        g = groups[0:j]
        key = (f, tuple(g))
        res = 0
        if key in storage:
            res = storage[key]
        else:
            res = possibilities(f, g)
            storage[key] = res
        #print(' - ',f, g, res)
        if res > 0:
            result += res * possibilities_fast('.'.join(field_l), groups[j:])
    #print(field, groups, result)
    return result

def solve(input):
    lines = input.splitlines()

    result = 0
    for line in lines:
        field = line.split()[0]
        groups = line.split()[1].split(',')
        groups = [int(i) for i in groups]
        field_l = ''
        groups_l = []
        for i in range(0, 5):
            field_l += field
            if i < 4:
                field_l += '?'
            groups_l.extend(groups)
        #p = possibilities('??????????????????????????????????????????????????????????????????????????', [1, 7, 1, 7, 1, 7, 1, 7, 1, 7], 0)
        #p = possibilities_fast('??#.?????#??????', [1, 1, 1, 1, 6])
        #print(p)
        #exit()
        #field_l = field
        #groups_l = groups
        print(field_l, groups_l)
        #p = possibilities(field_l, groups_l)
        p = possibilities_fast(field_l, groups_l)
        print(p)
        result += p

    print('Result: %s' % result)

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    