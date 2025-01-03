import sys

def copy_range(range):
    return {
        'x' : { 'min' : range['x']['min'], 'max' : range['x']['max'] },
        'm' : { 'min' : range['m']['min'], 'max' : range['m']['max']  },
        'a' : { 'min' : range['a']['min'], 'max' : range['a']['max']  },
        's' : { 'min' : range['s']['min'], 'max' : range['s']['max']  },
        }

def accepted_ranges(workflows, range_in, next):
    ranges = []
    range = copy_range(range_in)
    if next == 'A':
        ranges.append(range)
        return ranges
    if next == 'R':
        return []
    for step in workflows[next]:
        variable, comp, value, next_wf = step
        if comp == '>':
            if range[variable]['max'] <= value:
                continue # Not possible
            range_new = copy_range(range)
            range_new[variable]['min'] = max(value + 1, range[variable]['min'])
            ranges += accepted_ranges(workflows, range_new, next_wf)
            range[variable]['max'] = value
            if range[variable]['max'] < range[variable]['min']:
                break # not possible to continue
        elif comp == '<':
            if range[variable]['min'] >= value:
                continue # Not possible
            range_new = copy_range(range)
            range_new[variable]['max'] = min(value - 1, range[variable]['max'])
            ranges += accepted_ranges(workflows, range_new, next_wf)
            range[variable]['min'] = value
            if range[variable]['max'] < range[variable]['min']:
                break # not possible to continue
        elif next_wf == 'A':
            ranges.append(range)
        elif next_wf != 'R':
            ranges += accepted_ranges(workflows, range, next_wf)
    return ranges

def solve(input):
    workflow_rating = input.split('\n\n')  
    workflows = {}  
    for line in workflow_rating[0].splitlines():
        name = line[:line.index('{')]
        workflows[name] = []
        rules = line[line.index('{') + 1:-1].split(',')
        for rule in rules:
            variable = ''
            comp = ''
            value = 0
            next = rule
            u = rule.split(':')
            if len(u) > 1:
                next = u[1]
                for c in ['<', '>']:
                    s = u[0].split(c)
                    if len(s) > 1:
                        variable = s[0]
                        comp = c
                        value = int(s[1])
            workflows[name].append((variable, comp, value, next))
    #print(workflows)

    start_range = {
        'x' : { 'min' : 1, 'max' : 4000 },
        'm' : { 'min' : 1, 'max' : 4000 },
        'a' : { 'min' : 1, 'max' : 4000 },
        's' : { 'min' : 1, 'max' : 4000 },
    }
    ranges = accepted_ranges(workflows, start_range, 'in')
    #print(ranges)

    result = 0
    for range in ranges:
        ans = 1
        for c in 'xmas':
            ans *= 1 + range[c]['max'] - range[c]['min']
        result += ans


    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))