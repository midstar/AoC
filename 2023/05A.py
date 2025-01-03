import sys

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
    seeds = [eval(i) for i in seedsStr]
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
    for seed in seeds:
        fromType = 'seed'
        fromValue = seed
        while fromType in maps:
            toValue = mapValue(fromValue, maps[fromType]['map'])
            #print('%s: %s -> %s' % (fromType, fromValue, toValue))
            fromType = maps[fromType]['to']
            fromValue = toValue
        #print('%s: %s' % (fromType, fromValue))
        if lowest == -1 or lowest > fromValue:
            lowest = fromValue

    return lowest

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))