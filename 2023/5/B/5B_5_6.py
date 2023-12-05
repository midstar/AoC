import argparse

def mapValue(value, mapDict):
    for src, dst_range in mapDict.items():
        rangeV = dst_range['range']
        if value >= src and value < (src + rangeV):
            offset = value - src
            return dst_range['dst'] + offset
    return value

def solve(input):
    lines = input.splitlines()
    seedsStr = lines[0].split(':')[1].split()
    seeds = []
    while len(seedsStr) > 0:
        seeds.append({
            'start' : int(seedsStr.pop(0)),
            'len' : int(seedsStr.pop(0))
        })
    lines = lines[2:]
    maps = {}
    while len(lines) > 0:
        name = lines.pop(0).split(':')[0]
        from_to = name.split('-')
        fromV = from_to[0]
        toV = from_to[2].split()[0]
        maps[fromV] = {
            'to' : toV,
            'map': {}
        }
        entry = lines.pop(0)
        while entry != "":
            items = entry.split()
            maps[fromV]['map'][int(items[1])] = {
                'dst' : int(items[0]),
                'range' : int(items[2])
            }
            if len(lines) == 0:
                break
            entry = lines.pop(0)
    #print(maps)
    
    lowest = -1
    for i in range(4,6): 
        seed = seeds[i]
        print(seed)
        count = 0
        length = seed['len']
        hundred = int(length / 100)
        for value in range(seed['start'], seed['start'] + seed['len']):
            count += 1
            if count % hundred == 0:
                print('%s percent' % (count / hundred))
            fromType = 'seed'
            fromValue = value
            while fromType in maps:
                toValue = mapValue(fromValue, maps[fromType]['map'])
                #print('%s: %s -> %s' % (fromType, fromValue, toValue))
                fromType = maps[fromType]['to']
                fromValue = toValue
            #print('%s: %s' % (fromType, fromValue))
            if lowest == -1 or lowest > fromValue:
                lowest = fromValue

    print('Result: %s' % str(lowest))

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    