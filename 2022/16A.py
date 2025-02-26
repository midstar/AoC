import sys, re

def bfs(valves, start_valve, stop_value):
    q = [(0, start_valve)]
    visited = set()
    while q:
        steps, valve = q.pop(0)
        if valve == stop_value: return steps
        if valve in visited: continue
        visited.add(valve)
        for v in valves[valve]['to']:
            q.append((steps + 1, v))

def max_pressure(valves,valve,minutes_left,pressure = 0, visited=None):
    if not visited: visited = {valve}
    pressures = set()
    for valve2, minutes in valves[valve]['to']:
        if valve2 in visited: continue
        if minutes >= minutes_left: continue
        minutes_left2 = minutes_left - minutes
        pressure2 = pressure + minutes_left2 * valves[valve2]['flow_rate']
        pressures.add(max_pressure(valves,valve2,minutes_left2,pressure2, visited | {valve2}))
    if not pressures: return pressure
    return max(pressures)

def solve(input):
    first_valve = 'AA'
    valves = {}
    for line in input.splitlines():
        name, *to_names = re.findall(r'([A-Z]{2})', line)
        flow_rate = int(re.findall(r'(\d+)', line)[0])
        valves[name] = {
            'flow_rate' : flow_rate,
            'to' : to_names
        }

    # Only the first valve and all valves with flow_rate > 0 are relevant
    valid_valves = {key for key, value in valves.items() if value['flow_rate'] > 0}
    valid_valves.add(first_valve) # Always flow_rate == 0

    # Calc distance in minutes between all valves
    valves2 = {}
    for name in valid_valves:
        valves2[name] = {
            'flow_rate' : valves[name]['flow_rate'],
            'to' : set()
        }
        for name2 in valid_valves:
            if name2 == name: continue
            # Add extra minute (+1) for opening the valve
            valves2[name]['to'].add((name2,bfs(valves,name,name2) + 1))
    valves = valves2

    return max_pressure(valves,first_valve,30)  
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))