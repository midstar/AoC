import sys


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
    #print(workflow)

    ratings_list = []
    for line in workflow_rating[1].splitlines():
        ratings_s = line[1:-1].split(',')
        ratings = {}
        for rating_s in ratings_s:
            s = rating_s.split('=')
            ratings[s[0]] = int(s[1])
        ratings_list.append(ratings)
    #print(ratings_list)

    result = 0
    for ratings in ratings_list:
        next = 'in'
        while True:
            if next == 'R':
                break
            if next == 'A':
                for variable, value in ratings.items():
                    result += value
                break
            workflow = workflows[next]
            for step in workflow:
                variable, comp, value, next_wf = step
                if variable == '':
                    next = next_wf
                    break
                elif comp == '>':
                    if variable in ratings:
                        if ratings[variable] > value:
                            next = next_wf
                            break
                elif comp == '<':
                    if variable in ratings:
                        if ratings[variable] < value:
                            next = next_wf
                            break
    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))