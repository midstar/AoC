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

def possibilities(field, groups, start_index = 0):
    if '?' not in field:
        if is_possible(field, groups):
            return 1
        else:
            return 0
    if field.count('#') > sum(groups):
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




def solve(input):
    lines = input.splitlines()

    result = 0
    for line in lines:
        field = line.split()[0]
        groups = line.split()[1].split(',')
        groups = [int(i) for i in groups]
        p = possibilities(field, groups, 0)
        result += p
        #print('--------------', field, groups, p)

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