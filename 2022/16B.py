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

def all_paths(valves,valve,minutes_left,pressure = 0, visited=None):
    if not visited: visited = {valve}
    all_p = []
    for valve2, minutes in valves[valve]['to']:
        if valve2 in visited: continue
        if minutes >= minutes_left: continue
        minutes_left2 = minutes_left - minutes
        pressure2 = pressure + minutes_left2 * valves[valve2]['flow_rate']
        all_p += all_paths(valves,valve2,minutes_left2,pressure2, visited | {valve2})
    if all_p: return all_p
    return [[pressure,visited]]

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

    paths = all_paths(valves,first_valve,26)
    max_pressure, max_valves = max(paths)

    # Find best path not including valves from max_path
    pre_visited = max_valves.copy()
    pre_visited.remove('AA')
    min_pressure, _ = max(all_paths(valves,first_valve,26,0,pre_visited))

    # Remove all paths smaller than min_pressure. This is just to reduce
    # the number of paths in next step
    paths = [(p, v) for p, v in paths if p >= min_pressure]

    # Check non-intersecting paths
    result = 0
    while paths:
        my_pressure, my_valves = paths.pop()
        my_valves.remove('AA')
        for other_pressure, other_valves in paths:
            if bool(my_valves & other_valves) == False:
                result = max(result,my_pressure + other_pressure)

    return result
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))