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

def is_maybe_possible(field, groups):
    if field.count('#') > sum(groups):
        return False
    complete_groups = field[:field.index('?')].replace('.',' ').split()
    l = len(complete_groups)
    if (l == 0):
        return True
    if (l > len(groups)):
        return False
    last_index = l - 1
    if len(complete_groups[last_index]) > groups[last_index]:
        return False
    tmp = complete_groups.pop() # Last cannot be trusted
    l = len(complete_groups)
    for i in range(0, l):
        if len(complete_groups[i]) != groups[i]:
            return False
    
    if len(groups) > l:
        rest = tmp + '.' + field[field.index('?'):] 
        remaining_groups = groups[l:]
        if (sum(remaining_groups) + len(remaining_groups) - 1) > len(rest) :
            return False 
    

    return True

def possibilities(field, groups, start_index = 0):
    #print(field)
    if '?' not in field:
        if is_possible(field, groups):
            return 1
        else:
            return 0
    if not is_maybe_possible(field, groups):
        return 0
    if start_index >= len(field):
        return 0

    count = 0
    start_index = field.index('?')
    
    field_tmp = field.replace('?', '.', 1)
    count += possibilities(field_tmp, groups, start_index + 1)
    
    field_tmp = field.replace('?', '#', 1)
    count += possibilities(field_tmp, groups, start_index + 1)

    return count

storage = {}

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
        print(field_l, groups_l)
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