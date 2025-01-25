import sys

def fuel_one(dist):
    return int(dist * (1 + dist) / 2)

def fuel(crabs, pos):
    return sum(fuel_one(abs(crab - pos)) for crab in crabs)

def fuel_lowest(crabs, fuel_current, pos, inc):
    f = fuel(crabs, pos)
    if f > fuel_current:
        return fuel_current
    return fuel_lowest(crabs, f, pos + inc, inc)

def solve(input):
    crabs = list(map(int,input.strip().split(',')))
    avg_pos = round(sum(crabs) / len(crabs))
    avg_fuel = fuel(crabs,avg_pos)
    return min(fuel_lowest(crabs,avg_fuel,avg_pos,-1),fuel_lowest(crabs,avg_fuel,avg_pos,1))
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))