import sys

def mapValueOne(value, mapDict):
    for src, dst_range in mapDict.items():
        rangeV = dst_range['range']
        if value >= src and value < (src + rangeV):
            offset = value - src
            return dst_range['dst'] + offset
    return value

def mapValue(value, maps):
        fromType = 'seed'
        fromValue = value
        while fromType in maps:
            toValue = mapValueOne(fromValue, maps[fromType]['map'])
            fromType = maps[fromType]['to']
            fromValue = toValue
        return fromValue

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

    for seed in seeds:
        #print(seed)
        value = seed['start']
        size = seed['start'] + seed['len']
        while value < size:
            toValue = mapValue(value, maps)
            if lowest == -1 or lowest > toValue:
                lowest = toValue
            # Fast check forward if we are in same map
            step = 1000
            testValue = min(value + step, size)
            testToValue = mapValue(testValue, maps)
            if (toValue + step) == testToValue:
                value = testValue
            else: 
                value += 1

    return lowest

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))