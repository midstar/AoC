import sys
import math

class Monkey():
    def __init__(self, operation, test, true_monkey, false_monkey):
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.items = []
        self.inspections = 0
    
    def lcm(self, lcm):
        self.lcm = lcm
    
    def add(self, item):
        self.items.append(item)
    
    def run(self):
        result = []
        while self.items:
            self.inspections += 1
            item = self.items.pop(0)
            operation = self.operation.replace('old', str(item))
            val = eval(operation)
            val = val % self.lcm
            if val % self.test == 0:
                result.append((self.true_monkey, val))
            else:
                result.append((self.false_monkey, val))
        return result



def solve(input):
    monkeys = []
    tests = []

    monkeysLines = [l.splitlines() for l in input.split('\n\n')]
    for monkeyLines in monkeysLines:
        operation = monkeyLines[2].split('=')[1]
        test = int(monkeyLines[3].split()[-1])
        tests.append(test)
        true_monkey = int(monkeyLines[4].split()[-1])
        false_monkey = int(monkeyLines[5].split()[-1])
        monkey = Monkey(operation, test, true_monkey, false_monkey)
        for item in monkeyLines[1].split(':')[1].split(','):
            monkey.add(int(item))
        monkeys.append(monkey)
    
    lcm = math.lcm(*tests)
    for monkey in monkeys: monkey.lcm(lcm)
    
    for i in range(0, 10_000):
        for j, monkey in enumerate(monkeys):
            next_items = monkey.run()
            for next, item in next_items:
                monkeys[next].add(item)
        '''
        print('Round', i + 1)
        for j, monkey in enumerate(monkeys):
            print(f'  Monkey {j}:', monkey.inspections)
        '''
        


    inspections = [m.inspections for m in monkeys]
    #for j, val in enumerate(inspections):
    #    print(f'  Monkey {j}:', val)

    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))